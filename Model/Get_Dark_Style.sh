#!/bin/bash

# Lấy tên chủ đề GTK hiện tại
current_theme=$(gsettings get org.gnome.desktop.interface gtk-theme)
echo "$current_theme"
# Kiểm tra nếu là Dark Style
if [[ "$current_theme" == *"dark"* ]]; then
    echo "dark"
else
    echo "light"
fi
