#!/bin/bash

# Lấy trạng thái của Night Light
night_light_status=$(gsettings get org.gnome.settings-daemon.plugins.color night-light-enabled)

# Kiểm tra và in kết quả
echo "$night_light_status"