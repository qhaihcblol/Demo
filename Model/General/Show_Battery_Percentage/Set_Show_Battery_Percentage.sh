#!/bin/bash
Mode=$1

gsettings set org.gnome.desktop.interface show-battery-percentage "$Mode"
