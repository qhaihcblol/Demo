#!/bin/bash

# Script thiết lập trạng thái Automatic Suspend Plugged In

if [[ $1 == "True" ]]; then
    gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'suspend'
elif [[ $1 == "False" ]]; then
    gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing'
else
    echo "Invalid parameter. Use 'True' or 'False'."
fi
