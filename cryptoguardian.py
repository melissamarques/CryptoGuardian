import os
import sys
import random
import string
from cryptography.fernet import Fernet
from PyQt5 import QtCore, QtGui, QtWidgets

class CryptoGuardian(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 419)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 130, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 200, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 30, 191, 41))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 576, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.encrypt_file)
        self.pushButton_2.clicked.connect(self.decrypt_file)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CryptoGuardian"))
        self.pushButton.setText(_translate("MainWindow", "Criptografar"))
        self.pushButton_2.setText(_translate("MainWindow", "Descriptografar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">CryptoGuardian</span></p></body></html>"))

    def generate_random_password(self, length=16):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(caracteres) for _ in range(length))

    def encrypt_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Selecione um arquivo para criptografar", "", "Todos os arquivos (*)")
        if file_path:
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)

            with open(file_path, 'rb') as file:
                file_data = file.read()

            encrypted_data = cipher_suite.encrypt(file_data)

            encrypted_file_path = file_path + '.encrypted'
            with open(encrypted_file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)

            self.copy_password_to_clipboard(key)
            self.show_message(f'Arquivo criptografado: {encrypted_file_path}', "Senha de criptografia copiada para a área de transferência.")

    def copy_password_to_clipboard(self, password):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(password.decode())

    def decrypt_file(self):
        encrypted_file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Selecione um arquivo para descriptografar", "", "Encrypted Files (*.encrypted)")
        if encrypted_file_path:
            senha_usuario, ok = QtWidgets.QInputDialog.getText(None, "Senha", "Digite a senha de descriptografia:")
            if ok:
                key = senha_usuario.encode()

                cipher_suite = Fernet(key)

                with open(encrypted_file_path, 'rb') as encrypted_file:
                    encrypted_data = encrypted_file.read()

                decrypted_data = cipher_suite.decrypt(encrypted_data)

                decrypted_file_path = encrypted_file_path.replace('.encrypted', '.decrypted')
                with open(decrypted_file_path, 'wb') as decrypted_file:
                    decrypted_file.write(decrypted_data)

                self.show_message(f'Arquivo descriptografado: {decrypted_file_path}', "")

    def show_message(self, message, password):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("CryptoGuardian")
        if password:
            msg.setInformativeText(password)
        msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CryptoGuardian()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
