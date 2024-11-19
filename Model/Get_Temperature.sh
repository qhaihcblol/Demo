#!/bin/bash

# Lấy giá trị độ sáng của Night Light và loại bỏ phần "uint32"
brightness=$(gsettings get org.gnome.settings-daemon.plugins.color night-light-temperature | awk '{print $2}')

# In giá trị độ sáng
echo "$brightness"
