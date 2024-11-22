#!/bin/bash

delay=$1

gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout "$delay"
