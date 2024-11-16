#!/bin/bash

# Chuyển đổi các file UI thành file Python tương ứng
pyside6-rcc res.qrc >res_rc.py

pyside6-uic main_form.ui >View/Main.py
pyside6-uic battery_level_form.ui >View/Battery_Level.py
pyside6-uic brightness_form.ui >View/Brightness.py
pyside6-uic info_form.ui >View/Info.py
pyside6-uic power_mode_form.ui >View/Power_Mode.py
pyside6-uic display_mode_form.ui >View/Display_Mode.py
pyside6-uic power_saving_form.ui >View/Power_Saving.py