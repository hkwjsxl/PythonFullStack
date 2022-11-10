# Requires -RunAsAdministrator
$PROGRAM_NAME = 'UnblockNeteaseMusic'
# $AUTHOR_NAME = '1715173329'
$PROJECT_NAME = 'UnblockNeteaseMusic'
$REPO_NAME = 'server'
$BRANCH_NAME = 'enhanced'

$INSTALLATION_PATH = "$env:APPDATA\$PROGRAM_NAME"
$BIN_PATH = "$INSTALLATION_PATH\bin"
$TMP_PATH = "$INSTALLATION_PATH\tmp"
$SCRIPT_PATH = "$INSTALLATION_PATH\script"

$OS_BIT = if ([System.Environment]::Is64BitOperatingSystem) { 'x64' } else { 'x86' }
$NODE_VERSION = if ([System.Environment]::OSVersion.Version.Major -gt 6) { 'v16.13.0' } else { 'v12.22.7' }
$NODE_NAME = "node-$NODE_VERSION-win-$OS_BIT"
$NODE_URI = "https://npm.taobao.org/mirrors/node/$NODE_VERSION/$NODE_NAME.zip"
$NODE_SAVE_PATH = "$TMP_PATH\$NODE_NAME.zip"
$NODE_EXEC_PATH = "$BIN_PATH\$NODE_NAME\node.exe"

# https://github.com/UnblockNeteaseMusic/server.git
# https://github.com/UnblockNeteaseMusic/server/archive/refs/heads/enhanced.zip
# $UNBLOCKNETEASEMUSIC_URI = "https://github.com/nondanee/$PROGRAM_NAME/archive/master.zip"
# $UNBLOCKNETEASEMUSIC_COMMIT_URI = "https://api.github.com/repos/nondanee/$PROGRAM_NAME/commits/master"
# https://ghproxy.com/https://github.com/1715173329/UnblockNeteaseMusic/archive/refs/heads/enhanced.zip
$UNBLOCKNETEASEMUSIC_URI = "https://ghproxy.com/https://github.com/$PROJECT_NAME/$REPO_NAME/archive/$BRANCH_NAME.zip"
$UNBLOCKNETEASEMUSIC_COMMIT_URI = "https://api.github.com/repos/$PROJECT_NAME/$REPO_NAME/commits/$BRANCH_NAME"
$UNBLOCKNETEASEMUSIC_SAVE_PATH = "$TMP_PATH\$PROGRAM_NAME.zip"
$UNBLOCKNETEASEMUSIC_VERSION_PATH = "$TMP_PATH\$PROGRAM_NAME.version"
$UNBLOCKNETEASEMUSIC_RUN_COMMAND_PATH = "$TMP_PATH\$PROGRAM_NAME.run"
$UNBLOCKNETEASEMUSIC_EXEC_PATH = "$BIN_PATH\$REPO_NAME-$BRANCH_NAME"
$UNBLOCKNETEASEMUSIC_EXEC_FILE = "$UNBLOCKNETEASEMUSIC_EXEC_PATH\app.js"
$UNBLOCKNETEASEMUSIC_CERTIFICATE_AUTHORITY_FILE = "$UNBLOCKNETEASEMUSIC_EXEC_PATH\ca.crt"
$UNBLOCKNETEASEMUSIC_CERTIFICATE_AUTHORITY_NAME = "$PROGRAM_NAME Root CA"

$WORKING_DIRECTORY = "$UNBLOCKNETEASEMUSIC_EXEC_PATH"
# $DEFAULT_ARGUMENT = 'app.js -p 6666:6667 -s -e http://music.163.com -f 59.111.19.33'
$DEFAULT_ARGUMENT = 'app.js -p 6666:6667 -e http://music.163.com'
$global:EXEC_ARGUMENTS = "$DEFAULT_ARGUMENT"

