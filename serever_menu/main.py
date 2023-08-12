# -*- coding: utf-8 -*-
from License import Ui_License # Это наш конвертированный файл дизайна
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QProxyStyle, QStyle, QMessageBox, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QMovie
import random



class MyProxyStyle(QProxyStyle):
    def pixelMetric(self, QStyle_PixelMetric, option=None, widget=None):

        if QStyle_PixelMetric == QStyle.PM_SmallIconSize:
            return 24
        else:
            return QProxyStyle.pixelMetric(self, QStyle_PixelMetric, option, widget)

class LicenseApp(QtWidgets.QMainWindow, Ui_License):
    def __init__(self):
        super().__init__()
        self.file = None
        self.ui = Ui_License()
        self.ui.setupUi(self)

        self.ui.pushButton_key.clicked.connect(self.generator_key)

    def generator_key(self):
        password_length = 8
        characters = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

        pass_old = []

        k1 = ""
        k2 = ""
        k3 = ""
        k4 = ""

        for index in range(int(password_length)):
            k1 += random.choice(characters)
        for index in range(int(password_length)):
            k2 += random.choice(characters)
        for index in range(int(password_length)):
            k3 += random.choice(characters)
        for index in range(int(password_length)):
            k4 += random.choice(characters)
        pass_now = k1 + "-" + k2 + "-" + k3 + "-" + k4
        self.ui.lineEdit_key.setText(pass_now)
        # print("Password generated: " + k1 + "-" + k2 + "-" + k3 + "-" + k4)

        for pas in pass_old:
            if pas in pass_old:
                print(f"Уже есть такой пароль:  + {pas}")
                print
            else:
                pass_old.append(pass_now)
                print(pas)



if __name__ == '__main__':
    import sys  # sys нужен для передачи argv в QApplication
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = LicenseApp()  # Создаём объект класса Activation
    myStyle = MyProxyStyle('Fusion')
    app.setStyle(myStyle)
    window.show()  # Показываем окно активации
    sys.exit(app.exec())  # и запускаем приложение