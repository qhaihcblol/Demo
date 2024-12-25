#!/bin/bash
Option=$1
case $Option in
'poweroff')
    echo "Power off"
    systemctl poweroff

    ;;
'restart')
    echo "Reboot"
    systemctl reboot
    ;;
'suspend')
    echo "Suspend"
    systemctl suspend
    ;;
'logout')
    echo "Logout"
    gnome-session-quit --logout --no-prompt
    ;;
*)
    echo "Invalid Option"
    ;;
esac
