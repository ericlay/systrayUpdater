# systrayUpdater
Simple Qt based system tray icon to notify of available updates and then update on click

Uses config file for options.
- Terminal command and option (usually `-e`)
- Timer duration for `checkupdates` to run in backgound
- Option to use `checkupdates -d` to preload new pkgs to cache
	(must complete update before installing new pkgs or suffer partial upgrades!!)
- Custom system tray icon

TODO
- look into adding option to view news 
