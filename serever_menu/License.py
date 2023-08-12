# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'License.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_License(object):
    def setupUi(self, License):
        if not License.objectName():
            License.setObjectName(u"License")
        License.resize(700, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(License.sizePolicy().hasHeightForWidth())
        License.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(License)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 681, 561))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 450, 99))
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(450, 0))
        self.groupBox.setMaximumSize(QSize(450, 16777215))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_key = QPushButton(self.groupBox)
        self.pushButton_key.setObjectName(u"pushButton_key")
        sizePolicy.setHeightForWidth(self.pushButton_key.sizePolicy().hasHeightForWidth())
        self.pushButton_key.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.pushButton_key.setFont(font1)
        self.pushButton_key.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.horizontalLayout.addWidget(self.pushButton_key)

        self.lineEdit_key = QLineEdit(self.groupBox)
        self.lineEdit_key.setObjectName(u"lineEdit_key")
        sizePolicy.setHeightForWidth(self.lineEdit_key.sizePolicy().hasHeightForWidth())
        self.lineEdit_key.setSizePolicy(sizePolicy)
        self.lineEdit_key.setMinimumSize(QSize(325, 0))
        self.lineEdit_key.setMaximumSize(QSize(330, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        self.lineEdit_key.setFont(font2)
        self.lineEdit_key.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_key.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"color: rgb(0, 85, 255);")
        self.lineEdit_key.setEchoMode(QLineEdit.Normal)
        self.lineEdit_key.setDragEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit_key)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        License.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(License)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 22))
        License.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(License)
        self.statusbar.setObjectName(u"statusbar")
        License.setStatusBar(self.statusbar)

        self.retranslateUi(License)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(License)
    # setupUi

    def retranslateUi(self, License):
        License.setWindowTitle(QCoreApplication.translate("License", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("License", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u043a\u043b\u044e\u0447\u0435\u0439", None))
        self.pushButton_key.setText(QCoreApplication.translate("License", u"\u041a\u043b\u044e\u0447", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_key.setToolTip(QCoreApplication.translate("License", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_key.setWhatsThis(QCoreApplication.translate("License", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_key.setText(QCoreApplication.translate("License", u"XXXXXXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("License", u"\u041b\u0438\u0446\u0435\u043d\u0437\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("License", u"\u0411\u0414", None))
    # retranslateUi

