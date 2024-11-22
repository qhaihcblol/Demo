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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(576, 380)
        self.Dim_Screen_CB = QCheckBox(Form)
        self.Dim_Screen_CB.setObjectName(u"Dim_Screen_CB")
        self.Dim_Screen_CB.setGeometry(QRect(150, 10, 111, 24))
        self.Auto_PS_Btn = QCheckBox(Form)
        self.Auto_PS_Btn.setObjectName(u"Auto_PS_Btn")
        self.Auto_PS_Btn.setGeometry(QRect(150, 100, 291, 24))
        self.Screen_Blank_CbB = QComboBox(Form)
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
        self.Screen_Blank_CbB.setGeometry(QRect(270, 60, 101, 26))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 60, 91, 18))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 160, 171, 18))
        self.On_Battery_Power_CB = QCheckBox(Form)
        self.On_Battery_Power_CB.setObjectName(u"On_Battery_Power_CB")
        self.On_Battery_Power_CB.setGeometry(QRect(190, 200, 151, 24))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 240, 66, 18))
        self.Delay1_CbB = QComboBox(Form)
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
        self.Delay1_CbB.setGeometry(QRect(280, 240, 101, 26))
        self.Plugged_In_CB = QCheckBox(Form)
        self.Plugged_In_CB.setObjectName(u"Plugged_In_CB")
        self.Plugged_In_CB.setGeometry(QRect(190, 280, 141, 24))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 320, 66, 18))
        self.Delay2_CbB = QComboBox(Form)
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
        self.Delay2_CbB.setGeometry(QRect(280, 320, 101, 26))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Dim_Screen_CB.setText(QCoreApplication.translate("Form", u"Dim Screen", None))
        self.Auto_PS_Btn.setText(QCoreApplication.translate("Form", u"Automatic Power Saver", None))
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

        self.label.setText(QCoreApplication.translate("Form", u"Screen Blank", None))
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

    # retranslateUi

