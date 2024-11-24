#!/bin/bash

# Kiểm tra trạng thái tùy chọn "Show Battery Percentage"
status=$(gsettings get org.gnome.desktop.interface show-battery-percentage)

echo "$status"