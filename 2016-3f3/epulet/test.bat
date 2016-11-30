@echo off
for %%f in (*.*) do (
	if "%%~xf" == ".txt" (
		type %%f
		echo : 
		py epulet.py < %%f))