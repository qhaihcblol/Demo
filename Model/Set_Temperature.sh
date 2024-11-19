#!/bin/bash

# Kiểm tra tham số đầu vào
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <temperature>"
    echo "Temperature value should be between 1700 and 4700."
    exit 1
fi

# Lấy tham số đầu vào (nhiệt độ màu từ 1700 đến 4700)
temperature=$1

# Kiểm tra nếu giá trị đầu vào hợp lệ (giữa 1700 và 4700)
if [[ "$temperature" -lt 1700 || "$temperature" -gt 4700 ]]; then
    echo "Invalid temperature value. Please enter a value between 1700 and 4700."
    exit 1
fi

# Cập nhật nhiệt độ màu của Night Light
gsettings set org.gnome.settings-daemon.plugins.color night-light-temperature "$temperature"