$AUTO_BOOT_PS_SCRIPT = "$SCRIPT_PATH\$PROGRAM_NAME.ps1"
$AUTO_BOOT_VB_SCRIPT = "$SCRIPT_PATH\$PROGRAM_NAME.vbs"
$AUTO_BOOT_SHORTCUT = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\$PROGRAM_NAME.lnk"

[System.Net.ServicePointManager]::SecurityProtocol = "tls12, tls11, tls"

function ShowMenu () {
    ClsWorkaround
    WriteLine
    @"
     网易云解锁安装脚本
            V0.07 2022.10.21
            SINCE 2019.09.10
                AUTHOR @LOGI
----------------------------
0. 退出
1. 安装
2. 卸载
3. 运行
4. 停止
5. 更新
6. 自定义音源
7. 局域网共享
8. 添加开机自启
9. 取消开机自启
"@
    WriteLine
    switch (Read-Host '请选择') {
        0 { exit 0 }
        1 { InstallUnblockNeteaseMusic }
        2 { UninstallUnblockNeteaseMusic }
        3 { StartUnblockNeteaseMusic }
        4 { StopUnblockNeteaseMusic }
        5 { UpdateUnblockNeteaseMusic }
        6 { CustomizeSourceOrder }
        7 { ShowLocalAreaNetworkConfig }
        8 { EnableUnblockNeteaseMusicAutoBoot }
        9 { DisableUnblockNeteaseMusicAutoBoot }
        Default { ShowMenu }
    }
}

function DateWorkaround($DateObject) {
    if ($PSVersionTable.PSVersion.Major -gt 5) {
        Get-Date -Format u -Date $DateObject.ToLocalTime()
    }
    else {
        Get-Date -Format u -Date "$DateObject"
    }
}

function ClsWorkaround {
    if ($PSVersionTable.PSVersion.Major -gt 5) {
        # https://github.com/microsoft/terminal/issues/9018
        # https://superuser.com/questions/1628694/how-do-i-add-a-keyboard-shortcut-to-clear-scrollback-buffer-in-windows-terminal
        # "$([char]27)[2J$([char]27)[3J$([char]27)[2H"
        # Write-Host -NoNewline "`e[2J`e[3J`e[H"
        Write-Host -NoNewline "`e[H"
        # try {
        # https://stackoverflow.com/questions/58542227/set-console-top-most-in-powershell
        # $Null = [System.Console]::SetWindowPosition(0, [System.Console]::CursorTop)
        #             $signature = @'
        # [DllImport("kernel32.dll")] public static extern IntPtr GetConsoleWindow();
        # [DllImport("user32.dll")]
        # public static extern bool SetWindowPos(
        #     IntPtr hWnd,
        #     IntPtr hWndInsertAfter,
        #     int X,
        #     int Y,
        #     int cx,
        #     int cy,
        #     uint uFlags);
        # '@
        #             $type = Add-Type -MemberDefinition $signature -Name SetWindowPosition -Namespace SetWindowPos -Using System.Text -PassThru
        #             $handle = $type::GetConsoleWindow()
        #             $Null = $type::SetWindowPos($handle, -1, 0, 0, 0, 0, 0x0003)
        # }
        # catch {}
    }
    Clear-Host
}

function Test-Administrator {
    $User = [Security.Principal.WindowsIdentity]::GetCurrent()
    return (New-Object Security.Principal.WindowsPrincipal $User).IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
}

function WriteLine() {
    Write-Host -Object '----------------------------'
}

function NewPath($Path) {
    if (!(Test-Path "$Path")) {
        $Null = New-Item -ItemType Directory -Path "$Path" -Force
    }
}

function RemovePath($Path) {
    if (Test-Path -Path "$Path") {
        if ((Get-Item "$Path") -is [System.IO.DirectoryInfo]) {
            try {
                Get-ChildItem -Path "$Path" -File -Recurse | Remove-Item -Force
                Get-ChildItem -Path "$Path" -Directory -Recurse | Remove-Item -Recurse -Force
                Remove-Item "$Path" -Force
            }
            catch {
                cmd /c rd /s /q "$Path"
            }
        }
        else {
            Remove-Item "$Path" -Force
        }
    }
}

