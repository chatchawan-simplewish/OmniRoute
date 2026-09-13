"""Focused offline regression for the bounded R4 candidate-start launcher."""
import ast
import pathlib
import runpy


ROOT = pathlib.Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "scripts/auto-switch-candidate-start-r4-20260913.py"

assert LAUNCHER.is_file(), "R4 launcher implementation missing"
module = runpy.run_path(str(LAUNCHER), run_name="candidate_start_r4_test")
assert module["CONTRACT"].is_file(), "R4 contract missing"
contract = module["CONTRACT"].read_text(encoding="utf-8")
assert "NOT EXECUTABLE" in contract and "independent Sol High review" in contract

assert module["SOURCE"] == "e53d895e9a5e38a7f06ce59de254835f10e829c1"
assert module["CANDIDATE_IID"] == "sha256:8211e1071a3b68eac01673d76129150eb0c0fea329dd222bc8bf0394b13fc844"
assert module["CANDIDATE_TAG"] == "omniroute-auto-switch-r3:" + module["SOURCE"]
assert module["TRANSFER_RESULT_HASH"] == "1146ddb26372878193223babc726db9764f367d41604660760b0640f6003261f"
assert module["TRANSPORT_HELPER_HASH"] == "78bb97e57d6229aae84c2f0d0caaf68eeb71ba6b92e69415d83af2a869b8224a"

payload = module["render_remote"]()
ast.parse(payload)
assert "subprocess.run" not in payload
assert "subprocess.Popen" in payload
assert "CANDIDATE_NAME='omniroute-auto-switch-candidate-r4-20260913'" in payload
assert "CANDIDATE_VOLUME='omniroute-auto-switch-candidate-data-r4-20260913'" in payload
assert "RETAINED_R3_ID='6b1089d2b14c175448ca48437e63a7ea0f880deb6374eee26ebf8bc96f498663'" in payload
assert "RETAINED_OLD_IID='sha256:a91994bf883698d4520ff048d16be999d4614331a528c76c0b95bc6dc8bec803'" in payload
assert payload.count("'OMNIROUTE_DISABLE_BACKGROUND_SERVICES':'true'") == 2
assert "'OMNIROUTE_DISABLE_BACKGROUND_SERVICES':'1'" not in payload
assert "--network','none" in payload and "--read-only" in payload
assert "container','rm" not in payload and "volume','rm" not in payload
assert "171_agent_route_deferred_metrics" in payload
assert "deferred_requests" in payload

module["offline_check"]()
print("PASS: R4 pins, retained candidates, migration 171, isolation and bounded capture; no remote calls")
