# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'power_mode_form.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(576, 380)
        self.Power_Mode_Option = QGroupBox(Form)
        self.Power_Mode_Option.setObjectName(u"Power_Mode_Option")
        self.Power_Mode_Option.setGeometry(QRect(110, 60, 341, 221))
        self.Power_Mode_Option.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(153, 193, 241);\n"
"	border-radius:5px;\n"
"	padding:15px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.Power_Mode_Option)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Performance_RBtn = QRadioButton(self.Power_Mode_Option)
        self.Performance_RBtn.setObjectName(u"Performance_RBtn")

        self.verticalLayout.addWidget(self.Performance_RBtn)

        self.Balanced_RBtn = QRadioButton(self.Power_Mode_Option)
        self.Balanced_RBtn.setObjectName(u"Balanced_RBtn")

        self.verticalLayout.addWidget(self.Balanced_RBtn)

        self.PowerSaver_RBtn = QRadioButton(self.Power_Mode_Option)
        self.PowerSaver_RBtn.setObjectName(u"PowerSaver_RBtn")

        self.verticalLayout.addWidget(self.PowerSaver_RBtn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Power_Mode_Option.setTitle(QCoreApplication.translate("Form", u"Power Mode", None))
        self.Performance_RBtn.setText(QCoreApplication.translate("Form", u"Performance", None))
        self.Balanced_RBtn.setText(QCoreApplication.translate("Form", u"Balanced", None))
        self.PowerSaver_RBtn.setText(QCoreApplication.translate("Form", u"Power Saver", None))
    # retranslateUi

