param(
    [switch]$ForceExplorerRestart
)

# Determine project root (parent of this script's directory: .../tools )
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$rootDir   = Split-Path -Parent $scriptDir

Write-Host "Script directory : $scriptDir"
Write-Host "Project root     : $rootDir"

if (-not (Test-Path $rootDir)) { Write-Host "Root directory not found."; exit 1 }

########################
# PATH handling: include tools directory (where launchers live)
########################
$userPath = [Environment]::GetEnvironmentVariable('PATH','User')
$entries = @(); if ($userPath) { $entries = $userPath -split ';' | Where-Object { $_ -ne '' } }
if ($entries -notcontains $scriptDir) {
    $newPath = ($scriptDir + ';' + $userPath).TrimEnd(';')
    [Environment]::SetEnvironmentVariable('PATH',$newPath,'User')
    Write-Host "Prepended tools directory to user PATH." } else { Write-Host "Tools directory already in user PATH." }

# (VBS launcher removed per requirement; only exe launcher maintained)

# Build lc.exe if possible
try {
    $exePath = Join-Path $scriptDir 'lc.exe'; $need=$true
    if (Test-Path $exePath) { if ( (Get-Item $exePath).LastWriteTimeUtc -ge (Get-Item $MyInvocation.MyCommand.Definition).LastWriteTimeUtc ) { $need=$false } }
    if ($need) {
        $cands = @("$env:WINDIR\Microsoft.NET\Framework\v4.0.30319\csc.exe","$env:WINDIR\Microsoft.NET\Framework64\v4.0.30319\csc.exe") | Where-Object { Test-Path $_ }
        if ($cands) {
            $csc = $cands[0]; $csTmp = Join-Path $scriptDir 'lc_launcher.tmp.cs'
            $src = @'
using System;using System.Diagnostics;class Program{[STAThread]static void Main(){try{string dir="@@ROOT@@";var p=new ProcessStartInfo("cmd.exe","/c code \""+dir+"\"");p.CreateNoWindow=true;p.UseShellExecute=false;Process.Start(p);}catch{}}}
'@ -replace '@@ROOT@@',[Regex]::Escape($rootDir).Replace("\\","\\\\")
            Set-Content -Path $csTmp -Value $src -Encoding UTF8
            & $csc /nologo /target:winexe /out:"$exePath" "$csTmp" | Out-Null
            Remove-Item $csTmp -ErrorAction SilentlyContinue
            if (Test-Path $exePath) { Write-Host "Built tools/lc.exe." } else { Write-Host "Build lc.exe failed." }
        } else { Write-Host "csc.exe not found; skipping lc.exe (tools)." }
    } else { Write-Host "tools/lc.exe up-to-date." }
} catch { Write-Host "Build error: $($_.Exception.Message)" }

# Broadcast env change
try { Add-Type @'
using System;using System.Runtime.InteropServices;public class EnvRefresh{[DllImport("user32.dll",SetLastError=true,CharSet=CharSet.Auto)]public static extern IntPtr SendMessageTimeout(IntPtr hWnd,int Msg,IntPtr wParam,string lParam,int fuFlags,int uTimeout,out IntPtr lpdwResult);} 
'@ -ErrorAction SilentlyContinue | Out-Null; [EnvRefresh]::SendMessageTimeout([IntPtr]0xffff,0x1A,[IntPtr]0,'Environment',2,5000,[ref]([IntPtr]::Zero))|Out-Null; Write-Host "Broadcasted environment change." } catch {}

if ($ForceExplorerRestart) { Write-Host "Restarting Explorer..."; try { Get-Process explorer -ErrorAction SilentlyContinue | Stop-Process -Force; Start-Sleep 1; Start-Process explorer.exe; Write-Host "Explorer restarted." } catch { Write-Host "Explorer restart failed: $($_.Exception.Message)" } }

Write-Host "Done. Win+R -> lc will open project root: $rootDir (exe launcher only)."
