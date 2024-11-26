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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(678, 431)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 280, 40, 40))
        self.label_4.setMinimumSize(QSize(40, 40))
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/image/Resource/powersaver.png"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 190, 40, 40))
        self.label_5.setMinimumSize(QSize(40, 40))
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setPixmap(QPixmap(u":/image/Resource/balance.png"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(120, 90, 40, 40))
        self.label_6.setMinimumSize(QSize(40, 40))
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/image/Resource/performance.png"))
        self.label_6.setScaledContents(True)
        self.Performance_Btn = QPushButton(Form)
        self.Performance_Btn.setObjectName(u"Performance_Btn")
        self.Performance_Btn.setGeometry(QRect(210, 90, 181, 41))
        self.Balanced_Btn = QPushButton(Form)
        self.Balanced_Btn.setObjectName(u"Balanced_Btn")
        self.Balanced_Btn.setGeometry(QRect(210, 190, 181, 41))
        self.Power_Saver_Btn = QPushButton(Form)
        self.Power_Saver_Btn.setObjectName(u"Power_Saver_Btn")
        self.Power_Saver_Btn.setGeometry(QRect(210, 280, 181, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.Performance_Btn.setText(QCoreApplication.translate("Form", u"Performance", None))
        self.Balanced_Btn.setText(QCoreApplication.translate("Form", u"Balanced", None))
        self.Power_Saver_Btn.setText(QCoreApplication.translate("Form", u"Power Saver", None))
    # retranslateUi