function ReleaseZip($ZipFile, $TargetFolder) {
    try {
        Expand-Archive -Path "$ZipFile" -DestinationPath "$TargetFolder" -Force:$True
    }
    catch {
        NewPath "$TargetFolder"
        $ShellApp = New-Object -ComObject Shell.Application
        $Files = $ShellApp.NameSpace($ZipFile).Items()
        $ShellApp.NameSpace($TargetFolder).CopyHere($Files, 16)
    }
}

function CreateShortcut($SourceExe, $ArgumentsToSourceExe, $DestinationPath) {
    $WshShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut($DestinationPath)
    $Shortcut.TargetPath = $SourceExe
    if ($Null -ne "$ArgumentsToSourceExe") {
        $Shortcut.Arguments = "$ArgumentsToSourceExe"
    }
    $Shortcut.Save()
}

function CheckInstallationStatus() {
    if (Test-Path -Path "$NODE_EXEC_PATH") {
        if (Test-Path -Path "$UNBLOCKNETEASEMUSIC_EXEC_FILE") {
            return $True
        }
    }
    return $False
}

function ReadRunConfigCommand() {
    if (Test-Path -Path "$UNBLOCKNETEASEMUSIC_RUN_COMMAND_PATH") {
        $Command = Get-Content -Path "$UNBLOCKNETEASEMUSIC_RUN_COMMAND_PATH"
        if ($Command.StartsWith("$DEFAULT_ARGUMENT")) {
            $global:EXEC_ARGUMENTS = "$Command"
        }
    }
}

function SaveRunConfigCommand($Command) {
    "$Command" | Out-File -Encoding ascii -FilePath "$UNBLOCKNETEASEMUSIC_RUN_COMMAND_PATH"
}

function InstallCertificateAuthority {
    try {
        $Null = cmd /c certutil -addstore Root "$UNBLOCKNETEASEMUSIC_CERTIFICATE_AUTHORITY_FILE"
    }
    catch {
        return
    }
    "Root CA 已加载"
}

function UninstallCertificateAuthority {
    try {
        $Null = cmd /c certutil -delstore Root "$UNBLOCKNETEASEMUSIC_CERTIFICATE_AUTHORITY_NAME"
    }
    catch {
        return
    }
    "Root CA 已删除"
}

function InstallUnblockNeteaseMusic ($Update) {
    if (!($Update) -and (CheckInstallationStatus)) {
        "$PROGRAM_NAME 已经安装"
        return
    }

    NewPath "$INSTALLATION_PATH"
    NewPath "$TMP_PATH"
    NewPath "$BIN_PATH"

    if (!(Test-Path -Path "$NODE_EXEC_PATH")) {
        "正在下载 $NODE_NAME"
        try {
            # https://github.com/PowerShell/PowerShell/issues/14348
            Invoke-WebRequest -UseBasicParsing -Uri "$NODE_URI" -OutFile "$NODE_SAVE_PATH"
        }
        catch {
            '网络故障，请尝试使用代理'
            return
        }
        "正在解压 $NODE_NAME"
        ReleaseZip "$NODE_SAVE_PATH" "$BIN_PATH"
    }

    "正在下载 $PROGRAM_NAME"
    try {
        Invoke-WebRequest -UseBasicParsing -Uri "$UNBLOCKNETEASEMUSIC_URI" -OutFile "$UNBLOCKNETEASEMUSIC_SAVE_PATH"
    }
    catch {
        '网络故障，请尝试使用代理'
        return
    }

    "正在解压 $PROGRAM_NAME"
    RemovePath "$UNBLOCKNETEASEMUSIC_EXEC_PATH"
    ReleaseZip "$UNBLOCKNETEASEMUSIC_SAVE_PATH" "$BIN_PATH"

    InstallCertificateAuthority

    $StartMessage = (StartUnblockNeteaseMusic) + "`n" + (EnableUnblockNeteaseMusicAutoBoot)
    if ($Update) {
        "$PROGRAM_NAME 更新完成"
    }
    else {
        $Null = IsLastestVersion
        "$PROGRAM_NAME 安装完成"
        "$StartMessage"
    }
}

