#!/bin/bash

# Script kiểm tra trạng thái Automatic Suspend On Battery Power

# Đọc trạng thái của khóa
status=$(gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type)

echo $status