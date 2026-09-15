"""Retained remote POSIX descriptor observation; never reads the credential."""
import json
import os
import pathlib
import stat
import sys
import time


KEYS = {"schema", "host", "nonce", "secret_parent", "secret_leaf", "state_leaf",
        "terminal_leaf", "bootstrap_sha256"}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def parse(raw):
    def unique(pairs):
        value = {}
        for key, item in pairs:
            if key in value:
                raise ValueError("duplicate key")
            value[key] = item
        return value
    value = json.loads(raw, object_pairs_hook=unique)
    if not isinstance(value, dict) or set(value) != KEYS or raw != canonical(value):
        raise ValueError("noncanonical config")
    return value


def absent(parent_fd, leaf):
    try:
        os.stat(leaf, dir_fd=parent_fd, follow_symlinks=False)
        return False
    except FileNotFoundError:
        return True


def observe(config):
    if os.name != "posix" or config["schema"] != "auto-switch-q4-r9-descriptor-preflight-config/v1":
        raise ValueError("POSIX only")
    leaves = (config["secret_leaf"], config["state_leaf"], config["terminal_leaf"])
    if (len(set(leaves)) != 3 or any(not isinstance(leaf, str) or pathlib.PurePosixPath(leaf).name != leaf for leaf in leaves)
            or any(not leaf.startswith("q4-r9-") for leaf in leaves[1:])):
        raise ValueError("unsafe leaf")
    parent_fd = secret_fd = None
    try:
        parent_fd = os.open(config["secret_parent"], os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC)
        parent = os.fstat(parent_fd)
        secret_fd = os.open(config["secret_leaf"], os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=parent_fd)
        secret = os.fstat(secret_fd)
        if (not stat.S_ISDIR(parent.st_mode) or parent.st_uid != 0 or parent.st_gid != 0
                or stat.S_IMODE(parent.st_mode) != 0o700 or not stat.S_ISREG(secret.st_mode)
                or secret.st_uid != 0 or secret.st_gid != 0 or stat.S_IMODE(secret.st_mode) != 0o600
                or not 1 <= secret.st_size <= 4096):
            raise ValueError("unsafe objects")
        state_absent = absent(parent_fd, config["state_leaf"])
        terminal_absent = absent(parent_fd, config["terminal_leaf"])
        if not state_absent or not terminal_absent:
            raise ValueError("occupied leaf")
        credential = {
            "schema": "auto-switch-q4-r9-credential/v1",
            "parent_device": parent.st_dev, "parent_inode": parent.st_ino,
            "parent_uid": parent.st_uid, "parent_gid": parent.st_gid,
            "parent_mode": stat.S_IMODE(parent.st_mode),
            "secret_device": secret.st_dev, "secret_inode": secret.st_ino,
            "secret_uid": secret.st_uid, "secret_gid": secret.st_gid,
            "secret_mode": stat.S_IMODE(secret.st_mode), "secret_size": secret.st_size,
            "secret_mtime_ns": secret.st_mtime_ns, "secret_leaf": config["secret_leaf"],
        }
        return {
            "schema": "auto-switch-q4-r9-descriptor-preflight/v1", "status": "PASS",
            "host": config["host"], "nonce": config["nonce"], "observed_unix_ns": time.time_ns(),
            "secret_parent": config["secret_parent"], "credential": credential,
            "state_leaf": config["state_leaf"], "terminal_leaf": config["terminal_leaf"],
            "state_absent": True, "terminal_absent": True,
            "bootstrap_sha256": config["bootstrap_sha256"],
        }
    finally:
        if secret_fd is not None:
            os.close(secret_fd)
        if parent_fd is not None:
            os.close(parent_fd)


def main():
    raw = sys.stdin.buffer.read(16385)
    if len(raw) > 16384:
        return 1
    sys.stdout.buffer.write(canonical(observe(parse(raw))))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception:
        raise SystemExit(1)
