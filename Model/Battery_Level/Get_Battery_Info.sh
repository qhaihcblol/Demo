#!/bin/bash

# Lấy thông tin thiết bị pin
BATTERY=$(upower -e | grep 'battery')

if [ -z "$BATTERY" ]; then
    echo "Không tìm thấy thiết bị pin!"
    exit 1
fi

# Lấy thông tin trạng thái pin
STATUS=$(upower -i "$BATTERY" | grep "state" | awk '{print $2}')
PERCENTAGE=$(upower -i "$BATTERY" | grep "percentage" | awk '{print $2}')
TIME_TO_FULL=$(upower -i "$BATTERY" | grep "time to full" | awk '{print $4, $5}')
TIME_TO_EMPTY=$(upower -i "$BATTERY" | grep "time to empty" | awk '{print $4, $5}')

echo "$STATUS"
echo "$PERCENTAGE"

case $STATUS in
    "charging")
        echo "Time to full:"
        if [ -z "$TIME_TO_FULL" ]; then
            echo "Calculating..."
        else
            echo "$TIME_TO_FULL"
        fi
        ;;
    "discharging")
        echo "Time to empty:"
        if [ -z "$TIME_TO_EMPTY" ]; then
            echo "Calculating..."
        else
            echo "$TIME_TO_EMPTY"
        fi
        ;;
    "fully-charged")
        echo "Time to empty/full:"
        echo "Fully charged!"
        ;;
    "pending-charge")
        echo "Time to full:"
        echo "......"
        ;;
    "pending-discharge")
        echo "Time to empty:"
        echo "......"
        ;;
    *)
        echo "Trạng thái pin không xác định."
        ;;
esac
