# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'power_saving_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(686, 431)
        self.horizontalLayout_7 = QHBoxLayout(Form)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(79, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.widget_9 = QWidget(Form)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_5 = QVBoxLayout(self.widget_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_8 = QWidget(self.widget_9)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.widget_8)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.widget_7 = QWidget(self.widget_8)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_5 = QWidget(self.widget_7)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_2 = QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.On_Battery_Power_CB = QCheckBox(self.widget_5)
        self.On_Battery_Power_CB.setObjectName(u"On_Battery_Power_CB")
        self.On_Battery_Power_CB.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_2.addWidget(self.On_Battery_Power_CB)

        self.widget_3 = QWidget(self.widget_5)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.Delay1_CbB = QComboBox(self.widget_3)
        self.Delay1_CbB.addItem("")
        self.Delay1_CbB.addItem("")
        self.Delay1_CbB.addItem("")
        self.Delay1_CbB.addItem("")
        self.Delay1_CbB.addItem("")
        self.Delay1_CbB.addItem("")
        self.Delay1_CbB.addItem("")
        self.Delay1_CbB.addItem("")
        self.Delay1_CbB.addItem("")
        self.Delay1_CbB.addItem("")
        self.Delay1_CbB.setObjectName(u"Delay1_CbB")
        self.Delay1_CbB.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout_2.addWidget(self.Delay1_CbB)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.horizontalLayout_4.addWidget(self.widget_5)

        self.line = QFrame(self.widget_7)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.widget_6 = QWidget(self.widget_7)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Plugged_In_CB = QCheckBox(self.widget_6)
        self.Plugged_In_CB.setObjectName(u"Plugged_In_CB")
        self.Plugged_In_CB.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout_3.addWidget(self.Plugged_In_CB)

        self.widget_4 = QWidget(self.widget_6)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.Delay2_CbB = QComboBox(self.widget_4)
        self.Delay2_CbB.addItem("")
        self.Delay2_CbB.addItem("")
        self.Delay2_CbB.addItem("")
        self.Delay2_CbB.addItem("")
        self.Delay2_CbB.addItem("")
        self.Delay2_CbB.addItem("")
        self.Delay2_CbB.addItem("")
        self.Delay2_CbB.addItem("")
        self.Delay2_CbB.addItem("")
        self.Delay2_CbB.addItem("")
        self.Delay2_CbB.setObjectName(u"Delay2_CbB")
        self.Delay2_CbB.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout_3.addWidget(self.Delay2_CbB)


        self.verticalLayout_3.addWidget(self.widget_4)


        self.horizontalLayout_4.addWidget(self.widget_6)


        self.verticalLayout_4.addWidget(self.widget_7)


        self.verticalLayout_5.addWidget(self.widget_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.widget_2 = QWidget(self.widget_9)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Auto_PS_CB = QCheckBox(self.widget_2)
        self.Auto_PS_CB.setObjectName(u"Auto_PS_CB")
        self.Auto_PS_CB.setStyleSheet(u"QCheckBox {\n"
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
        self.Auto_PS_CB.setChecked(False)

        self.verticalLayout.addWidget(self.Auto_PS_CB)

        self.Dim_Screen_CB = QCheckBox(self.widget_2)
        self.Dim_Screen_CB.setObjectName(u"Dim_Screen_CB")
        self.Dim_Screen_CB.setStyleSheet(u"QCheckBox {\n"
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

        self.verticalLayout.addWidget(self.Dim_Screen_CB)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label)

        self.Screen_Blank_CbB = QComboBox(self.widget)
        self.Screen_Blank_CbB.addItem("")
        self.Screen_Blank_CbB.addItem("")
        self.Screen_Blank_CbB.addItem("")
        self.Screen_Blank_CbB.addItem("")
        self.Screen_Blank_CbB.addItem("")
        self.Screen_Blank_CbB.addItem("")
        self.Screen_Blank_CbB.addItem("")
        self.Screen_Blank_CbB.addItem("")
        self.Screen_Blank_CbB.addItem("")
        self.Screen_Blank_CbB.addItem("")
        self.Screen_Blank_CbB.setObjectName(u"Screen_Blank_CbB")
        self.Screen_Blank_CbB.setStyleSheet(u"QComboBox {\n"
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
"")

        self.horizontalLayout.addWidget(self.Screen_Blank_CbB)


        self.verticalLayout.addWidget(self.widget)


        self.horizontalLayout_5.addWidget(self.widget_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_7.addWidget(self.widget_9)

        self.horizontalSpacer_6 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Automatic Suspend", None))
        self.On_Battery_Power_CB.setText(QCoreApplication.translate("Form", u"On Battery Power", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Delay", None))
        self.Delay1_CbB.setItemText(0, QCoreApplication.translate("Form", u"15 minutes", None))
        self.Delay1_CbB.setItemText(1, QCoreApplication.translate("Form", u"20 minutes", None))
        self.Delay1_CbB.setItemText(2, QCoreApplication.translate("Form", u"25 minutes", None))
        self.Delay1_CbB.setItemText(3, QCoreApplication.translate("Form", u"30 minutes", None))
        self.Delay1_CbB.setItemText(4, QCoreApplication.translate("Form", u"45 minutes", None))
        self.Delay1_CbB.setItemText(5, QCoreApplication.translate("Form", u"1 hour", None))
        self.Delay1_CbB.setItemText(6, QCoreApplication.translate("Form", u"80 minutes", None))
        self.Delay1_CbB.setItemText(7, QCoreApplication.translate("Form", u"90 minutes", None))
        self.Delay1_CbB.setItemText(8, QCoreApplication.translate("Form", u"100 minutes", None))
        self.Delay1_CbB.setItemText(9, QCoreApplication.translate("Form", u"2 hours", None))

        self.Plugged_In_CB.setText(QCoreApplication.translate("Form", u"Plugged In", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Delay", None))
        self.Delay2_CbB.setItemText(0, QCoreApplication.translate("Form", u"15 minutes", None))
        self.Delay2_CbB.setItemText(1, QCoreApplication.translate("Form", u"20 minutes", None))
        self.Delay2_CbB.setItemText(2, QCoreApplication.translate("Form", u"25 minutes", None))
        self.Delay2_CbB.setItemText(3, QCoreApplication.translate("Form", u"30 minutes", None))
        self.Delay2_CbB.setItemText(4, QCoreApplication.translate("Form", u"45 minutes", None))
        self.Delay2_CbB.setItemText(5, QCoreApplication.translate("Form", u"1 hour", None))
        self.Delay2_CbB.setItemText(6, QCoreApplication.translate("Form", u"80 minutes", None))
        self.Delay2_CbB.setItemText(7, QCoreApplication.translate("Form", u"90 minutes", None))
        self.Delay2_CbB.setItemText(8, QCoreApplication.translate("Form", u"100 minutes", None))
        self.Delay2_CbB.setItemText(9, QCoreApplication.translate("Form", u"2 hours", None))

        self.Auto_PS_CB.setText(QCoreApplication.translate("Form", u"Automatic Power Saver", None))
        self.Dim_Screen_CB.setText(QCoreApplication.translate("Form", u"Dim Screen", None))
        self.label.setText(QCoreApplication.translate("Form", u"Screen Blank", None))
        self.Screen_Blank_CbB.setItemText(0, QCoreApplication.translate("Form", u"1 minutes", None))
        self.Screen_Blank_CbB.setItemText(1, QCoreApplication.translate("Form", u"2 minutes", None))
        self.Screen_Blank_CbB.setItemText(2, QCoreApplication.translate("Form", u"3 minutes", None))
        self.Screen_Blank_CbB.setItemText(3, QCoreApplication.translate("Form", u"4 minutes", None))
        self.Screen_Blank_CbB.setItemText(4, QCoreApplication.translate("Form", u"5 minutes", None))
        self.Screen_Blank_CbB.setItemText(5, QCoreApplication.translate("Form", u"8 minutes", None))
        self.Screen_Blank_CbB.setItemText(6, QCoreApplication.translate("Form", u"10 minutes", None))
        self.Screen_Blank_CbB.setItemText(7, QCoreApplication.translate("Form", u"12 minutes", None))
        self.Screen_Blank_CbB.setItemText(8, QCoreApplication.translate("Form", u"15 minutes", None))
        self.Screen_Blank_CbB.setItemText(9, QCoreApplication.translate("Form", u"Never", None))

    # retranslateUi

