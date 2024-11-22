#!/bin/bash

BLANK_TIME=$1
gsettings set org.gnome.desktop.session idle-delay "$BLANK_TIME"