function UninstallUnblockNeteaseMusic() {
    if (!(CheckInstallationStatus)) {
        "$PROGRAM_NAME 尚未安装"
        return
    }

    StopUnblockNeteaseMusic
    DisableUnblockNeteaseMusicAutoBoot
    RemovePath "$INSTALLATION_PATH"
    UninstallCertificateAuthority
    "$PROGRAM_NAME 卸载完成"
}

function StartUnblockNeteaseMusic() {
    if (!(CheckInstallationStatus)) {
        InstallUnblockNeteaseMusic
    }

    ReadRunConfigCommand
    $Null = StopUnblockNeteaseMusic
    Start-Process -WorkingDirectory "$WORKING_DIRECTORY" -FilePath "$NODE_EXEC_PATH" -WindowStyle Hidden -ArgumentList "$global:EXEC_ARGUMENTS"
    Start-Sleep -Seconds 2

    Get-Process -Name *node* | ForEach-Object {
        if ($_.Path -eq "$NODE_EXEC_PATH") {
            $global:IS_NOT_RUNNING = $False
            "$PROGRAM_NAME 启动成功"
        }
    }
    if ($IS_NOT_RUNNING) {
        "$PROGRAM_NAME 启动失败"
    }
}

function StopUnblockNeteaseMusic() {
    if (!(CheckInstallationStatus)) {
        "$PROGRAM_NAME 尚未安装"
        return
    }
    Get-Process -Name *node* | ForEach-Object {
        # if ($_.Path -eq "$NODE_EXEC_PATH") {
        if ($_.Path.StartsWith("$BIN_PATH")) {
            Stop-Process -Id $_.Id
        }
    }
    Start-Sleep -Seconds 1
    "$PROGRAM_NAME 已经停止"
}

function IsLastestVersion () {
    # https://stackoverflow.com/questions/18770723/hide-progress-of-invoke-webrequest
    $OriginalPref = $ProgressPreference
    $ProgressPreference = "SilentlyContinue"
    try {
        $Commit = (Invoke-WebRequest -UseBasicParsing -Uri "$UNBLOCKNETEASEMUSIC_COMMIT_URI").Content
    }
    catch {
        return $False
    }
    finally {
        $ProgressPreference = $OriginalPref
    }

    try {
        $CommitData = "$Commit" | ConvertFrom-Json
    }
    catch {
        $Null = [System.Reflection.Assembly]::LoadWithPartialName("System.Web.Extensions")
        $Serializer = New-Object System.Web.Script.Serialization.JavaScriptSerializer
        $CommitData = $Serializer.DeserializeObject("$Commit")
    }
    $LastestCommitDate = DateWorkaround $CommitData.commit.committer.date
    
    if (Test-Path -Path "$UNBLOCKNETEASEMUSIC_VERSION_PATH") {
        $CurrentCommitDate = Get-Content -Path "$UNBLOCKNETEASEMUSIC_VERSION_PATH"
    }
    else {
        $Null = New-Item -Force -Type File -Path "$UNBLOCKNETEASEMUSIC_VERSION_PATH"
        $CurrentCommitDate = ""
    }

    if ("$LastestCommitDate" -ne "$CurrentCommitDate") {
        "$LastestCommitDate" | Out-File -Encoding ascii -FilePath "$UNBLOCKNETEASEMUSIC_VERSION_PATH"
        return $False
    }
    return $True
}

function UpdateUnblockNeteaseMusic() {
    if (IsLastestVersion) {
        WriteLine
        '已是最新版本'
        return
    }
    if (CheckInstallationStatus) {
        StopUnblockNeteaseMusic
        InstallUnblockNeteaseMusic $True
    }
    else {
        InstallUnblockNeteaseMusic
    }
}

