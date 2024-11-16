#!/bin/bash

# Kiểm tra tham số đầu vào
if [ $# -ne 1 ]; then
    echo "Usage: $0 <mode>"
    echo "Available modes: performance, balanced, power-saver"
    exit 1
fi

# Lấy giá trị mode từ tham số đầu vào
mode=$1

# Chuyển đổi mode
case "$mode" in
    performance)
        powerprofilesctl set performance
        ;;
    balanced)
        powerprofilesctl set balanced
        ;;
    power-saver)
        powerprofilesctl set power-saver
        ;;
    *)
        echo "Chế độ không hợp lệ: $mode"
        echo "Vui lòng chọn một trong các chế độ sau: performance, balanced, power-saver"
        exit 1
        ;;
esac