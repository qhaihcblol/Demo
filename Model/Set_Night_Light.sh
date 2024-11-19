#!/bin/bash

# Kiểm tra tham số đầu vào
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 {on|off}"
    exit 1
fi

# Lấy tham số đầu vào
action=$1

# Bật hoặc tắt Night Light tùy theo tham số đầu vào
if [[ "$action" == "True" ]]; then
    gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled true
elif [[ "$action" == "False" ]]; then
    gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled false
else
    echo "Tham số không hợp lệ. Sử dụng 'true' hoặc 'false'."
    exit 1
fi
