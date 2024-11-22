#!/bin/bash

# Kiểm tra tham số đầu vào
if [ "$#" -ne 1 ]; then
    echo "Sử dụng: $0 [on|off]"
    exit 1
fi

# Lấy tham số đầu vào
ACTION=$1

# Bật hoặc tắt dim screen dựa vào tham số đầu vào
if [ "$ACTION" == "True" ]; then
    gsettings set org.gnome.settings-daemon.plugins.power idle-dim true
elif [ "$ACTION" == "False" ]; then
    gsettings set org.gnome.settings-daemon.plugins.power idle-dim false
else
    echo "Tham số không hợp lệ. Vui lòng sử dụng 'True' hoặc 'False'."
    exit 1
fi
