# Unregister tools directory launchers (which open project root)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$rootDir   = Split-Path -Parent $scriptDir
Write-Host "Tools dir    : $scriptDir"
Write-Host "Project root : $rootDir"

$userPath = [Environment]::GetEnvironmentVariable('PATH','User')
if ($userPath -match [Regex]::Escape($scriptDir)) {
  $newPath = ($userPath -split ';' | Where-Object { $_ -and $_ -ne $scriptDir }) -join ';'
  [Environment]::SetEnvironmentVariable('PATH',$newPath,'User')
  Write-Host "Removed tools directory from user PATH." } else { Write-Host "Tools directory not in user PATH." }

foreach ($f in 'lc.exe','lc.cmd') { $p = Join-Path $scriptDir $f; if (Test-Path $p) { Remove-Item $p -ErrorAction SilentlyContinue; Write-Host "Deleted $f" } }

try { Add-Type @'
using System;using System.Runtime.InteropServices;public class EnvRefresh{[DllImport("user32.dll",SetLastError=true,CharSet=CharSet.Auto)]public static extern IntPtr SendMessageTimeout(IntPtr hWnd,int Msg,IntPtr wParam,string lParam,int fuFlags,int uTimeout,out IntPtr lpdwResult);} 
'@ -ErrorAction SilentlyContinue | Out-Null; [EnvRefresh]::SendMessageTimeout([IntPtr]0xffff,0x1A,[IntPtr]0,'Environment',2,5000,[ref]([IntPtr]::Zero))|Out-Null; Write-Host "Broadcasted environment change." } catch {}

Write-Host "Unregister complete."
