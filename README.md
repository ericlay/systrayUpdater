# systrayUpdater
PyQt5 system tray applet to notify of available updates.

For Arch (based) systems only!

Right click to access menu actions:
- Run update
- Read the News
- Display list of packages with updates available (click to search arch website for highlighted package)

To install:
```
git clone https://github.com/ericlay/systrayUpdater.git
cd systrayUpdater
makepkg -sric
```

Uses config file for options: `/etc/systrayupdater/config.yml`
- Terminal command and option (usually `-e`)
- Timer duration for `checkupdates` to run in backgound
- Custom system tray icon
- Override by copying file to `$HOME/systrayupdater/config.yml`

Includes:
- .desktop file for autostarting
- Tray and shortcut icons

