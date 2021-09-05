#!/bin/bash

RED='\033[0;31m'
LUPDATE="$(grep 'pacman -Syu' /var/log/pacman.log | tail -1| awk -F'[][]' '{print $2}')"
MODPKGS="$(find /var/cache/pacman/pkg -type f -newermt $LUPDATE)"

if [[ -n $MODPKGS ]]; then
  echo
  echo -e "\a"
  echo -e "                  ${RED}[WARNING]${NC}"
  echo -e "  ${RED}There are newer package files in the cache${NC}"
  echo -e "      ${RED}Sending error signals and aborting${NC}"
  echo
  echo -e "   ${RED}Please run full update before continuing${NC}"
  echo
  exit 1
elif [[ -z $MODPKGS ]]; then
  exit 0
else
  echo "    Error?"
  exit 1
fi
