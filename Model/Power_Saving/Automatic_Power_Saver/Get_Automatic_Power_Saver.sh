#!/bin/bash

# Script kiểm tra trạng thái của Automatic Power Saver

# Đọc trạng thái của khóa power-saver-profile-on-low-battery
status=$(gsettings get org.gnome.settings-daemon.plugins.power power-saver-profile-on-low-battery)

echo $status