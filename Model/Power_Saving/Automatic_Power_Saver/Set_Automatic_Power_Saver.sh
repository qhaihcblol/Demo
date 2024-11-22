#!/bin/bash

# Script bật/tắt chức năng Automatic Power Saver

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 [on|off]"
    exit 1
fi

mode=$1

if [[ $mode == "True" ]]; then
    gsettings set org.gnome.settings-daemon.plugins.power power-saver-profile-on-low-battery true
elif [[ $mode == "False" ]]; then
    gsettings set org.gnome.settings-daemon.plugins.power power-saver-profile-on-low-battery false
else
    echo "Invalid argument: $mode"
    echo "Usage: $0 [on|off]"
    exit 1
fi
