$ErrorActionPreference = 'Stop'
$bash = 'C:\Program Files\Git\bin\bash.exe'
if (-not (Test-Path -LiteralPath $bash -PathType Leaf)) { throw 'MOCK_BASH_UNAVAILABLE' }
$live = [IO.File]::ReadAllText((Join-Path $PSScriptRoot 'task-2-secure-console-transfer-v61-live-source.md'))
$scope = [IO.File]::ReadAllText((Join-Path $PSScriptRoot 'task-2-secure-console-transfer-v61-scope-source.md'))
$cleanup = [regex]::Match($scope, '(?ms)\$remote = @''\n(?<code>.*?)\n''@').Groups['code'].Value
$rollback = [regex]::Match($live, '(?ms)\$rollback = @''\n(?<code>.*?)\n''@').Groups['code'].Value
if (-not $cleanup -or -not $rollback) { throw 'MOCK_SOURCE_EXTRACTION_FAILED' }
$mock = @'
mode="$1"
delete_count=0
trap 'printf "MOCK_DELETE_COUNT=%s\n" "$delete_count"' EXIT
sudo() {
    if [ "$1" = ss ]; then
        case "$mode" in
            present_pre) printf 'LISTEN 0 128 127.0.0.1:20130 0.0.0.0:*\n'; return 0 ;;
            error_pre) return 3 ;;
            present_post) if [ "$delete_count" -eq 1 ]; then printf 'LISTEN 0 128 127.0.0.1:20130 0.0.0.0:*\n'; fi; return 0 ;;
            error_post) if [ "$delete_count" -eq 1 ]; then return 3; fi; return 0 ;;
            absent) return 0 ;;
        esac
        return 91
    fi
    if [ "$1" != docker ]; then return 92; fi
    case "$2" in
        inspect)
            case "$4" in
                '{{.Id}}') printf '%s\n' aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ;;
                '{{.State.Status}}') printf 'running\n' ;;
                '{{.Image}}') printf 'sha256:5f5c8640aae01df9654968d946d8f1a56c497f1dd5c5cda4cf95ab7c14d58648\n' ;;
                '{{json .HostConfig.PortBindings}}') printf '{}\n' ;;
                *) return 93 ;;
            esac ;;
        network) if [ "$delete_count" -eq 0 ]; then printf '3\n'; else printf '2\n'; fi ;;
        rm)
            if [ "$4" != aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ]; then return 94; fi
            delete_count=$((delete_count + 1)) ;;
        ps) if [ "$delete_count" -ne 1 ]; then return 95; fi ;;
        *) return 96 ;;
    esac
}
'@
$cases = 0
foreach ($entry in @(@('cleanup', $cleanup), @('rollback', $rollback))) {
    foreach ($mode in @('present_pre', 'error_pre', 'present_post', 'error_post', 'absent')) {
        $scriptText = $mock + "`n" + $entry[1].Replace('__PROXY_ID__', ('a' * 64)) + "`n"
        $lines = @($scriptText | & $bash -s -- $mode 2>&1)
        $code = $LASTEXITCODE
        $text = $lines -join "`n"
        $expectedDeletes = if ($entry[0] -eq 'cleanup' -and $mode -in @('present_pre', 'error_pre')) { 0 } else { 1 }
        $expectedPass = $mode -eq 'absent'
        if (($code -eq 0) -ne $expectedPass -or
            $text.Contains('=PASS') -ne $expectedPass -or
            -not $text.Contains("MOCK_DELETE_COUNT=$expectedDeletes")) {
            throw "LISTENER_MOCK_FAIL=$($entry[0])/$mode EXIT=$code EXPECTED_DELETES=$expectedDeletes"
        }
        $cases++
    }
}
[Console]::Out.WriteLine("V61_LISTENER_MOCK=PASS CASES=$cases/10 REAL_DOCKER=0 REAL_SSH=0 REAL_DELETIONS=0")
