#!/bin/bash

# Kiểm tra đầu vào: Đảm bảo giá trị độ sáng là số và trong khoảng hợp lệ
if [[ "$1" =~ ^[0-9]+$ ]] && [ "$1" -ge 0 ] && [ "$1" -le 100 ]; then
    # Sử dụng brightnessctl để điều chỉnh độ sáng màn hình
    brightnessctl set "$1"%
else
    echo "Error: Invalid brightness value. Please provide a value between 0 and 100."
    exit 1
fi
