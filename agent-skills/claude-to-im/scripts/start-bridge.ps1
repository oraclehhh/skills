$ErrorActionPreference = 'Stop'
$CtiHome = Join-Path $env:USERPROFILE '.claude-to-im'
$RuntimeDir = Join-Path $CtiHome 'runtime'
$PidFile = Join-Path $RuntimeDir 'bridge.pid'
$StatusFile = Join-Path $RuntimeDir 'status.json'
$LogFile = Join-Path $CtiHome 'logs' 'bridge.log'
$SkillDir = Split-Path -Parent $PSCommandPath | Split-Path -Parent
$DaemonMjs = Join-Path $SkillDir 'dist' 'daemon.mjs'

# Ensure directories
@('data','logs','runtime','data/messages') | ForEach-Object {
    $dir = Join-Path $CtiHome $_
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
}

# Clean CLAUDECODE env var
[System.Environment]::SetEnvironmentVariable('CLAUDECODE', $null)

# Read config.env
$configPath = Join-Path $CtiHome 'config.env'
if (Test-Path $configPath) {
    Get-Content $configPath | ForEach-Object {
        if ($_ -match '^([^#=]+)=(.*)$') {
            $name = $Matches[1].Trim()
            $value = $Matches[2].Trim()
            [System.Environment]::SetEnvironmentVariable($name, $value)
        }
    }
}

$nodePath = (Get-Command node).Source
Write-Host "Starting bridge from: $DaemonMjs"

$proc = Start-Process -FilePath $nodePath `
    -ArgumentList "`"$DaemonMjs`"" `
    -WorkingDirectory $SkillDir `
    -WindowStyle Hidden `
    -RedirectStandardOutput $LogFile `
    -RedirectStandardError $LogFile `
    -PassThru

Set-Content -Path $PidFile -Value $proc.Id
Write-Host "Bridge started (PID: $($proc.Id))"
Start-Sleep -Seconds 3

# Check status
if (Test-Path $StatusFile) {
    Get-Content $StatusFile -Raw
} else {
    Write-Host "Status file not yet created"
}
