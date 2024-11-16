# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'brightness_form.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSlider, QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(576, 380)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 160, 321, 62))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/image/Resource/brightness.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.Brightness_Slider = QSlider(self.layoutWidget)
        self.Brightness_Slider.setObjectName(u"Brightness_Slider")
        self.Brightness_Slider.setStyleSheet(u"QSlider{\n"
"	background-color: rgb(222, 221, 218);\n"
"	border-radius:15px;\n"
"	padding:10px;\n"
"}")
        self.Brightness_Slider.setMinimum(9)
        self.Brightness_Slider.setMaximum(937)
        self.Brightness_Slider.setOrientation(Qt.Orientation.Horizontal)
        self.Brightness_Slider.setTickPosition(QSlider.TickPosition.NoTicks)

        self.horizontalLayout.addWidget(self.Brightness_Slider)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
    # retranslateUi

