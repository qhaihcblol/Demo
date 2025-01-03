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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(701, 431)
        self.horizontalLayout_6 = QHBoxLayout(Form)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(146, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_3 = QWidget(self.widget_4)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_3.addWidget(self.widget_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-radius:15px;")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_2 = QWidget(self.widget_5)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/image/Resource/brightness.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setBold(False)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)

        self.Brightness_Slider = QSlider(self.widget_2)
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

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.widget = QWidget(self.widget_5)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QPushButton{\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF; /* Ch\u1eef tr\u1eafng */\n"
"    background-color: #2196F3; /* M\u00e0u xanh lam nh\u1ea1t */\n"
"    border: 2px solid #1976D2; /* Vi\u1ec1n xanh \u0111\u1eadm */\n"
"    border-radius: 10px;\n"
"    padding: 5px 15px;\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1976D2; /* \u0110\u1ed5i sang xanh \u0111\u1eadm khi hover */\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self._25_Btn = QPushButton(self.widget)
        self._25_Btn.setObjectName(u"_25_Btn")

        self.horizontalLayout_2.addWidget(self._25_Btn)

        self._50_Btn = QPushButton(self.widget)
        self._50_Btn.setObjectName(u"_50_Btn")

        self.horizontalLayout_2.addWidget(self._50_Btn)

        self._75_Btn = QPushButton(self.widget)
        self._75_Btn.setObjectName(u"_75_Btn")

        self.horizontalLayout_2.addWidget(self._75_Btn)

        self._100_Btn = QPushButton(self.widget)
        self._100_Btn.setObjectName(u"_100_Btn")

        self.horizontalLayout_2.addWidget(self._100_Btn)


        self.verticalLayout_4.addWidget(self.widget)

        self.percent = QLabel(self.widget_5)
        self.percent.setObjectName(u"percent")
        font1 = QFont()
        font1.setBold(True)
        self.percent.setFont(font1)
        self.percent.setStyleSheet(u"QLabel{\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: #4CAF50; /* M\u00e0u xanh l\u00e1 nh\u1ea1t */\n"
"    margin: 10px 0;\n"
"    text-align: center;\n"
"}")
        self.percent.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.percent)


        self.verticalLayout_3.addWidget(self.widget_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"    font-size: 15px;\n"
"    font-style: italic;\n"
"    color: #555555; /* M\u00e0u x\u00e1m \u0111\u1eadm */\n"
"    margin-top: 5px;\n"
"    text-align: center;\n"
"}")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_4 = QSpacerItem(145, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_6.addWidget(self.widget_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"0%", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"100%", None))
        self._25_Btn.setText(QCoreApplication.translate("Form", u"25%", None))
        self._50_Btn.setText(QCoreApplication.translate("Form", u"50%", None))
        self._75_Btn.setText(QCoreApplication.translate("Form", u"75%", None))
        self._100_Btn.setText(QCoreApplication.translate("Form", u"100%", None))
        self.percent.setText(QCoreApplication.translate("Form", u"Brightness: n%", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Drag and drop to adjust brightness", None))
    # retranslateUi

