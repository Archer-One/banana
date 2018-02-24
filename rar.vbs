set fso=createobject("scripting.filesystemobject") 
set ws=createobject("wscript.shell")
path=ws.regread("HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\WinRAR.exe\path")
path=fso.getfile(path&"\rar.exe").shortpath
name="C:\xx\"
ws.run path&" a "&date()&" "&name,0