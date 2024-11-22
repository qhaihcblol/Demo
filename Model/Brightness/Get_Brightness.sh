#!/bin/bash

# Kiểm tra nếu brightnessctl có sẵn trên hệ thống
if ! command -v brightnessctl &> /dev/null; then
    echo "brightnessctl could not be found, please install it first."
    exit 1
fi

# Lấy giá trị độ sáng hiện tại
brightnessctl get
