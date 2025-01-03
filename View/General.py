# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'general_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(590, 417)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(109, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.widget_2 = QWidget(self.widget_4)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Show_Battery_Percentage_CB = QCheckBox(self.widget_2)
        self.Show_Battery_Percentage_CB.setObjectName(u"Show_Battery_Percentage_CB")
        self.Show_Battery_Percentage_CB.setStyleSheet(u"QCheckBox {\n"
"    spacing: 10px;\n"
"    font-size: 16px;\n"
"    color: #333;\n"
"    background-color: rgb(246, 245, 244); /* N\u1ec1n m\u1eb7c \u0111\u1ecbnh */\n"
"    border: 2px solid rgb(222, 221, 218); /* Vi\u1ec1n m\u1eb7c \u0111\u1ecbnh */\n"
"    border-radius: 10px; /* Bo tr\u00f2n g\u00f3c */\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"    background-color: rgb(200, 255, 200); /* N\u1ec1n xanh l\u00e1 nh\u1ea1t khi checked */\n"
"    border: 2px solid rgb(0, 150, 0); /* Vi\u1ec1n xanh l\u00e1 \u0111\u1eadm khi checked */\n"
"    color: #333; /* Gi\u1eef m\u00e0u ch\u1eef khi checked */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.Show_Battery_Percentage_CB)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.Power_Button_Behavior_CbB = QComboBox(self.widget)
        self.Power_Button_Behavior_CbB.addItem("")
        self.Power_Button_Behavior_CbB.addItem("")
        self.Power_Button_Behavior_CbB.addItem("")
        self.Power_Button_Behavior_CbB.setObjectName(u"Power_Button_Behavior_CbB")
        self.Power_Button_Behavior_CbB.setStyleSheet(u"QComboBox {\n"
"    background-color: #FFFFFF; /* M\u00e0u n\u1ec1n tr\u1eafng */\n"
"    color: #333333;           /* M\u00e0u ch\u1eef \u0111\u1eadm */\n"
"    border: 1px solid #CCCCCC; /* Vi\u1ec1n m\u00e0u x\u00e1m nh\u1ea1t */\n"
"    border-radius: 5px;       /* Bo g\u00f3c nh\u1eb9 */\n"
"    padding: 5px 10px;        /* Kho\u1ea3ng c\u00e1ch b\u00ean trong */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #AAAAAA; /* Vi\u1ec1n \u0111\u1eadm h\u01a1n khi r\u00ea chu\u1ed9t */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;             /* Lo\u1ea1i b\u1ecf vi\u1ec1n dropdown */\n"
"    background-color: #FFFFFF; /* N\u1ec1n tr\u1eafng */\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #CCCCCC; /* Vi\u1ec1n tr\u00e1i dropdown */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/image/Resource/down-arrow.svg);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemVie"
                        "w {\n"
"    background-color: #FFFFFF; /* N\u1ec1n danh s\u00e1ch */\n"
"    border: 1px solid #CCCCCC; /* Vi\u1ec1n danh s\u00e1ch */\n"
"    selection-background-color: #F0F0F0; /* N\u1ec1n khi ch\u1ecdn */\n"
"    selection-color: #333333;  /* M\u00e0u ch\u1eef khi ch\u1ecdn */\n"
"    color: #333333;            /* M\u00e0u ch\u1eef m\u1eb7c \u0111\u1ecbnh */\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"QComboBox:disabled {\n"
"    background-color: #F0F0F0; /* N\u1ec1n x\u00e1m nh\u1ea1t */\n"
"    color: #A0A0A0;           /* M\u00e0u ch\u1eef x\u00e1m nh\u1ea1t */\n"
"    border: 1px solid #E0E0E0; /* Vi\u1ec1n x\u00e1m nh\u1ea1t */\n"
"}\n"
"\n"
"QComboBox::drop-down:disabled {\n"
"    background-color: #F0F0F0; /* N\u1ec1n x\u00e1m nh\u1ea1t cho dropdown */\n"
"    border-left: 1px solid #E0E0E0; /* Vi\u1ec1n tr\u00e1i x\u00e1m nh\u1ea1t */\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.Power_Button_Behavior_CbB)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget_4)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #007BFF; /* N\u1ec1n xanh */\n"
"    color: #FFFFFF;            /* Ch\u1eef tr\u1eafng */\n"
"    border: 1px solid #0056b3; /* Vi\u1ec1n xanh \u0111\u1eadm */\n"
"    border-radius: 5px;        /* Bo g\u00f3c nh\u1eb9 */\n"
"    padding: 8px 15px;         /* Kho\u1ea3ng c\u00e1ch b\u00ean trong */\n"
"    font-size: 14px;           /* C\u1ee1 ch\u1eef */\n"
"    font-weight: bold;         /* Ch\u1eef \u0111\u1eadm */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* N\u1ec1n \u0111\u1eadm h\u01a1n khi r\u00ea chu\u1ed9t */\n"
"    border: 1px solid #004085; /* Vi\u1ec1n \u0111\u1eadm h\u01a1n khi r\u00ea chu\u1ed9t */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004085; /* N\u1ec1n t\u1ed1i h\u01a1n khi nh\u1ea5n */\n"
"    border: 1px solid #003366; /* Vi\u1ec1n \u0111\u1eadm h\u01a1n khi nh\u1ea5n */\n"
"}")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Suspend_Btn = QPushButton(self.widget_3)
        self.Suspend_Btn.setObjectName(u"Suspend_Btn")

        self.gridLayout.addWidget(self.Suspend_Btn, 1, 0, 1, 1)

        self.Log_Out_Btn = QPushButton(self.widget_3)
        self.Log_Out_Btn.setObjectName(u"Log_Out_Btn")

        self.gridLayout.addWidget(self.Log_Out_Btn, 0, 0, 1, 1)

        self.Power_Off_Btn = QPushButton(self.widget_3)
        self.Power_Off_Btn.setObjectName(u"Power_Off_Btn")

        self.gridLayout.addWidget(self.Power_Off_Btn, 1, 1, 1, 1)

        self.Restart_Btn = QPushButton(self.widget_3)
        self.Restart_Btn.setObjectName(u"Restart_Btn")

        self.gridLayout.addWidget(self.Restart_Btn, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.widget_4)

        self.horizontalSpacer = QSpacerItem(108, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Show_Battery_Percentage_CB.setText(QCoreApplication.translate("Form", u"Show Battery Percentage", None))
        self.label.setText(QCoreApplication.translate("Form", u"Power Button Behavior", None))
        self.Power_Button_Behavior_CbB.setItemText(0, QCoreApplication.translate("Form", u"Suspend", None))
        self.Power_Button_Behavior_CbB.setItemText(1, QCoreApplication.translate("Form", u"Power Off", None))
        self.Power_Button_Behavior_CbB.setItemText(2, QCoreApplication.translate("Form", u"Nothing", None))

        self.Suspend_Btn.setText(QCoreApplication.translate("Form", u"Suspend", None))
        self.Log_Out_Btn.setText(QCoreApplication.translate("Form", u"Log Out", None))
        self.Power_Off_Btn.setText(QCoreApplication.translate("Form", u"Power Off", None))
        self.Restart_Btn.setText(QCoreApplication.translate("Form", u"Restart", None))
    # retranslateUi

