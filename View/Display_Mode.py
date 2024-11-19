# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'display_mode_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QSizePolicy,
    QSlider, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(576, 380)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 110, 141, 61))
        self.widget.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-radius:25px;")
        self.Night_Light_CB = QCheckBox(self.widget)
        self.Night_Light_CB.setObjectName(u"Night_Light_CB")
        self.Night_Light_CB.setGeometry(QRect(20, 20, 101, 24))
        self.Night_Light_CB.setCheckable(True)
        self.Night_Light_CB.setChecked(False)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(310, 110, 141, 61))
        self.widget_2.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-radius:25px;")
        self.Dark_Style_CB = QCheckBox(self.widget_2)
        self.Dark_Style_CB.setObjectName(u"Dark_Style_CB")
        self.Dark_Style_CB.setGeometry(QRect(20, 20, 92, 24))
        self.Dark_Style_CB.setChecked(False)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 220, 141, 18))
        self.Temperature_Slider = QSlider(Form)
        self.Temperature_Slider.setObjectName(u"Temperature_Slider")
        self.Temperature_Slider.setGeometry(QRect(80, 260, 371, 16))
        self.Temperature_Slider.setStyleSheet(u"")
        self.Temperature_Slider.setMinimum(1700)
        self.Temperature_Slider.setMaximum(4700)
        self.Temperature_Slider.setSingleStep(100)
        self.Temperature_Slider.setOrientation(Qt.Orientation.Horizontal)
        self.Temperature_Slider.setInvertedAppearance(False)
        self.Temperature_Slider.setInvertedControls(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Night_Light_CB.setText(QCoreApplication.translate("Form", u"Night Light", None))
        self.Dark_Style_CB.setText(QCoreApplication.translate("Form", u"Dark Style", None))
        self.label.setText(QCoreApplication.translate("Form", u"Color Temperature", None))
    # retranslateUi

