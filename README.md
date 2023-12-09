# systrayUpdater 󱉛
PyQt5 system tray applet notifier of available updates.

For Arch (based) systems only!

Right click to access menu actions:
- Run update
- Read the News
- Display list of packages with updates available 
    - (click to find package on Arch linux Package Search website)

To install:
```
git clone https://github.com/ericlay/systrayUpdater.git
cd systrayUpdater
makepkg -sric
```

Post install:
It is suggested to copy `/etc/systrayupdater` to `$HOME/.config/systrayupdater`

Uses config file for options: `/etc/systrayupdater/config.yml`
- Terminal command (set to `$TERM` by default)
- Set terminal option (usually `-e`)
- Timer duration for `checkupdates` to run in backgound
- Custom system tray icon
- Defaults to `$HOME/systrayupdater/config.yml` if found

Includes:
- .desktop file for autostarting
- Tray and shortcut icons

