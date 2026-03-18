# scripts/install_windows.ps1
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "AI Coding Language Benchmark - Windows Auto Installer" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

Write-Host "Checking/Installing Winget packages..." -ForegroundColor Yellow

$wingetPackages = @(
    "Golang.Go",
    "OpenJS.NodeJS",
    "Rustlang.Rustup",
    "RubyInstallerTeam.RubyWithDevkit",
    "EclipseAdoptium.Temurin.21.JDK",
    "StrawberryPerl.StrawberryPerl",
    "Haskell.ghcup"
)

foreach ($pkg in $wingetPackages) {
    Write-Host "Installing $pkg..."
    winget install --id $pkg --accept-package-agreements --accept-source-agreements
}

Write-Host "------------------------------------------------------------" -ForegroundColor Cyan
Write-Host "Installing sub-dependencies (TypeScript, Mypy, Steep)..." -ForegroundColor Yellow

Write-Host "Installing TypeScript..."
npm install -g typescript

Write-Host "Installing Python Mypy..."
python -m pip install mypy

Write-Host "Installing Ruby Steep..."
gem install steep

Write-Host "============================================================" -ForegroundColor Green
Write-Host "You may need to restart your terminal after the script finishes to ensure all PATH variables are updated." -ForegroundColor Green