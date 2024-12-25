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
        self.layoutWidget.setGeometry(QRect(130, 160, 371, 62))
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

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

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

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 240, 241, 18))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(330, 120, 121, 18))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"0%", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"100%", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Drag and drop to adjust brightness", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Brightness", None))
    # retranslateUi

