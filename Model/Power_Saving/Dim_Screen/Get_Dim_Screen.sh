#!/bin/bash

DIM_STATUS=$(gsettings get org.gnome.settings-daemon.plugins.power idle-dim)

echo "$DIM_STATUS"
