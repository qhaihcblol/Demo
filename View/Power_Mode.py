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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(645, 431)
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.widget_5 = QWidget(Form)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(450, 350))
        self.widget_5.setMaximumSize(QSize(450, 350))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"QPushButton {\n"
"    background-color: #e6e6e6;\n"
"    color: #333; /* M\u00e0u ch\u1eef */\n"
"    padding: 10px 15px;\n"
"    border: 2px solid #cccccc; /* Vi\u1ec1n */\n"
"    border-radius: 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d9d9d9; /* M\u00e0u n\u1ec1n khi hover */\n"
"    border-color: #bbbbbb; /* Vi\u1ec1n khi hover */\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.widget = QWidget(self.widget_4)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
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
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.Performance_Btn.setFont(font)

        self.horizontalLayout.addWidget(self.Performance_Btn)


        self.verticalLayout.addWidget(self.widget)

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

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.info = QLabel(self.widget_5)
        self.info.setObjectName(u"info")
        self.info.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(True)
        self.info.setFont(font1)
        self.info.setStyleSheet(u"QLabel {\n"
"    background-color: #f2f2f2;    /* M\u00e0u n\u1ec1n s\u00e1ng nh\u1eb9 */\n"
"    color: #333333;               /* M\u00e0u ch\u1eef x\u00e1m \u0111\u1eadm */\n"
"    border: 1px solid #cccccc;    /* \u0110\u01b0\u1eddng vi\u1ec1n m\u00e0u x\u00e1m nh\u1ea1t */\n"
"    border-radius: 8px;           /* Bo tr\u00f2n g\u00f3c */\n"
"    font-family: \"Arial\", sans-serif; /* Font ch\u1eef hi\u1ec7n \u0111\u1ea1i */\n"
"    font-size: 20px;              /* K\u00edch th\u01b0\u1edbc ch\u1eef v\u1eeba ph\u1ea3i */\n"
"    font-weight: bold;            /* Ch\u1eef in \u0111\u1eadm */\n"
"    padding: 5px;                 /* Kho\u1ea3ng c\u00e1ch n\u1ed9i dung b\u00ean trong */\n"
"    text-align: center;           /* Canh gi\u1eefa n\u1ed9i dung */\n"
"}")
        self.info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.info)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout_5.addWidget(self.widget_5)

        self.horizontalSpacer_2 = QSpacerItem(79, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText("")
#if QT_CONFIG(tooltip)
        self.Performance_Btn.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; font-style:italic; color:#5e5c64;\">High </span><span style=\" font-size:11pt; font-weight:400; font-style:italic; color:#5e5c64;\">performance and power usage</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Performance_Btn.setText(QCoreApplication.translate("Form", u"Performance", None))
        self.label_5.setText("")
#if QT_CONFIG(tooltip)
        self.Balanced_Btn.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; font-style:italic; color:#5e5c64;\">Standard </span><span style=\" font-size:11pt; font-weight:400; font-style:italic; color:#5e5c64;\">performance and power usage</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Balanced_Btn.setText(QCoreApplication.translate("Form", u"Balanced", None))
        self.label_4.setText("")
#if QT_CONFIG(tooltip)
        self.Power_Saver_Btn.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; font-style:italic; color:#5e5c64;\">Reduced </span><span style=\" font-size:11pt; font-weight:400; font-style:italic; color:#5e5c64;\">performance and power usage</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Power_Saver_Btn.setText(QCoreApplication.translate("Form", u"Power Saver", None))
        self.info.setText(QCoreApplication.translate("Form", u"Infomation", None))
    # retranslateUi

