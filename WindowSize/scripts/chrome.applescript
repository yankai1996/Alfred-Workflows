set theApp to "Google Chrome"
set appHeight to 1080
set appWidth to 1180


tell application theApp
	activate
	reopen
	set the bounds of the first window to {0, 0, appWidth, appHeight}
end tell