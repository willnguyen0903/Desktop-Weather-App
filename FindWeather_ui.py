# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 612)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu = QPushButton(self.header_widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon)
        self.menu.setIconSize(QSize(20, 20))
        self.menu.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.menu)

        self.horizontalSpacer_2 = QSpacerItem(158, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setPlaceholderText("Enter Location's Name")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_16 = QPushButton(self.header_widget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        icon1 = QIcon()
        icon1.addFile(u":/images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButton_16)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(157, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_14 = QPushButton(self.header_widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"border:none;")
        icon2 = QIcon()
        icon2.addFile(u":/images/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.pushButton_14)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Celcius_page = QWidget()
        self.Celcius_page.setObjectName(u"Celcius_page")
        self.celcius_label = QLabel(self.Celcius_page)
        self.celcius_label.setObjectName(u"celcius_label")
        self.celcius_label.setGeometry(QRect(0, 0, 531, 541))
        font = QFont()
        font.setFamilies([u"Fixedsys"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.celcius_label.setFont(font)
        self.celcius_label.setStyleSheet(u"font: 9pt \"Fixedsys\";")
        self.celcius_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.Celcius_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.fahrenheit_label = QLabel(self.profile_page)
        self.fahrenheit_label.setObjectName(u"fahrenheit_label")
        self.fahrenheit_label.setGeometry(QRect(0, 0, 531, 541))
        self.fahrenheit_label.setFont(font)
        self.fahrenheit_label.setStyleSheet(u"font: 9pt \"Fixedsys\";")
        self.fahrenheit_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.profile_page)
        self.notification_page = QWidget()
        self.notification_page.setObjectName(u"notification_page")
        self.label_4 = QLabel(self.notification_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 150, 241, 31))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_4.setFont(font1)
        self.stackedWidget.addWidget(self.notification_page)
        self.messages_page = QWidget()
        self.messages_page.setObjectName(u"messages_page")
        self.label_6 = QLabel(self.messages_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 110, 241, 31))
        self.label_6.setFont(font1)
        self.stackedWidget.addWidget(self.messages_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.label_8 = QLabel(self.settings_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(170, 20, 241, 31))
        self.label_8.setFont(font1)
        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget { \n"
"	background-color: rgb(31, 149, 239);\n"
"}\n"
"QPushButton {\n"
"	color:white;\n"
"	border: none;\n"
"	height: 30px;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: #f5fafe;\n"
"	color:#1f95ef;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/images/profile_pic.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_button = QPushButton(self.icon_only_widget)
        self.dashboard_button.setObjectName(u"dashboard_button")
        icon3 = QIcon()
        icon3.addFile(u":/images/celcius-white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/images/celcius.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_button.setIcon(icon3)
        self.dashboard_button.setCheckable(True)
        self.dashboard_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_button)

        self.profile_button = QPushButton(self.icon_only_widget)
        self.profile_button.setObjectName(u"profile_button")
        icon4 = QIcon()
        icon4.addFile(u"images/farenheit-white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/images/fahrenheit.png", QSize(), QIcon.Normal, QIcon.On)
        self.profile_button.setIcon(icon4)
        self.profile_button.setCheckable(True)
        self.profile_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.profile_button)

        self.messages_button = QPushButton(self.icon_only_widget)
        self.messages_button.setObjectName(u"messages_button")
        icon5 = QIcon()
        icon5.addFile(u":/images/messages_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/images/messages.png", QSize(), QIcon.Normal, QIcon.On)
        self.messages_button.setIcon(icon5)
        self.messages_button.setCheckable(True)
        self.messages_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.messages_button)

        self.notification_button = QPushButton(self.icon_only_widget)
        self.notification_button.setObjectName(u"notification_button")
        icon6 = QIcon()
        icon6.addFile(u":/images/notifications_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/images/notifications.png", QSize(), QIcon.Normal, QIcon.On)
        self.notification_button.setIcon(icon6)
        self.notification_button.setCheckable(True)
        self.notification_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.notification_button)

        self.settings_button = QPushButton(self.icon_only_widget)
        self.settings_button.setObjectName(u"settings_button")
        icon7 = QIcon()
        icon7.addFile(u":/images/settings_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/images/settings.png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_button.setIcon(icon7)
        self.settings_button.setCheckable(True)
        self.settings_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settings_button)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 275, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.sign_out_button = QPushButton(self.icon_only_widget)
        self.sign_out_button.setObjectName(u"sign_out_button")
        icon8 = QIcon()
        icon8.addFile(u":/images/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/images/log_out.png", QSize(), QIcon.Normal, QIcon.On)
        self.sign_out_button.setIcon(icon8)
        self.sign_out_button.setCheckable(True)
        self.sign_out_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.sign_out_button)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget { \n"
"	background-color: rgb(31, 149, 239);\n"
"	color:white;\n"
"}\n"
"QPushButton {\n"
"	color:white;\n"
"	text-align:left;\n"
"	height: 30px;\n"
"	border: none;\n"
"	padding-left: 10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #f5fafe;\n"
"	color:#1f95ef;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/images/profile_pic.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_3.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_button_2 = QPushButton(self.icon_name_widget)
        self.dashboard_button_2.setObjectName(u"dashboard_button_2")
        self.dashboard_button_2.setIcon(icon3)
        self.dashboard_button_2.setCheckable(True)
        self.dashboard_button_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_button_2)

        self.profile_button_2 = QPushButton(self.icon_name_widget)
        self.profile_button_2.setObjectName(u"profile_button_2")
        icon9 = QIcon()
        icon9.addFile(u"images/farenheit-white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u"images/fahrenheit.png", QSize(), QIcon.Normal, QIcon.On)
        self.profile_button_2.setIcon(icon9)
        self.profile_button_2.setCheckable(True)
        self.profile_button_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.profile_button_2)

        self.messages_button_2 = QPushButton(self.icon_name_widget)
        self.messages_button_2.setObjectName(u"messages_button_2")
        self.messages_button_2.setIcon(icon5)
        self.messages_button_2.setCheckable(True)
        self.messages_button_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.messages_button_2)

        self.notification_button_2 = QPushButton(self.icon_name_widget)
        self.notification_button_2.setObjectName(u"notification_button_2")
        self.notification_button_2.setIcon(icon6)
        self.notification_button_2.setCheckable(True)
        self.notification_button_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.notification_button_2)

        self.settings_button_2 = QPushButton(self.icon_name_widget)
        self.settings_button_2.setObjectName(u"settings_button_2")
        self.settings_button_2.setIcon(icon7)
        self.settings_button_2.setCheckable(True)
        self.settings_button_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settings_button_2)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 275, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.sign_out_button_2 = QPushButton(self.icon_name_widget)
        self.sign_out_button_2.setObjectName(u"sign_out_button_2")
        self.sign_out_button_2.setIcon(icon8)
        self.sign_out_button_2.setCheckable(True)
        self.sign_out_button_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.sign_out_button_2)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.settings_button.toggled.connect(self.settings_button_2.setChecked)
        self.notification_button.toggled.connect(self.notification_button_2.setChecked)
        self.messages_button.toggled.connect(self.messages_button_2.setChecked)
        self.profile_button.toggled.connect(self.profile_button_2.setChecked)
        self.dashboard_button.toggled.connect(self.dashboard_button_2.setChecked)
        self.dashboard_button_2.toggled.connect(self.dashboard_button.setChecked)
        self.profile_button_2.toggled.connect(self.profile_button.setChecked)
        self.messages_button_2.toggled.connect(self.messages_button.setChecked)
        self.notification_button_2.toggled.connect(self.notification_button.setChecked)
        self.settings_button_2.toggled.connect(self.settings_button.setChecked)
        self.sign_out_button.toggled.connect(MainWindow.close)
        self.sign_out_button_2.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu.setText("")
        self.pushButton_16.setText("")
        self.pushButton_14.setText("")
        self.celcius_label.setText(QCoreApplication.translate("MainWindow", u"No Location Found", None))
        self.fahrenheit_label.setText(QCoreApplication.translate("MainWindow", u"No Location Found", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Notification Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Messages Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Settings Page", None))
        self.label.setText("")
        self.dashboard_button.setText("")
        self.profile_button.setText("")
        self.messages_button.setText("")
        self.notification_button.setText("")
        self.settings_button.setText("")
        self.sign_out_button.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"FindWeather", None))
        self.dashboard_button_2.setText(QCoreApplication.translate("MainWindow", u"Celcius", None))
        self.profile_button_2.setText(QCoreApplication.translate("MainWindow", u"Fahrenheit", None))
        self.messages_button_2.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.notification_button_2.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.settings_button_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.sign_out_button_2.setText(QCoreApplication.translate("MainWindow", u"Sign out", None))
    # retranslateUi

