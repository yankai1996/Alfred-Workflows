set theApp to "Preview"
set appHeight to 1080
set appWidth to 900


tell application theApp
	activate
	reopen
	set the bounds of the first window to {0, 0, appWidth, appHeight}
end tell

tell application "System Events"
	tell process "Preview"
		keystroke "2" using command down
	end tell
end tell