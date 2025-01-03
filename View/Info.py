# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_form.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(608, 431)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(55, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout = QGridLayout(self.widget_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_2 = QWidget(self.widget_4)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Logo = QLabel(self.widget_2)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMinimumSize(QSize(150, 200))
        self.Logo.setMaximumSize(QSize(150, 200))
        self.Logo.setStyleSheet(u"m")
        self.Logo.setPixmap(QPixmap(u":/image/Resource/QuocHieu.jpeg"))
        self.Logo.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.Logo)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.gridLayout.addWidget(self.widget_4, 0, 2, 1, 1)

        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_3 = QWidget(self.widget_6)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Logo_2 = QLabel(self.widget_3)
        self.Logo_2.setObjectName(u"Logo_2")
        self.Logo_2.setMinimumSize(QSize(150, 200))
        self.Logo_2.setMaximumSize(QSize(150, 200))
        self.Logo_2.setStyleSheet(u"m")
        self.Logo_2.setPixmap(QPixmap(u":/image/Resource/QuangHai.jpg"))
        self.Logo_2.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.Logo_2)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)


        self.verticalLayout_5.addWidget(self.widget_3)


        self.gridLayout.addWidget(self.widget_6, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_5)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalSpacer_3 = QSpacerItem(54, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Logo.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"V\u00f5 Qu\u1ed1c Hi\u1ebfu", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"- 22T_KHDL -", None))
        self.Logo_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Tr\u01b0\u01a1ng Quang H\u1ea3i", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"- 22T_KHDL -", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">GV h\u01b0\u1edbng d\u1eabn: </span><span style=\" font-size:12pt;\">Tr\u1ea7n H\u1ed3 Th\u1ee7y Ti\u00ean</span></p></body></html>", None))
    # retranslateUi

