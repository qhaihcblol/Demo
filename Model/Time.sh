#!/bin/bash

# Lấy thông tin thiết bị pin
BATTERY=$(upower -e | grep 'battery')

if [ -z "$BATTERY" ]; then
    echo "Không tìm thấy thiết bị pin!"
    exit 1
fi

# Lấy thông tin trạng thái pin
STATUS=$(upower -i "$BATTERY" | grep "state" | awk '{print $2}')
TIME_TO_FULL=$(upower -i "$BATTERY" | grep "time to full" | awk '{print $4, $5}')
TIME_TO_EMPTY=$(upower -i "$BATTERY" | grep "time to empty" | awk '{print $4, $5}')

# Kiểm tra trạng thái pin
if [ "$STATUS" == "charging" ]; then
    if [ -z "$TIME_TO_FULL" ]; then
        echo "Pin đang sạc nhưng không thể xác định thời gian sạc đầy."
    else
        echo "Pin đang sạc. Thời gian còn lại để sạc đầy: $TIME_TO_FULL"
    fi
elif [ "$STATUS" == "discharging" ]; then
    if [ -z "$TIME_TO_EMPTY" ]; then
        echo "Pin đang sử dụng nhưng không thể xác định thời gian còn lại."
    else
        echo "Pin đang sử dụng. Thời gian còn lại: $TIME_TO_EMPTY"
    fi
else
    echo "Pin đang ở trạng thái: $STATUS"
fi
