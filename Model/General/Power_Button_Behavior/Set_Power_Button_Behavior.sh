#!/bin/bash

# Kiểm tra tham số đầu vào
if [ $# -ne 1 ]; then
    echo "Usage: $0 <behavior>"
    echo "Available behaviors: suspend, shutdown, nothing, interactive"
    exit 1
fi

BEHAVIOR=$1

# Danh sách các giá trị hợp lệ
VALID_BEHAVIORS=("suspend" "shutdown" "nothing" "interactive")

# Kiểm tra xem giá trị đầu vào có hợp lệ không
VALID=false
for valid_behavior in "${VALID_BEHAVIORS[@]}"; do
    if [ "$valid_behavior" == "$BEHAVIOR" ]; then
        VALID=true
        break
    fi
done

if [ "$VALID" == "false" ]; then
    echo "Invalid behavior: $BEHAVIOR"
    echo "Available behaviors: suspend, hibernate, nothing, interactive"
    exit 2
fi

# Thay đổi cài đặt thông qua gsettings
gsettings set org.gnome.settings-daemon.plugins.power power-button-action "$BEHAVIOR"

if [ $? -eq 0 ]; then
    echo "Power button behavior set to '$BEHAVIOR' successfully."
else
    echo "Failed to set power button behavior."
    exit 3
fi