function EnableUnblockNeteaseMusicAutoBoot() {
    if (!(CheckInstallationStatus)) {
        InstallUnblockNeteaseMusic
    }
    NewPath "$SCRIPT_PATH"
    ReadRunConfigCommand
    @"
function IsOnline () {
    `$CheckSites = @(
        'http://163.com',
        'http://qq.com',
        'http://baidu.com'
    )
    foreach (`$site in `$CheckSites) {
        try {
            `$StatusCode = (Invoke-WebRequest -UseBasicParsing -Uri "`$site" -TimeoutSec 1).StatusCode
            if (200 -eq `$StatusCode) {
                return `$True
            }
        }
        catch { }
    }
    return `$False
}`n
while (`$True) {
    if (IsOnline) {
        Start-Process -WorkingDirectory "$WORKING_DIRECTORY" -FilePath "$NODE_EXEC_PATH" -WindowStyle Hidden -ArgumentList "$global:EXEC_ARGUMENTS"
        Exit
    }
    Start-Sleep -Seconds 60
}
"@ | Out-File -FilePath "$AUTO_BOOT_PS_SCRIPT" -Encoding ascii -Force
    @"
CURR_DIR = createobject("Scripting.FileSystemObject").GetFile(Wscript.ScriptFullName).ParentFolder.Path
set WS = createobject("wscript.shell")
WS.currentdirectory = CURR_DIR
WS.Run "cmd /c powershell.exe -command ""& { Set-ExecutionPolicy Remotesigned -Scope Process; .'.\$PROGRAM_NAME.ps1' }""",0
"@ | Out-File -FilePath "$AUTO_BOOT_VB_SCRIPT" -Encoding ascii -Force
    CreateShortcut "$AUTO_BOOT_VB_SCRIPT" $Null "$AUTO_BOOT_SHORTCUT"
    '开机自启设置成功'
}

function DisableUnblockNeteaseMusicAutoBoot() {
    if (!(CheckInstallationStatus)) {
        "$PROGRAM_NAME 尚未安装"
        return
    }
    RemovePath -Path "$AUTO_BOOT_SHORTCUT"
    '开机自启取消成功'
}

function CustomizeSourceOrder() {
    if (!(CheckInstallationStatus)) {
        "$PROGRAM_NAME 尚未安装"
        return
    }
    WriteLine
    '可选音源如下，你可自定义它们的个数和顺序，中间以英文空格隔开：'
    'netease qq baidu kugou kuwo migu joox youtube bilibili pyncmd'
    WriteLine
    $customizedSourceOrder = Read-Host '请输入音源序列'
    if ($customizedSourceOrder.Trim().Length -gt 0) {
        $global:EXEC_ARGUMENTS = "$DEFAULT_ARGUMENT -o $customizedSourceOrder"
        SaveRunConfigCommand "$global:EXEC_ARGUMENTS"
        WriteLine
        '正在重新启动...'
        $Null = StartUnblockNeteaseMusic
        $Null = EnableUnblockNeteaseMusicAutoBoot
    }
    '自定义音源设置完成'
}

function ShowLocalAreaNetworkConfig() {
    if (!(CheckInstallationStatus)) {
        "$PROGRAM_NAME 尚未安装"
        return
    }

    # $ip = [System.Net.DNS]::GetHostByName($Null).AddressList[0].IPAddressToString
    $ip = (Get-NetIPAddress -AddressFamily IPv4 -InterfaceIndex (Get-NetRoute -DestinationPrefix "0.0.0.0/0").ifIndex).IPAddress
    @"
----------------------------
      WIFI 手动代理配置
主机名：$ip
端  口：6666
"@
}

while ($True) {
    if (!(Test-Administrator)) {
        "请以管理员身份运行"
        break
    }

    ShowMenu
    WriteLine
    '请按任意键继续...'
    [void][System.Console]::ReadKey($True)
}
