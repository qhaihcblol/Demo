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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

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
        self.Menu_Btn = QPushButton(self.header_widget)
        self.Menu_Btn.setObjectName(u"Menu_Btn")
        self.Menu_Btn.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u"Resource/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon8.addFile(u"Resource/image.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Info_Btn.setIcon(icon8)
        self.Info_Btn.setIconSize(QSize(20, 20))
        self.Info_Btn.setCheckable(False)
        self.Info_Btn.setAutoExclusive(False)

        self.horizontalLayout_4.addWidget(self.Info_Btn)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Info_Page = QWidget()
        self.Info_Page.setObjectName(u"Info_Page")
        self.label_2 = QLabel(self.Info_Page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 110, 66, 18))
        self.stackedWidget.addWidget(self.Info_Page)
        self.Battery_Level_Page = QWidget()
        self.Battery_Level_Page.setObjectName(u"Battery_Level_Page")
        self.widget = QWidget(self.Battery_Level_Page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(130, 50, 300, 300))
        self.widget.setMinimumSize(QSize(300, 300))
        self.widget.setMaximumSize(QSize(300, 300))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.circle_lv = QFrame(self.widget)
        self.circle_lv.setObjectName(u"circle_lv")
        self.circle_lv.setStyleSheet(u"QFrame{\n"
"	background-color: qconicalgradient(cx:0.512029, cy:0.551, angle:90, stop:0.749 rgba(87, 227, 137, 255), stop:0.750 rgba(53, 132, 228, 255));\n"
"	border-radius: 140px;\n"
"}")
        self.circle_lv.setFrameShape(QFrame.Shape.NoFrame)
        self.circle_lv.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.circle_lv)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.circle_bg = QFrame(self.circle_lv)
        self.circle_bg.setObjectName(u"circle_bg")
        self.circle_bg.setStyleSheet(u"QFrame{\n"
"	background-color: #282a36;\n"
"	color: #f8f8f2;\n"
"	border-radius: 120px;\n"
"}")
        self.circle_bg.setFrameShape(QFrame.Shape.NoFrame)
        self.circle_bg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.circle_bg)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.texts = QFrame(self.circle_bg)
        self.texts.setObjectName(u"texts")
        self.texts.setMaximumSize(QSize(16777215, 180))
        self.texts.setStyleSheet(u"background: none;")
        self.texts.setFrameShape(QFrame.Shape.NoFrame)
        self.texts.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.texts)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.title = QLabel(self.texts)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setBold(True)
        self.title.setFont(font2)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.title, 0, 0, 1, 1)

        self.frame = QFrame(self.texts)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.version = QLabel(self.frame)
        self.version.setObjectName(u"version")
        self.version.setMinimumSize(QSize(120, 24))
        self.version.setMaximumSize(QSize(120, 24))
        self.version.setStyleSheet(u"QLabel{\n"
"border-radius:12px;\n"
"color: rgb(151,159,200);\n"
"background-color: rgb(68,71,90)\n"
"}")
        self.version.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.version)


        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 1)

        self.loading = QLabel(self.texts)
        self.loading.setObjectName(u"loading")
        self.loading.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.loading, 3, 0, 1, 1)

        self.empty = QFrame(self.texts)
        self.empty.setObjectName(u"empty")
        self.empty.setMinimumSize(QSize(0, 80))
        self.empty.setFrameShape(QFrame.Shape.NoFrame)
        self.empty.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.empty)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Percent = QLabel(self.empty)
        self.Percent.setObjectName(u"Percent")
        self.Percent.setMaximumSize(QSize(200, 200))
        font3 = QFont()
        font3.setFamilies([u"Noto Sans Bamum"])
        font3.setPointSize(35)
        font3.setBold(False)
        font3.setItalic(False)
        self.Percent.setFont(font3)
        self.Percent.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.Percent)


        self.gridLayout_2.addWidget(self.empty, 1, 0, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_2)


        self.verticalLayout_8.addWidget(self.texts)


        self.verticalLayout_7.addWidget(self.circle_bg)


        self.verticalLayout_6.addWidget(self.circle_lv)

        self.stackedWidget.addWidget(self.Battery_Level_Page)
        self.Power_Mode_Page = QWidget()
        self.Power_Mode_Page.setObjectName(u"Power_Mode_Page")
        self.label_5 = QLabel(self.Power_Mode_Page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 100, 191, 18))
        self.stackedWidget.addWidget(self.Power_Mode_Page)
        self.Brightness_Page = QWidget()
        self.Brightness_Page.setObjectName(u"Brightness_Page")
        self.label_6 = QLabel(self.Brightness_Page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 120, 311, 18))
        self.stackedWidget.addWidget(self.Brightness_Page)
        self.Display_Mode_Page = QWidget()
        self.Display_Mode_Page.setObjectName(u"Display_Mode_Page")
        self.label_7 = QLabel(self.Display_Mode_Page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(160, 60, 251, 18))
        self.stackedWidget.addWidget(self.Display_Mode_Page)
        self.Power_Saving_Page = QWidget()
        self.Power_Saving_Page.setObjectName(u"Power_Saving_Page")
        self.label_8 = QLabel(self.Power_Saving_Page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(180, 110, 241, 18))
        self.stackedWidget.addWidget(self.Power_Saving_Page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu_widget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Menu_Btn.toggled.connect(self.icon_only_widget.setHidden)
        self.Menu_Btn.toggled.connect(self.icon_name_widget.setVisible)
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
        self.Menu_Btn.setText("")
        self.pushButton_14.setText("")
        self.Info_Btn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Info page", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Battery Level", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0 - Beta 1", None))
        self.loading.setText(QCoreApplication.translate("MainWindow", u"Loading ...", None))
        self.Percent.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt;\">0</span><span style=\" font-size:24pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Power Mode", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"dispay mode", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"power saving", None))
    # retranslateUi

