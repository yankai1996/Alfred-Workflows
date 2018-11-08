-- NSAppleScript

on alfred_script(q)
	tell application "iTerm"
		activate
		set startup_file to (q & "/bin/startup.sh")
		if (count of windows) is 0 then
			create window with default profile
		end if
		select first window
    		tell the first window
      		tell current session to write text (startup_file)
			set webapps to (quoted form of (q & "/webapps/"))
			tell current session to write text ("open -a Finder " & webapps)
		end tell	
	end tell
end alfred_script