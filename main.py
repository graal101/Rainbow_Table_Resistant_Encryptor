#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main_window.ui', self)

        # Подключаем сигналы и слоты
        # self.pushButton.clicked.connect(self.on_button_click)

    # def on_button_click(self):
        # print("Кнопка нажата!") 



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
