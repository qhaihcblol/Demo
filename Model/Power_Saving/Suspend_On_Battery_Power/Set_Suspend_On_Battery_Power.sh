#!/bin/bash

# Script thiết lập trạng thái Automatic Suspend On Battery Power

if [[ $1 == "True" ]]; then
    gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'suspend'
elif [[ $1 == "False" ]]; then
    gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type 'nothing'
else
    echo "Invalid parameter. Use 'True' or 'False'."
fi
