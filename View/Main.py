# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(53, 132, 228);\n"
"}\n"
"QPushButton{\n"
"	color:white;\n"
"	text-align:left;\n"
"	border:none;\n"
"	padding:5px 0px 5px 10px;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#f5fafe;\n"
"	color:#1f95ef;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Logo = QLabel(self.icon_only_widget)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMinimumSize(QSize(50, 50))
        self.Logo.setMaximumSize(QSize(50, 50))
        self.Logo.setPixmap(QPixmap(u":/image/Resource/logo.png"))
        self.Logo.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.Logo)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.Battery_Level_Btn1 = QPushButton(self.icon_only_widget)
        self.Battery_Level_Btn1.setObjectName(u"Battery_Level_Btn1")
        icon = QIcon()
        icon.addFile(u":/image/Resource/battery.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Battery_Level_Btn1.setIcon(icon)
        self.Battery_Level_Btn1.setIconSize(QSize(30, 30))
        self.Battery_Level_Btn1.setCheckable(True)
        self.Battery_Level_Btn1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Battery_Level_Btn1)

        self.Power_Mode_Btn1 = QPushButton(self.icon_only_widget)
        self.Power_Mode_Btn1.setObjectName(u"Power_Mode_Btn1")
        icon1 = QIcon()
        icon1.addFile(u":/image/Resource/powermode.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Power_Mode_Btn1.setIcon(icon1)
        self.Power_Mode_Btn1.setIconSize(QSize(30, 30))
        self.Power_Mode_Btn1.setCheckable(True)
        self.Power_Mode_Btn1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Power_Mode_Btn1)

        self.Brightness_Btn1 = QPushButton(self.icon_only_widget)
        self.Brightness_Btn1.setObjectName(u"Brightness_Btn1")
        icon2 = QIcon()
        icon2.addFile(u":/image/Resource/brightness.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Brightness_Btn1.setIcon(icon2)
        self.Brightness_Btn1.setIconSize(QSize(30, 30))
        self.Brightness_Btn1.setCheckable(True)
        self.Brightness_Btn1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Brightness_Btn1)

        self.Power_Saving_Btn1 = QPushButton(self.icon_only_widget)
        self.Power_Saving_Btn1.setObjectName(u"Power_Saving_Btn1")
        icon3 = QIcon()
        icon3.addFile(u":/image/Resource/powersaving.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Power_Saving_Btn1.setIcon(icon3)
        self.Power_Saving_Btn1.setIconSize(QSize(30, 30))
        self.Power_Saving_Btn1.setCheckable(True)
        self.Power_Saving_Btn1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Power_Saving_Btn1)

        self.General_Btn1 = QPushButton(self.icon_only_widget)
        self.General_Btn1.setObjectName(u"General_Btn1")
        icon4 = QIcon()
        icon4.addFile(u":/image/Resource/general.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.General_Btn1.setIcon(icon4)
        self.General_Btn1.setIconSize(QSize(30, 30))
        self.General_Btn1.setCheckable(True)
        self.General_Btn1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.General_Btn1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 113, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.Sign_Out_Btn1 = QPushButton(self.icon_only_widget)
        self.Sign_Out_Btn1.setObjectName(u"Sign_Out_Btn1")
        icon5 = QIcon()
        icon5.addFile(u":/image/Resource/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Sign_Out_Btn1.setIcon(icon5)
        self.Sign_Out_Btn1.setIconSize(QSize(30, 30))
        self.Sign_Out_Btn1.setCheckable(True)
        self.Sign_Out_Btn1.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.Sign_Out_Btn1)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(53, 132, 228);\n"
"	color:white;\n"
"}\n"
"QPushButton{\n"
"	color:white;\n"
"	text-align:left;\n"
"	border:none;\n"
"	padding:5px 0px 5px 10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"	font:14px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#f5fafe;\n"
"	color:#1f95ef;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.Logo_Label = QLabel(self.icon_name_widget)
        self.Logo_Label.setObjectName(u"Logo_Label")
        self.Logo_Label.setMinimumSize(QSize(50, 50))
        self.Logo_Label.setMaximumSize(QSize(50, 50))
        self.Logo_Label.setPixmap(QPixmap(u":/image/Resource/logo.png"))
        self.Logo_Label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.Logo_Label)

        self.SideBar_Label = QLabel(self.icon_name_widget)
        self.SideBar_Label.setObjectName(u"SideBar_Label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.SideBar_Label.setFont(font)

        self.horizontalLayout_2.addWidget(self.SideBar_Label)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.Battery_Level_Btn2 = QPushButton(self.icon_name_widget)
        self.Battery_Level_Btn2.setObjectName(u"Battery_Level_Btn2")
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        self.Battery_Level_Btn2.setFont(font1)
        self.Battery_Level_Btn2.setIcon(icon)
        self.Battery_Level_Btn2.setIconSize(QSize(30, 30))
        self.Battery_Level_Btn2.setCheckable(True)
        self.Battery_Level_Btn2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Battery_Level_Btn2)

        self.Power_Mode_Btn2 = QPushButton(self.icon_name_widget)
        self.Power_Mode_Btn2.setObjectName(u"Power_Mode_Btn2")
        self.Power_Mode_Btn2.setFont(font1)
        self.Power_Mode_Btn2.setIcon(icon1)
        self.Power_Mode_Btn2.setIconSize(QSize(30, 30))
        self.Power_Mode_Btn2.setCheckable(True)
        self.Power_Mode_Btn2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Power_Mode_Btn2)

        self.Brightness_Btn2 = QPushButton(self.icon_name_widget)
        self.Brightness_Btn2.setObjectName(u"Brightness_Btn2")
        self.Brightness_Btn2.setFont(font1)
        self.Brightness_Btn2.setIcon(icon2)
        self.Brightness_Btn2.setIconSize(QSize(30, 30))
        self.Brightness_Btn2.setCheckable(True)
        self.Brightness_Btn2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Brightness_Btn2)

        self.Power_Saving_Btn2 = QPushButton(self.icon_name_widget)
        self.Power_Saving_Btn2.setObjectName(u"Power_Saving_Btn2")
        self.Power_Saving_Btn2.setFont(font1)
        self.Power_Saving_Btn2.setIcon(icon3)
        self.Power_Saving_Btn2.setIconSize(QSize(30, 30))
        self.Power_Saving_Btn2.setCheckable(True)
        self.Power_Saving_Btn2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Power_Saving_Btn2)

        self.General_Btn2 = QPushButton(self.icon_name_widget)
        self.General_Btn2.setObjectName(u"General_Btn2")
        self.General_Btn2.setFont(font1)
        self.General_Btn2.setIcon(icon4)
        self.General_Btn2.setIconSize(QSize(30, 30))
        self.General_Btn2.setCheckable(True)
        self.General_Btn2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.General_Btn2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 113, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.Sign_Out_Btn2 = QPushButton(self.icon_name_widget)
        self.Sign_Out_Btn2.setObjectName(u"Sign_Out_Btn2")
        self.Sign_Out_Btn2.setFont(font1)
        self.Sign_Out_Btn2.setIcon(icon5)
        self.Sign_Out_Btn2.setIconSize(QSize(30, 30))
        self.Sign_Out_Btn2.setCheckable(True)
        self.Sign_Out_Btn2.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.Sign_Out_Btn2)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu_widget = QWidget(self.centralwidget)
        self.main_menu_widget.setObjectName(u"main_menu_widget")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.main_menu_widget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Menu_Btn = QPushButton(self.header_widget)
        self.Menu_Btn.setObjectName(u"Menu_Btn")
        self.Menu_Btn.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u":/image/Resource/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Menu_Btn.setIcon(icon6)
        self.Menu_Btn.setIconSize(QSize(20, 20))
        self.Menu_Btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.Menu_Btn)

        self.horizontalSpacer_2 = QSpacerItem(149, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_14 = QPushButton(self.header_widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        icon7 = QIcon()
        icon7.addFile(u"Resource/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_14.setIcon(icon7)
        self.pushButton_14.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton_14)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(149, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.Info_Btn = QPushButton(self.header_widget)
        self.Info_Btn.setObjectName(u"Info_Btn")
        self.Info_Btn.setStyleSheet(u"border:none;")
        icon8 = QIcon()
        icon8.addFile(u":/image/Resource/image.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Info_Btn.setIcon(icon8)
        self.Info_Btn.setIconSize(QSize(20, 20))
        self.Info_Btn.setCheckable(False)
        self.Info_Btn.setAutoExclusive(False)

        self.horizontalLayout_4.addWidget(self.Info_Btn)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.Stacked_Widget = QStackedWidget(self.main_menu_widget)
        self.Stacked_Widget.setObjectName(u"Stacked_Widget")
        self.Stacked_Widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.Stacked_Widget)


        self.gridLayout.addWidget(self.main_menu_widget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Menu_Btn.toggled.connect(self.icon_only_widget.setHidden)
        self.Menu_Btn.toggled.connect(self.icon_name_widget.setVisible)
        self.General_Btn1.toggled.connect(self.General_Btn2.setChecked)
        self.Power_Saving_Btn1.toggled.connect(self.Power_Saving_Btn2.setChecked)
        self.Brightness_Btn1.toggled.connect(self.Brightness_Btn2.setChecked)
        self.Power_Mode_Btn1.toggled.connect(self.Power_Mode_Btn2.setChecked)
        self.Power_Mode_Btn2.toggled.connect(self.Power_Mode_Btn1.setChecked)
        self.Brightness_Btn2.toggled.connect(self.Brightness_Btn1.setChecked)
        self.Power_Saving_Btn2.toggled.connect(self.Power_Saving_Btn1.setChecked)
        self.General_Btn2.toggled.connect(self.General_Btn1.setChecked)
        self.Sign_Out_Btn1.toggled.connect(MainWindow.close)
        self.Sign_Out_Btn2.toggled.connect(MainWindow.close)
        self.Battery_Level_Btn1.toggled.connect(self.Battery_Level_Btn2.setChecked)
        self.Battery_Level_Btn2.toggled.connect(self.Battery_Level_Btn1.setChecked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Logo.setText("")
        self.Battery_Level_Btn1.setText("")
        self.Power_Mode_Btn1.setText("")
        self.Brightness_Btn1.setText("")
        self.Power_Saving_Btn1.setText("")
        self.General_Btn1.setText("")
        self.Sign_Out_Btn1.setText("")
        self.Logo_Label.setText("")
        self.SideBar_Label.setText(QCoreApplication.translate("MainWindow", u"Power Management", None))
        self.Battery_Level_Btn2.setText(QCoreApplication.translate("MainWindow", u"Battery Level", None))
        self.Power_Mode_Btn2.setText(QCoreApplication.translate("MainWindow", u"Power Mode", None))
        self.Brightness_Btn2.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.Power_Saving_Btn2.setText(QCoreApplication.translate("MainWindow", u"Power Saving", None))
        self.General_Btn2.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.Sign_Out_Btn2.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.Menu_Btn.setText("")
        self.pushButton_14.setText("")
        self.Info_Btn.setText("")
    # retranslateUi

