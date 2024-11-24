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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(576, 380)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 70, 171, 20))
        self.Power_Button_Behavior_CbB = QComboBox(Form)
        self.Power_Button_Behavior_CbB.addItem("")
        self.Power_Button_Behavior_CbB.addItem("")
        self.Power_Button_Behavior_CbB.addItem("")
        self.Power_Button_Behavior_CbB.setObjectName(u"Power_Button_Behavior_CbB")
        self.Power_Button_Behavior_CbB.setGeometry(QRect(310, 70, 111, 26))
        self.Show_Battery_Percentage_CB = QCheckBox(Form)
        self.Show_Battery_Percentage_CB.setObjectName(u"Show_Battery_Percentage_CB")
        self.Show_Battery_Percentage_CB.setGeometry(QRect(140, 120, 201, 24))
        self.Suspend_Btn = QPushButton(Form)
        self.Suspend_Btn.setObjectName(u"Suspend_Btn")
        self.Suspend_Btn.setGeometry(QRect(150, 210, 88, 26))
        self.Restart_Btn = QPushButton(Form)
        self.Restart_Btn.setObjectName(u"Restart_Btn")
        self.Restart_Btn.setGeometry(QRect(330, 210, 88, 26))
        self.Power_Off_Btn = QPushButton(Form)
        self.Power_Off_Btn.setObjectName(u"Power_Off_Btn")
        self.Power_Off_Btn.setGeometry(QRect(150, 270, 88, 26))
        self.Log_Out_Btn = QPushButton(Form)
        self.Log_Out_Btn.setObjectName(u"Log_Out_Btn")
        self.Log_Out_Btn.setGeometry(QRect(330, 270, 88, 26))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Power Button Behavior", None))
        self.Power_Button_Behavior_CbB.setItemText(0, QCoreApplication.translate("Form", u"Suspend", None))
        self.Power_Button_Behavior_CbB.setItemText(1, QCoreApplication.translate("Form", u"Power Off", None))
        self.Power_Button_Behavior_CbB.setItemText(2, QCoreApplication.translate("Form", u"Nothing", None))

        self.Show_Battery_Percentage_CB.setText(QCoreApplication.translate("Form", u"Show Battery Percentage", None))
        self.Suspend_Btn.setText(QCoreApplication.translate("Form", u"Suspend", None))
        self.Restart_Btn.setText(QCoreApplication.translate("Form", u"Restart", None))
        self.Power_Off_Btn.setText(QCoreApplication.translate("Form", u"Power Off", None))
        self.Log_Out_Btn.setText(QCoreApplication.translate("Form", u"Log Out", None))
    # retranslateUi

