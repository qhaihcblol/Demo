#!/bin/bash

# Kiểm tra nếu brightnessctl có sẵn trên hệ thống
if ! command -v brightnessctl &> /dev/null; then
    echo "brightnessctl could not be found, please install it first."
    exit 1
fi

# Lấy giá trị độ sáng từ tham số đầu vào
brightness_value=$1

# Thiết lập độ sáng
brightnessctl -q set "${brightness_value}"
