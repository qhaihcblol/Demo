#!/bin/bash

# Script kiểm tra trạng thái Automatic Suspend Plugged In

# Đọc trạng thái của khóa
status=$(gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type)

echo $status
