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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(678, 431)
        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(60, 40, 291, 331))
        self.widget_4.setStyleSheet(u"        QPushButton {\n"
"            background-color: #e6e6e6;\n"
"            padding:10px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #d9d9d9;\n"
"        }")
        self.verticalLayout = QVBoxLayout(self.widget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"URW Gothic"])
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.widget = QWidget(self.widget_4)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(40, 40))
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/image/Resource/performance.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_6)

        self.Performance_Btn = QPushButton(self.widget)
        self.Performance_Btn.setObjectName(u"Performance_Btn")
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        self.Performance_Btn.setFont(font1)

        self.horizontalLayout.addWidget(self.Performance_Btn)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_2 = QWidget(self.widget_4)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(40, 40))
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setPixmap(QPixmap(u":/image/Resource/balance.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.Balanced_Btn = QPushButton(self.widget_2)
        self.Balanced_Btn.setObjectName(u"Balanced_Btn")

        self.horizontalLayout_2.addWidget(self.Balanced_Btn)


        self.verticalLayout.addWidget(self.widget_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.widget_3 = QWidget(self.widget_4)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(40, 40))
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/image/Resource/powersaver.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.Power_Saver_Btn = QPushButton(self.widget_3)
        self.Power_Saver_Btn.setObjectName(u"Power_Saver_Btn")

        self.horizontalLayout_3.addWidget(self.Power_Saver_Btn)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_5 = QWidget(Form)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(370, 40, 231, 321))
        self.verticalLayout_2 = QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"URW Gothic"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.textEdit = QTextEdit(self.widget_5)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"font: 600 16pt \"URW Gothic\";")

        self.verticalLayout_2.addWidget(self.textEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Power Mode", None))
        self.label_6.setText("")
        self.Performance_Btn.setText(QCoreApplication.translate("Form", u"Performance", None))
        self.label_5.setText("")
        self.Balanced_Btn.setText(QCoreApplication.translate("Form", u"Balanced", None))
        self.label_4.setText("")
        self.Power_Saver_Btn.setText(QCoreApplication.translate("Form", u"Power Saver", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Info", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'URW Gothic'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu Sans'; font-size:11pt; font-weight:400;\">infomation of button</span></p></body></html>", None))
    # retranslateUi

