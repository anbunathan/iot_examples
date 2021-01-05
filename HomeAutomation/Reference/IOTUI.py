import os
import codecs
import pickle
import paho.mqtt.client as mqtt
from PyQt5 import QtCore, QtGui, QtWidgets

filename = 'settings.txt'
def save_file():
    with open(filename, "wb") as myFile:
        pickle.dump(server_info, myFile)
if os.path.exists(filename):
    # Read Dictionary from this file
    with open(filename, "rb") as myFile:
        server_info = pickle.load(myFile)
else:
    # Create Dictionary Using Default parameters
    server_info = { "Server_Address":"m14.cloudmqtt.com", \
                    "Server_Port":"18410", \
                    "Username": "setsmjwc", \
                    "Password":"apDnKqHRgAjA"}
    save_file()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowOpacity(4.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.server_add = QtWidgets.QTextEdit(self.centralwidget)
        self.server_add.setGeometry(QtCore.QRect(293, 90, 211, 41))
        self.server_add.setObjectName("server_add")
        self.server_add_lbl = QtWidgets.QLabel(self.centralwidget)
        self.server_add_lbl.setGeometry(QtCore.QRect(150, 102, 131, 21))
        self.server_add_lbl.setObjectName("server_add_lbl")
        self.server_port = QtWidgets.QTextEdit(self.centralwidget)
        self.server_port.setGeometry(QtCore.QRect(293, 148, 211, 41))
        self.server_port.setObjectName("server_port")
        self.server_port_lbl = QtWidgets.QLabel(self.centralwidget)
        self.server_port_lbl.setGeometry(QtCore.QRect(150, 160, 131, 21))
        self.server_port_lbl.setObjectName("server_port_lbl")
        self.username = QtWidgets.QTextEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(293, 218, 211, 41))
        self.username.setObjectName("username")
        self.username_lbl = QtWidgets.QLabel(self.centralwidget)
        self.username_lbl.setGeometry(QtCore.QRect(150, 230, 131, 21))
        self.username_lbl.setObjectName("username_lbl")
        self.password = QtWidgets.QTextEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(293, 278, 211, 41))
        self.password.setObjectName("password")
        self.password_lbl = QtWidgets.QLabel(self.centralwidget)
        self.password_lbl.setGeometry(QtCore.QRect(150, 290, 131, 21))
        self.password_lbl.setObjectName("password_lbl")
        self.temp_lbl = QtWidgets.QLabel(self.centralwidget)
        self.temp_lbl.setGeometry(QtCore.QRect(140, 360, 71, 41))
        self.temp_lbl.setObjectName("temp_lbl")
        self.humid_lbl = QtWidgets.QLabel(self.centralwidget)
        self.humid_lbl.setGeometry(QtCore.QRect(310, 360, 71, 41))
        self.humid_lbl.setObjectName("humid_lbl")
        self.connect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.connect_btn.setGeometry(QtCore.QRect(540, 100, 91, 41))
        self.connect_btn.setObjectName("connect_btn")
        self.disconnect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.disconnect_btn.setGeometry(QtCore.QRect(540, 220, 91, 41))
        self.disconnect_btn.setObjectName("disconnect_btn")
        self.led_btn = QtWidgets.QPushButton(self.centralwidget)
        self.led_btn.setGeometry(QtCore.QRect(540, 390, 91, 41))
        self.led_btn.setObjectName("led_btn")
        self.load1_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load1_btn.setGeometry(QtCore.QRect(130, 500, 101, 31))
        self.load1_btn.setObjectName("load1_btn")
        self.load2_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load2_btn.setGeometry(QtCore.QRect(260, 500, 101, 31))
        self.load2_btn.setObjectName("load2_btn")
        self.load4_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load4_btn.setGeometry(QtCore.QRect(530, 500, 101, 31))
        self.load4_btn.setObjectName("load4_btn")
        self.load3_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load3_btn.setGeometry(QtCore.QRect(400, 500, 101, 31))
        self.load3_btn.setObjectName("load3_btn")
        self.temp = QtWidgets.QLabel(self.centralwidget)
        self.temp.setGeometry(QtCore.QRect(140, 410, 31, 21))
        self.temp.setObjectName("temp")
        self.c_lbl = QtWidgets.QLabel(self.centralwidget)
        self.c_lbl.setGeometry(QtCore.QRect(190, 410, 31, 21))
        self.c_lbl.setObjectName("c_lbl")
        self.percent_lbl = QtWidgets.QLabel(self.centralwidget)
        self.percent_lbl.setGeometry(QtCore.QRect(350, 410, 31, 21))
        self.percent_lbl.setObjectName("percent_lbl")
        self.humid = QtWidgets.QLabel(self.centralwidget)
        self.humid.setGeometry(QtCore.QRect(300, 410, 31, 21))
        self.humid.setObjectName("humid")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IOT"))
        self.server_add_lbl.setText(_translate("MainWindow", "Server Address:"))
        self.server_port_lbl.setText(_translate("MainWindow", "Server Port:"))
        self.username_lbl.setText(_translate("MainWindow", "UserName:"))
        self.password_lbl.setText(_translate("MainWindow", "Password:"))
        self.temp_lbl.setText(_translate("MainWindow", "Temperature"))
        self.humid_lbl.setText(_translate("MainWindow", "Humidity"))
        self.connect_btn.setText(_translate("MainWindow", "Connect"))
        self.disconnect_btn.setText(_translate("MainWindow", "Disconnect"))
        self.led_btn.setText(_translate("MainWindow", "LED On/Off"))
        self.load1_btn.setText(_translate("MainWindow", "Load1 Off"))
        self.load2_btn.setText(_translate("MainWindow", "Load2 Off"))
        self.load4_btn.setText(_translate("MainWindow", "Load4 Off"))
        self.load3_btn.setText(_translate("MainWindow", "Load3 Off"))
        self.temp.setText(_translate("MainWindow", "24"))
        self.c_lbl.setText(_translate("MainWindow", "C"))
        self.percent_lbl.setText(_translate("MainWindow", "%"))
        self.humid.setText(_translate("MainWindow", "56"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

