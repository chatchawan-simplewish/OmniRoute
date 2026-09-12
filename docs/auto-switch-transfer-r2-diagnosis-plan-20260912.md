# R2 builder-read diagnosis plan

R2 is spent. Its single invocation returned only `builder_read` / `CHECK_FAILED`; that envelope cannot identify a failing assertion. This is preparation for one separately reviewed, read-only builder diagnostic. It authorizes neither a transfer retry nor any export, archive mutation, cleanup, target contact, Docker load, service operation, credential access, or provider request.

## Exact R2 checks that could have failed

The frozen launcher first requires the retained archive to be a regular, non-symlink file and have a positive byte size. It then hashes the whole archive. Its capacity helper then checks `/var/tmp`, the string returned by unprivileged `docker info` for `DockerRootDir`, and, if Docker reports `io.containerd.snapshotter.v1`, a containerd root parsed from the sole `containerd` process with an explicit `--config` argument and that config's quoted `root` setting. Every checked filesystem must have at least twice the archive size plus 1 GiB according to `sudo -n df -Pk`.

The capacity helper returns `False` whenever Docker does not report the containerd snapshotter. The outer builder stage converts that `False` into `builder_read:containerd_path_unproven`, even if every archive and DockerRootDir check passed. That is a confirmed source flaw: builder-read unnecessarily requires a containerd path although it only reads the retained archive and does not load an image. The other candidates are not proven: unreadable/non-regular archive; hash read failure; insufficient space; unprivileged Docker info failure or malformed data; unavailable `sudo -n`; non-single/undetectable containerd process; inaccessible or unparseable config; absent/relative containerd root; or `df` failure/invalid output.

## Minimal fresh diagnostic

One bounded SSH call to the builder should make no writes and return a fixed JSON object with independent labels only: `archive_kind`, `archive_size`, `archive_sha256`, `var_tmp_capacity`, `docker_root_metadata`, `docker_root_capacity`, `driver_status`, `containerd_metadata`, and `containerd_capacity`. Each label is `PASS`, `FAIL`, `NOT_APPLICABLE`, or `UNPROVEN`; numeric archive size is included only when metadata is valid. It must map command errors, parse errors, and timeouts to those labels without retaining or printing stdout, stderr, paths other than the already pinned archive path, process arguments, configuration contents, image configuration, or secrets.

The diagnostic should evaluate later checks independently where their inputs are available, not stop at the first failure. It may inspect Docker info, the containerd process/config metadata, and filesystem statistics, but must not invoke `docker save`, `docker load`, image inspection, export, copy, mkdir, removal, or target SSH. Its result is evidence for a new reviewed procedure only; it cannot authorize continuation of R2.
