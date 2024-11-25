# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'battery_level_form.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(861, 431)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
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
        font = QFont()
        font.setBold(True)
        self.title.setFont(font)
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
        font1 = QFont()
        font1.setFamilies([u"Noto Sans Bamum"])
        font1.setPointSize(35)
        font1.setBold(False)
        font1.setItalic(False)
        self.Percent.setFont(font1)
        self.Percent.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.Percent)


        self.gridLayout_2.addWidget(self.empty, 1, 0, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_2)


        self.verticalLayout_8.addWidget(self.texts)


        self.verticalLayout_7.addWidget(self.circle_bg)


        self.verticalLayout_6.addWidget(self.circle_lv)


        self.horizontalLayout_2.addWidget(self.widget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.widget_5 = QWidget(Form)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout = QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.widget_5)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(203, 222, 221);\n"
"	font: 600 12pt \"URW Gothic\";\n"
"	padding:5px;\n"
"    border-top-left-radius: 7px; /* Bo g\u00f3c tr\u00ean b\u00ean tr\u00e1i */\n"
"    border-bottom-left-radius: 7px; /* Bo g\u00f3c d\u01b0\u1edbi b\u00ean tr\u00e1i */\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.Time_To = QLabel(self.widget_2)
        self.Time_To.setObjectName(u"Time_To")

        self.verticalLayout.addWidget(self.Time_To)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget_5)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(192, 191, 188);\n"
"	font: 600 12pt \"URW Gothic\";\n"
"	padding:5px;\n"
"    border-top-right-radius: 7px; /* Bo g\u00f3c tr\u00ean b\u00ean tr\u00e1i */\n"
"    border-bottom-right-radius: 7px; /* Bo g\u00f3c d\u01b0\u1edbi b\u00ean tr\u00e1i */\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.State_Result = QLabel(self.widget_3)
        self.State_Result.setObjectName(u"State_Result")

        self.verticalLayout_2.addWidget(self.State_Result)

        self.Percentage_Result = QLabel(self.widget_3)
        self.Percentage_Result.setObjectName(u"Percentage_Result")

        self.verticalLayout_2.addWidget(self.Percentage_Result)

        self.Time_Result = QLabel(self.widget_3)
        self.Time_Result.setObjectName(u"Time_Result")

        self.verticalLayout_2.addWidget(self.Time_Result)


        self.verticalLayout_11.addLayout(self.verticalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addWidget(self.widget_3)


        self.horizontalLayout_2.addWidget(self.widget_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"Battery Level", None))
        self.version.setText(QCoreApplication.translate("Form", u"v1.0.0 - Beta 1", None))
        self.loading.setText(QCoreApplication.translate("Form", u"Loading ...", None))
        self.Percent.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:36pt;\">0</span><span style=\" font-size:24pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"State:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Percentage:", None))
        self.Time_To.setText(QCoreApplication.translate("Form", u"Time to empty/full:", None))
        self.State_Result.setText(QCoreApplication.translate("Form", u"Result", None))
        self.Percentage_Result.setText(QCoreApplication.translate("Form", u"Result", None))
        self.Time_Result.setText(QCoreApplication.translate("Form", u"Result", None))
    # retranslateUi

