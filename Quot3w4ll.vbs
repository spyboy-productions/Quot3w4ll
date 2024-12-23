Set WshShell = CreateObject("WScript.Shell")
scriptPath = Replace(WScript.ScriptFullName, "Quot3w4ll.vbs", "wall.py")
WshShell.Run "python3 """ & scriptPath & """", 0, False
