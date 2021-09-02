#!/usr/bin/env python

"""
Current status is; it runs, it will initially get
number of updates, it will open new terminal window
and complete update (keeping the window open?),
IT DOES NOT UPDATE THE COUNT.
"""

# Get needed modules
import yaml
import subprocess
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Available Updates count holder
avail = ""

# Use config.yml file to allow for compatibility with
# most terminal emulators possible & custom icon
with open('config.yml') as f:
    conf = yaml.load(f, yaml.FullLoader)
    term = str(conf['terminal'])
    opt = str(conf['option'])
    icn = str(conf['icon'])
    f.close()

# Run checkupdates command
# Populates the available updates count holder
def count():
    cmd = ['checkupdates']
    p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['wc', '-l'], stdin=p1.stdout, stdout=subprocess.PIPE)
    output = ((p2.communicate()[0]).decode()).rstrip('\n')
    Nupd = []
    digit = str(output)+" Updates"
    Nupd.append(digit)
    global avail
    avail = Nupd[-1]

# Run system update
def update():
    cmd = [ term, opt, 'sudo', 'pacman', '-Syu']
    subprocess.Popen(cmd)

# Initially populate available updates count
count()

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Set up timer to update count
timer = QTimer()
timer.timeout.connect(count)
timer.start(10000)

# Adding an icon
icon = QIcon(icn)

# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setToolTip(avail)
tray.setVisible(True)

# Creating the options
menu = QMenu()
option1 = QAction(avail)
option1.triggered.connect(update)
menu.addAction(option1)

# To quit the app
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Adding options to the System Tray
tray.setContextMenu(menu)

app.exec_()
