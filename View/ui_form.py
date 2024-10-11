# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
"	height:30px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
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
        self.logo1 = QLabel(self.icon_only_widget)
        self.logo1.setObjectName(u"logo1")
        self.logo1.setMinimumSize(QSize(40, 40))
        self.logo1.setMaximumSize(QSize(40, 40))
        self.logo1.setPixmap(QPixmap(u"Resource/profile_pic.png"))
        self.logo1.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.logo1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.Battery_Level_Btn1 = QPushButton(self.icon_only_widget)
        self.Battery_Level_Btn1.setObjectName(u"Battery_Level_Btn1")
        icon = QIcon()
        icon.addFile(u"Resource/dashboard_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u"Resource/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Battery_Level_Btn1.setIcon(icon)
        self.Battery_Level_Btn1.setCheckable(True)
        self.Battery_Level_Btn1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Battery_Level_Btn1)

        self.Power_Mode_Btn1 = QPushButton(self.icon_only_widget)
        self.Power_Mode_Btn1.setObjectName(u"Power_Mode_Btn1")
        icon1 = QIcon()
        icon1.addFile(u"Resource/profile_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u"Resource/profile.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Power_Mode_Btn1.setIcon(icon1)
        self.Power_Mode_Btn1.setCheckable(True)
        self.Power_Mode_Btn1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Power_Mode_Btn1)

        self.Brightness_Btn1 = QPushButton(self.icon_only_widget)
        self.Brightness_Btn1.setObjectName(u"Brightness_Btn1")
        icon2 = QIcon()
        icon2.addFile(u"Resource/messages_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u"Resource/messages.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Brightness_Btn1.setIcon(icon2)
        self.Brightness_Btn1.setCheckable(True)
        self.Brightness_Btn1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Brightness_Btn1)

        self.Display_Mode_Btn1 = QPushButton(self.icon_only_widget)
        self.Display_Mode_Btn1.setObjectName(u"Display_Mode_Btn1")
        icon3 = QIcon()
        icon3.addFile(u"Resource/notifications_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u"Resource/notifications.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Display_Mode_Btn1.setIcon(icon3)
        self.Display_Mode_Btn1.setCheckable(True)
        self.Display_Mode_Btn1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Display_Mode_Btn1)

        self.Power_Saving_Btn1 = QPushButton(self.icon_only_widget)
        self.Power_Saving_Btn1.setObjectName(u"Power_Saving_Btn1")
        icon4 = QIcon()
        icon4.addFile(u"Resource/settings_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u"Resource/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.Power_Saving_Btn1.setIcon(icon4)
        self.Power_Saving_Btn1.setCheckable(True)
        self.Power_Saving_Btn1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.Power_Saving_Btn1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 113, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.Sign_Out_Btn1 = QPushButton(self.icon_only_widget)
        self.Sign_Out_Btn1.setObjectName(u"Sign_Out_Btn1")
        icon5 = QIcon()
        icon5.addFile(u"Resource/log_out_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Sign_Out_Btn1.setIcon(icon5)
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
"	height:30px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
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
        self.Logo_Label.setMinimumSize(QSize(40, 40))
        self.Logo_Label.setMaximumSize(QSize(40, 40))
        self.Logo_Label.setPixmap(QPixmap(u"Resource/profile_pic.png"))
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
        font1.setPointSize(10)
        self.Battery_Level_Btn2.setFont(font1)
        self.Battery_Level_Btn2.setIcon(icon)
        self.Battery_Level_Btn2.setCheckable(True)
        self.Battery_Level_Btn2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Battery_Level_Btn2)

        self.Power_Mode_Btn2 = QPushButton(self.icon_name_widget)
        self.Power_Mode_Btn2.setObjectName(u"Power_Mode_Btn2")
        self.Power_Mode_Btn2.setFont(font1)
        self.Power_Mode_Btn2.setIcon(icon1)
        self.Power_Mode_Btn2.setCheckable(True)
        self.Power_Mode_Btn2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Power_Mode_Btn2)

        self.Brightness_Btn2 = QPushButton(self.icon_name_widget)
        self.Brightness_Btn2.setObjectName(u"Brightness_Btn2")
        self.Brightness_Btn2.setFont(font1)
        self.Brightness_Btn2.setIcon(icon2)
        self.Brightness_Btn2.setCheckable(True)
        self.Brightness_Btn2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Brightness_Btn2)

        self.Display_Mode_Btn2 = QPushButton(self.icon_name_widget)
        self.Display_Mode_Btn2.setObjectName(u"Display_Mode_Btn2")
        self.Display_Mode_Btn2.setFont(font1)
        self.Display_Mode_Btn2.setIcon(icon3)
        self.Display_Mode_Btn2.setCheckable(True)
        self.Display_Mode_Btn2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Display_Mode_Btn2)

        self.Power_Saving_Btn2 = QPushButton(self.icon_name_widget)
        self.Power_Saving_Btn2.setObjectName(u"Power_Saving_Btn2")
        self.Power_Saving_Btn2.setFont(font1)
        self.Power_Saving_Btn2.setIcon(icon4)
        self.Power_Saving_Btn2.setCheckable(True)
        self.Power_Saving_Btn2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Power_Saving_Btn2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 113, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.Sign_Out_Btn2 = QPushButton(self.icon_name_widget)
        self.Sign_Out_Btn2.setObjectName(u"Sign_Out_Btn2")
        self.Sign_Out_Btn2.setFont(font1)
        self.Sign_Out_Btn2.setIcon(icon5)
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
        self.Button_Menu = QPushButton(self.header_widget)
        self.Button_Menu.setObjectName(u"Button_Menu")
        self.Button_Menu.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u"Resource/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Button_Menu.setIcon(icon6)
        self.Button_Menu.setIconSize(QSize(20, 20))
        self.Button_Menu.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.Button_Menu)

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

        self.pushButton_15 = QPushButton(self.header_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"border:none;")
        icon8 = QIcon()
        icon8.addFile(u"Resource/image.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_15.setIcon(icon8)
        self.pushButton_15.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.pushButton_15)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 100, 66, 18))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 120, 66, 18))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(160, 60, 66, 18))
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_8 = QLabel(self.page_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(180, 110, 66, 18))
        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu_widget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Button_Menu.toggled.connect(self.icon_only_widget.setHidden)
        self.Button_Menu.toggled.connect(self.icon_name_widget.setVisible)
        self.Power_Saving_Btn1.toggled.connect(self.Power_Saving_Btn2.setChecked)
        self.Display_Mode_Btn1.toggled.connect(self.Display_Mode_Btn2.setChecked)
        self.Brightness_Btn1.toggled.connect(self.Brightness_Btn2.setChecked)
        self.Power_Mode_Btn1.toggled.connect(self.Power_Mode_Btn2.setChecked)
        self.Battery_Level_Btn1.toggled.connect(self.Battery_Level_Btn2.setChecked)
        self.Battery_Level_Btn2.toggled.connect(self.Battery_Level_Btn1.setChecked)
        self.Power_Mode_Btn2.toggled.connect(self.Power_Mode_Btn1.setChecked)
        self.Brightness_Btn2.toggled.connect(self.Brightness_Btn1.setChecked)
        self.Display_Mode_Btn2.toggled.connect(self.Display_Mode_Btn1.setChecked)
        self.Power_Saving_Btn2.toggled.connect(self.Power_Saving_Btn1.setChecked)
        self.Sign_Out_Btn1.toggled.connect(MainWindow.close)
        self.Sign_Out_Btn2.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo1.setText("")
        self.Battery_Level_Btn1.setText("")
        self.Power_Mode_Btn1.setText("")
        self.Brightness_Btn1.setText("")
        self.Display_Mode_Btn1.setText("")
        self.Power_Saving_Btn1.setText("")
        self.Sign_Out_Btn1.setText("")
        self.Logo_Label.setText("")
        self.SideBar_Label.setText(QCoreApplication.translate("MainWindow", u"Sidebar", None))
        self.Battery_Level_Btn2.setText(QCoreApplication.translate("MainWindow", u"Battery Level", None))
        self.Power_Mode_Btn2.setText(QCoreApplication.translate("MainWindow", u"Power Mode", None))
        self.Brightness_Btn2.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.Display_Mode_Btn2.setText(QCoreApplication.translate("MainWindow", u"Display Mode", None))
        self.Power_Saving_Btn2.setText(QCoreApplication.translate("MainWindow", u"Power Saving", None))
        self.Sign_Out_Btn2.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.Button_Menu.setText("")
        self.pushButton_14.setText("")
        self.pushButton_15.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"5", None))
    # retranslateUi

