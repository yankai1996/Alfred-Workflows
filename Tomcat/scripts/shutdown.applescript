-- NSAppleScript

on alfred_script(q)
	tell application "iTerm"
		activate
		set shutdown to q & "/bin/shutdown.sh"
		if (count of windows) is 0 then
			create window with default profile
		end if
		select first window
    		tell the first window
      		tell current session to write text (quoted form of shutdown)
		end tell
	end tell
end alfred_script