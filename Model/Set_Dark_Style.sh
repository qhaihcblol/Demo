#!/bin/sh
boolDarkTheme=false
if [ "$boolDarkTheme" = true ]; then
    gsettings set org.gnome.desktop.interface gtk-theme 'Yaru-olive-dark'
    gsettings set org.gnome.desktop.interface gtk-color-scheme 'prefer-dark'
else
    gsettings set org.gnome.desktop.interface gtk-theme 'Yaru-olive'
    gsettings set org.gnome.desktop.interface gtk-color-scheme 'default'
fi