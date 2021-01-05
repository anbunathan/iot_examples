# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeAutomation.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(306, 231)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.connect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.connect_btn.setGeometry(QtCore.QRect(220, 10, 75, 31))
        self.connect_btn.setObjectName("connect_btn")
        self.disconnect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.disconnect_btn.setEnabled(False)
        self.disconnect_btn.setGeometry(QtCore.QRect(220, 70, 75, 31))
        self.disconnect_btn.setObjectName("disconnect_btn")
        self.temp_lbl = QtWidgets.QLabel(self.centralwidget)
        self.temp_lbl.setGeometry(QtCore.QRect(10, 120, 69, 18))
        self.temp_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.temp_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_lbl.setObjectName("temp_lbl")
        self.humid_lbl = QtWidgets.QLabel(self.centralwidget)
        self.humid_lbl.setGeometry(QtCore.QRect(110, 120, 69, 18))
        self.humid_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.humid_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.humid_lbl.setObjectName("humid_lbl")
        self.temp = QtWidgets.QLabel(self.centralwidget)
        self.temp.setGeometry(QtCore.QRect(10, 140, 31, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.temp.setFont(font)
        self.temp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.temp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temp.setObjectName("temp")
        self.c_lbl = QtWidgets.QLabel(self.centralwidget)
        self.c_lbl.setGeometry(QtCore.QRect(50, 140, 21, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.c_lbl.setFont(font)
        self.c_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.c_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.c_lbl.setObjectName("c_lbl")
        self.humidity = QtWidgets.QLabel(self.centralwidget)
        self.humidity.setGeometry(QtCore.QRect(110, 140, 31, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.humidity.setFont(font)
        self.humidity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.humidity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.humidity.setObjectName("humidity")
        self.percent_lbl = QtWidgets.QLabel(self.centralwidget)
        self.percent_lbl.setGeometry(QtCore.QRect(150, 140, 21, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.percent_lbl.setFont(font)
        self.percent_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.percent_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.percent_lbl.setObjectName("percent_lbl")
        self.led_btn = QtWidgets.QPushButton(self.centralwidget)
        self.led_btn.setEnabled(False)
        self.led_btn.setGeometry(QtCore.QRect(220, 110, 71, 51))
        self.led_btn.setObjectName("led_btn")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 71, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.server_add_lbl = QtWidgets.QLabel(self.layoutWidget)
        self.server_add_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.server_add_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.server_add_lbl.setObjectName("server_add_lbl")
        self.verticalLayout.addWidget(self.server_add_lbl)
        self.server_port_lbl = QtWidgets.QLabel(self.layoutWidget)
        self.server_port_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.server_port_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.server_port_lbl.setObjectName("server_port_lbl")
        self.verticalLayout.addWidget(self.server_port_lbl)
        self.username_lbl = QtWidgets.QLabel(self.layoutWidget)
        self.username_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.username_lbl.setObjectName("username_lbl")
        self.verticalLayout.addWidget(self.username_lbl)
        self.password_lbl = QtWidgets.QLabel(self.layoutWidget)
        self.password_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.password_lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_lbl.setObjectName("password_lbl")
        self.verticalLayout.addWidget(self.password_lbl)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 10, 111, 100))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.server_add = QtWidgets.QLineEdit(self.layoutWidget1)
        self.server_add.setMaxLength(30)
        self.server_add.setObjectName("server_add")
        self.verticalLayout_2.addWidget(self.server_add)
        self.server_port = QtWidgets.QLineEdit(self.layoutWidget1)
        self.server_port.setMaxLength(30)
        self.server_port.setObjectName("server_port")
        self.verticalLayout_2.addWidget(self.server_port)
        self.username = QtWidgets.QLineEdit(self.layoutWidget1)
        self.username.setMaxLength(30)
        self.username.setObjectName("username")
        self.verticalLayout_2.addWidget(self.username)
        self.password = QtWidgets.QLineEdit(self.layoutWidget1)
        self.password.setMaxLength(30)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout_2.addWidget(self.password)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 170, 281, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.load1_btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.load1_btn.setEnabled(False)
        self.load1_btn.setObjectName("load1_btn")
        self.horizontalLayout.addWidget(self.load1_btn)
        self.load2_btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.load2_btn.setEnabled(False)
        self.load2_btn.setObjectName("load2_btn")
        self.horizontalLayout.addWidget(self.load2_btn)
        self.load3_btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.load3_btn.setEnabled(False)
        self.load3_btn.setObjectName("load3_btn")
        self.horizontalLayout.addWidget(self.load3_btn)
        self.load4_btn = QtWidgets.QPushButton(self.layoutWidget2)
        self.load4_btn.setEnabled(False)
        self.load4_btn.setObjectName("load4_btn")
        self.horizontalLayout.addWidget(self.load4_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather Monitor"))
        self.connect_btn.setText(_translate("MainWindow", "Connect"))
        self.disconnect_btn.setText(_translate("MainWindow", "Disconnect"))
        self.temp_lbl.setText(_translate("MainWindow", "Temperature"))
        self.humid_lbl.setText(_translate("MainWindow", "Humidity"))
        self.temp.setText(_translate("MainWindow", "0"))
        self.c_lbl.setText(_translate("MainWindow", "C"))
        self.humidity.setText(_translate("MainWindow", "0"))
        self.percent_lbl.setText(_translate("MainWindow", "%"))
        self.led_btn.setText(_translate("MainWindow", "Led OFF"))
        self.server_add_lbl.setText(_translate("MainWindow", "Server Add :"))
        self.server_port_lbl.setText(_translate("MainWindow", "Server Port :"))
        self.username_lbl.setText(_translate("MainWindow", "Username :"))
        self.password_lbl.setText(_translate("MainWindow", "Password :"))
        self.load1_btn.setText(_translate("MainWindow", "Load1 Off"))
        self.load2_btn.setText(_translate("MainWindow", "Load2 Off"))
        self.load3_btn.setText(_translate("MainWindow", "Load3 Off"))
        self.load4_btn.setText(_translate("MainWindow", "Led OFF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

