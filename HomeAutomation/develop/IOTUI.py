import os
import codecs
import pickle
import paho.mqtt.client as mqtt
from PyQt5 import QtCore, QtGui, QtWidgets

global server_info
global led_state
global load1_state
global load2_state
global load3_state
global load4_state

led_state = False
load1_state = False
load2_state = False
load3_state = False
load4_state = False

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
    server_info = { "Server_Address":"m12.cloudmqtt.com", \
                    "Server_Port":"14761", \
                    "Username": "hhoixidh", \
                    "Password":"jo8yv8O0-9bm"}
    save_file()
	
# Callback Function on Connection with MQTT Server
def on_connect( client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    if rc == 0:
        # Subscribe Topic from here
        client.subscribe("home/#")
        # Enable Disconnect Button and Enable Others
        ui.connect_btn.setDisabled(True)
        # ui.server_add.setEnabled(False) Don't use this
        ui.server_add.setDisabled(True)
        ui.server_port.setDisabled(True)
        ui.username.setDisabled(True)
        ui.password.setDisabled(True)
        ui.disconnect_btn.setEnabled(True)
        ui.led_btn.setEnabled(True)
        ui.load1_btn.setEnabled(True)
        ui.load2_btn.setEnabled(True)
        ui.load3_btn.setEnabled(True)
        ui.load4_btn.setEnabled(True)
        ui.statusBar.setStatusTip("Connected")

# Callback Function on Receiving the Subscribed Topic/Message
def on_message( client, userdata, msg):
    # print the message received from the subscribed topic
    #print ( str(msg.payload) )
    #print ( str(len(msg.payload) ))
    if len(msg.payload) == 5:
        message = msg.payload
        message = message.decode()      # default decoding utf-8
        temp, humidity = message.split(',')
        ui.temp.setText(temp)
        ui.humid.setText(humidity)
		
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
        
def connect_with_server():
    global server_info
    client.username_pw_set(server_info["Username"], server_info["Password"])
    client.connect(server_info["Server_Address"], int(server_info["Server_Port"]), 60)
    client.loop_start()
	
def disconnect_with_server():
    client.loop_stop()
    client.disconnect()
    # Enable Connect Button and Disable Others
    ui.connect_btn.setEnabled(True)
    ui.server_add.setEnabled(True)
    ui.server_port.setEnabled(True)
    ui.username.setEnabled(True)
    ui.password.setEnabled(True)
    ui.disconnect_btn.setDisabled(True)
    ui.led_btn.setDisabled(True)
    ui.load1_btn.setDisabled(True)
    ui.load2_btn.setDisabled(True)
    ui.load3_btn.setDisabled(True)
    ui.load4_btn.setDisabled(True)
    ui.statusBar.setStatusTip("Not Connected")

def led_state_toggle():
    global led_state
    if led_state ==  True:
        client.publish("led", '0' )
        led_state = False
        ui.led_btn.setText("Led Off")
        
    else:
        client.publish("led", '1' )
        led_state = True
        ui.led_btn.setText("Led On")
		
def load1_state_toggle():
    global load1_state
    if load1_state == True:
        client.publish("load1", '0')
        load1_state = False
        ui.load1_btn.setText("Load1 Off")
    else:
        client.publish("load1", '1')
        load1_state = True
        ui.load1_btn.setText("Load1 On")

def load2_state_toggle():
    global load2_state
    if load2_state == True:
        client.publish("load2", '0')
        load2_state = False
        ui.load2_btn.setText("Load2 Off")
    else:
        client.publish("load2", '1')
        load2_state = True
        ui.load2_btn.setText("Load2 On")

def load3_state_toggle():
    global load3_state
    if load3_state == True:
        client.publish("load3", '0')
        load3_state = False
        ui.load3_btn.setText("Load3 Off")
    else:
        client.publish("load3", '1')
        load3_state = True
        ui.load3_btn.setText("Load3 On")

def load4_state_toggle():
    global load4_state
    if load4_state == True:
        client.publish("load4", '0')
        load4_state = False
        ui.load4_btn.setText("Load4 Off")
    else:
        client.publish("load4", '1')
        load4_state = True
        ui.load4_btn.setText("Load4 On")
        
def save_server_add():
    global server_info
    server_info["Server_Address"] = ui.server_add.text()
    save_file()
    
def save_server_port():
    server_info["Server_Port"] = ui.server_port.text()
    save_file()


def save_username():
    server_info["Username"] = ui.username.text()
    save_file()


def save_password():
    server_info["Password"] = ui.password.text()
    save_file()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowOpacity(4.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.server_add = QtWidgets.QLineEdit(self.centralwidget)
        self.server_add.setGeometry(QtCore.QRect(293, 90, 211, 41))
        self.server_add.setObjectName("server_add")
        self.server_add_lbl = QtWidgets.QLabel(self.centralwidget)
        self.server_add_lbl.setGeometry(QtCore.QRect(150, 102, 131, 21))
        self.server_add_lbl.setObjectName("server_add_lbl")
        self.server_port = QtWidgets.QLineEdit(self.centralwidget)
        self.server_port.setGeometry(QtCore.QRect(293, 148, 211, 41))
        self.server_port.setObjectName("server_port")
        self.server_port_lbl = QtWidgets.QLabel(self.centralwidget)
        self.server_port_lbl.setGeometry(QtCore.QRect(150, 160, 131, 21))
        self.server_port_lbl.setObjectName("server_port_lbl")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(293, 218, 211, 41))
        self.username.setObjectName("username")
        self.username_lbl = QtWidgets.QLabel(self.centralwidget)
        self.username_lbl.setGeometry(QtCore.QRect(150, 230, 131, 21))
        self.username_lbl.setObjectName("username_lbl")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
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
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

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
		# Update Server Information
        global server_info
        self.server_add.setText(server_info["Server_Address"])
        self.server_port.setText(server_info["Server_Port"])
        self.username.setText(server_info["Username"])
        self.password.setText(server_info["Password"])
		# Button Press Events
        self.connect_btn.clicked.connect( connect_with_server )
        self.disconnect_btn.clicked.connect( disconnect_with_server )
        self.led_btn.clicked.connect( led_state_toggle )
        self.load1_btn.clicked.connect(load1_state_toggle)
        self.load2_btn.clicked.connect(load2_state_toggle)
        self.load3_btn.clicked.connect(load3_state_toggle)
        self.load4_btn.clicked.connect(load4_state_toggle)
        self.server_add.editingFinished.connect( save_server_add )
        self.server_port.editingFinished.connect( save_server_port )
        self.username.editingFinished.connect( save_username )
        self.password.editingFinished.connect( save_password )
				
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

