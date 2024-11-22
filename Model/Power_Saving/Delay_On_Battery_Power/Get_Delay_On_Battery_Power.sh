#!/bin/bash

delay=$(gsettings get org.gnome.settings-daemon.plugins.power sleep-inactive-battery-timeout)
echo "$delay"
