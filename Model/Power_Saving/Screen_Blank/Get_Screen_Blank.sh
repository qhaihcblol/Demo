#!/bin/bash

# Lấy thời gian screen blank (idle-delay)
BLANK_TIME=$(gsettings get org.gnome.desktop.session idle-delay | awk '{print $2}')
echo "$BLANK_TIME"
