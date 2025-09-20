#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from Dialogs.dialogs import message, FileDialog
import tools.crypt as crp


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main_window.ui', self)

        # Подключаем сигналы и слоты
        self.radioDehash.toggled.connect(self.on_radioDehash_toggled)
        self.mn_font.triggered.connect(self.mn_font_choose)
        self.mn_quit.triggered.connect(self.mn_exit)
        self.mn_clear.triggered.connect(self.clear_all)
        self.btn_hash.clicked.connect(self.btnHash)

    def on_radioDehash_toggled(self):
        self.lineEdit_3.setEnabled(not self.radioDehash.isChecked())
        
    def mn_font_choose(self):
        font_open = FileDialog()
        fsize = font_open.font_dialog()
        if fsize:
            self.lineEdit.setFont(fsize)
            self.lineEdit_2.setFont(fsize)
            self.lineEdit_3.setFont(fsize)
            self.textEdit.setFont(fsize)
            
    def mn_exit(self):
        sys.exit()

        
    def clear_all(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.textEdit.clear()


    def btnHash(self):
        if not self.lineEdit.text() and not self.lineEdit_2.text():
            message('', 'Строка/Пароль..', 'Не заполнено поле для шифрования \n или поле пароля!..')
            return
        # Пока криптуем.
        str_str = self.lineEdit.text()
        pas_str = self.lineEdit_2.text()
        if self.radioHash.isChecked():
            if pas_str == self.lineEdit_3.text():
                self.textEdit.append(crp.encrypt_string(pas_str, str_str))
            else:
                message('', 'Ошибка шифрования', 'Не указано подтверждение пароля!')
                return
        if self.radioDehash.isChecked():
            self.textEdit.append(crp.decrypt_string(pas_str, str_str))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
