# systrayUpdater
Simple Qt based system tray icon to notify of available updates and then update on click

For Arch (based) systems only!

To install and use: Place files in appropriate locations and run appropriate commands when doing so

Uses config file for options.
- Terminal command and option (usually `-e`)
- Timer duration for `checkupdates` to run in backgound
- Option to use `checkupdates -d` to preload new pkgs to cache
	(must complete update before installing new pkgs or suffer partial updates!)
- Custom system tray icon

Includes:
- .desktop file for autostarting
- Pacman hook files to avoid partial updates
- Tray and shortcut icons

TODO
- look into adding option to view news 
