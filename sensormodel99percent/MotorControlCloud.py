# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MotorControl.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore as core
import os
import codecs
#from PyQt4 import QtCore, QtGui
#from PyQt4 import QtCore as core
#import rospy
#from std_msgs.msg import String
import pickle
import paho.mqtt.client as mqtt
import csv
global server_info
global writecsv,  writer,  writefile

filename = 'settings.txt'
writer=writefile={}
writecsv=False
toggleflag=False
rssi1=rssi2=rssi3=distance1=distance2=distance3=posx=posy="0"
states = ['left', 'right', 'forward', 'backward']
statecounter=0

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
def on_connect(client, userdata, flags, rc):
    print ("Connected with Code :" + str(rc))
    if rc == 0:
        # Subscribe Topic from here
        client.subscribe("rtls/#")
        # Enable Disconnect Button and Enable Others
        ui.connect_btn.setDisabled(True)
        # ui.server_add.setEnabled(False) Don't use this
        ui.server_add.setDisabled(True)
        ui.server_port.setDisabled(True)
        ui.username.setDisabled(True)
        ui.password.setDisabled(True)
        ui.disconnect_btn.setEnabled(True)
        ui.led_btn.setEnabled(True)

        ui.statusBar.setStatusTip("Connected")

# Callback Function on Receiving the Subscribed Topic/Message
def on_message( client, userdata, msg):
    # print the message received from the subscribed topic
    #print ( str(msg.payload) )
    #print ( str(len(msg.payload) ))
    parameters = (str(msg.payload)).split("$")
    #print(parameters)
    rssi1=parameters[0]
    rssi1 = rssi1.replace("b\"b\'", '')
    rssi2 = parameters[1]
    rssi3 = parameters[2]
    distance1 = parameters[3]
    distance2 = parameters[4]
    distance3 = parameters[5]
    posx = parameters[6]
    posy = parameters[7]
    ui.channel1val.setText(rssi1)
    ui.channel2val.setText(rssi2)
    ui.channel3val.setText(rssi3)
    ui.distance1.setText(distance1)
    ui.distance2.setText(distance2)
    ui.distance3.setText(distance3)
    ui.positionX.setText(posx)
    ui.positionY.setText(posy)
    if (writecsv == True):
        with open(filename, 'a') as writefile:
            writer = csv.writer(writefile)
            # writer.writerow({'RSSI1': rssi1, 'RSSI2': rssi2, 'RSSI3': rssi3,'Distance1': distance1, 'Distance2': distance2, 'Distance3': distance3, 'PosX': posx,  'PosY': posy})
            writer.writerow([rssi1, rssi2, rssi3, distance1, distance2, distance3, posx, posy])

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
    #ui.statusBar.setStatusTip("Not Connected")

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

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    # pub = rospy.Publisher('motorcontrol', String)
    def forward(self):
        str = "forward"
        client.publish("motorcontrol", str)
        # rospy.loginfo(str)
        # pub.publish(String(str))
    def backward(self):
        str = "backward"
        client.publish("motorcontrol", str)
        # rospy.loginfo(str)
        # pub.publish(String(str))
    def left(self):
        str = "left"
        client.publish("motorcontrol", str)
        # rospy.loginfo(str)
        # pub.publish(String(str))
    def right(self):
        str = "right"
        client.publish("motorcontrol", str)
        # rospy.loginfo(str)
        # pub.publish(String(str))
    def stop(self):
        str = "stop"
        client.publish("motorcontrol", str)
    def resetfunc(self):
        str = "reset"
        client.publish("motorcontrol", str)
    def autonavigate(self):
        str = "autonavigate"
        client.publish("motorcontrol", str)

        # rospy.loginfo(str)
        # pub.publish(String(str))
    def startcapture(self):
        global filename
        global writecsv, writer, writefile
        filename = 'sensorvalues'+ui.region.text()+'.csv'
        with open(filename, 'w') as writefile:

            writer = csv.DictWriter(writefile, fieldnames = ["RSSI1", "RSSI2", "RSSI3", "Distance1", "Distance2",  "Distance3",  "PosX", "PosY"])

            writer.writeheader()
            writecsv=True
            # self.timer1 = QTimer()
            # self.timer1.timeout.connect(self.stopcapture)
            # self.timer1.start(300000)
            timer1.setInterval(60000)
            timer1.timeout.connect(stopcapture)
            timer1.start()
            print("start cature")
            str = "startcapture"
            client.publish("motorcontrol", str)

        # rospy.loginfo(str)
        # pub.publish(String(str))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Forward = QtWidgets.QPushButton(self.centralwidget)
        self.Forward.setGeometry(QtCore.QRect(560, 10, 111, 51))
        self.Forward.setObjectName("Forward")
        self.Backward = QtWidgets.QPushButton(self.centralwidget)
        self.Backward.setGeometry(QtCore.QRect(560, 130, 111, 51))
        self.Backward.setObjectName("Backward")
        self.Left = QtWidgets.QPushButton(self.centralwidget)
        self.Left.setGeometry(QtCore.QRect(440, 70, 111, 51))
        self.Left.setObjectName("Left")
        self.Right = QtWidgets.QPushButton(self.centralwidget)
        self.Right.setGeometry(QtCore.QRect(680, 70, 111, 51))
        self.Right.setObjectName("Right")
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(560, 70, 111, 51))
        self.Stop.setObjectName("Stop")
        self.channel1 = QtWidgets.QLabel(self.centralwidget)
        self.channel1.setGeometry(QtCore.QRect(150, 320, 71, 21))
        self.channel1.setObjectName("channel1")
        self.RSSI = QtWidgets.QLabel(self.centralwidget)
        self.RSSI.setGeometry(QtCore.QRect(50, 270, 71, 41))
        self.RSSI.setObjectName("RSSI")
        self.Position = QtWidgets.QLabel(self.centralwidget)
        self.Position.setGeometry(QtCore.QRect(50, 470, 71, 41))
        self.Position.setObjectName("Position")
        self.sensor2 = QtWidgets.QLabel(self.centralwidget)
        self.sensor2.setGeometry(QtCore.QRect(410, 430, 71, 21))
        self.sensor2.setObjectName("sensor2")
        self.channel3val = QtWidgets.QLabel(self.centralwidget)
        self.channel3val.setGeometry(QtCore.QRect(540, 320, 71, 21))
        self.channel3val.setObjectName("channel3val")
        self.PosY = QtWidgets.QLabel(self.centralwidget) #label
        self.PosY.setGeometry(QtCore.QRect(510, 520, 91, 21))
        self.PosY.setObjectName("PosY")
        self.Distance = QtWidgets.QLabel(self.centralwidget)
        self.Distance.setGeometry(QtCore.QRect(50, 370, 71, 41))
        self.Distance.setObjectName("Distance")
        self.channel2 = QtWidgets.QLabel(self.centralwidget)
        self.channel2.setGeometry(QtCore.QRect(410, 320, 71, 21))
        self.channel2.setObjectName("channel2")
        self.channel3 = QtWidgets.QLabel(self.centralwidget)
        self.channel3.setGeometry(QtCore.QRect(630, 320, 71, 21))
        self.channel3.setObjectName("channel3")
        self.sensor3 = QtWidgets.QLabel(self.centralwidget)
        self.sensor3.setGeometry(QtCore.QRect(620, 430, 71, 21))
        self.sensor3.setObjectName("sensor3")
        self.PosX = QtWidgets.QLabel(self.centralwidget)
        self.PosX.setGeometry(QtCore.QRect(240, 520, 71, 21))
        self.PosX.setObjectName("PosX")
        self.sensor1 = QtWidgets.QLabel(self.centralwidget)
        self.sensor1.setGeometry(QtCore.QRect(140, 430, 71, 21))
        self.sensor1.setObjectName("sensor1")
        self.distance2 = QtWidgets.QLabel(self.centralwidget)
        self.distance2.setGeometry(QtCore.QRect(330, 430, 61, 21))
        self.distance2.setObjectName("distance2")
        self.positionX = QtWidgets.QLabel(self.centralwidget)
        self.positionX.setGeometry(QtCore.QRect(50, 520, 111, 21))
        self.positionX.setObjectName("positionX")
        self.distance1 = QtWidgets.QLabel(self.centralwidget)
        self.distance1.setGeometry(QtCore.QRect(50, 430, 71, 21))
        self.distance1.setObjectName("distance1")
        self.channel1val = QtWidgets.QLabel(self.centralwidget)
        self.channel1val.setGeometry(QtCore.QRect(50, 320, 71, 21))
        self.channel1val.setObjectName("channel1val")
        self.positionY = QtWidgets.QLabel(self.centralwidget)  #value
        self.positionY.setGeometry(QtCore.QRect(330, 520, 111, 21))
        self.positionY.setObjectName("positionY")
        self.distance3 = QtWidgets.QLabel(self.centralwidget)
        self.distance3.setGeometry(QtCore.QRect(540, 430, 61, 21))
        self.distance3.setObjectName("distance3")
        self.channel2val = QtWidgets.QLabel(self.centralwidget)
        self.channel2val.setGeometry(QtCore.QRect(330, 320, 61, 21))
        self.channel2val.setObjectName("channel2val")
        self.StartCapture = QtWidgets.QPushButton(self.centralwidget)
        self.StartCapture.setGeometry(QtCore.QRect(450, 210, 111, 41))
        self.StartCapture.setObjectName("StartCapture")
        self.StopCapture = QtWidgets.QPushButton(self.centralwidget)
        self.StopCapture.setGeometry(QtCore.QRect(570, 210, 91, 41))
        self.StopCapture.setObjectName("StopCapture")
        self.SaveCSV = QtWidgets.QPushButton(self.centralwidget)
        self.SaveCSV.setGeometry(QtCore.QRect(670, 210, 101, 41))
        self.SaveCSV.setObjectName("SaveCSV")
        self.server_add_lbl = QtWidgets.QLabel(self.centralwidget)
        self.server_add_lbl.setGeometry(QtCore.QRect(10, 20, 131, 21))
        self.server_add_lbl.setObjectName("server_add_lbl")
        self.username_lbl = QtWidgets.QLabel(self.centralwidget)
        self.username_lbl.setGeometry(QtCore.QRect(10, 70, 131, 21))
        self.username_lbl.setObjectName("username_lbl")
        self.server_add = QtWidgets.QLineEdit(self.centralwidget)
        self.server_add.setGeometry(QtCore.QRect(130, 10, 211, 41))
        self.server_add.setObjectName("server_add1")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(130, 60, 211, 41))
        self.username.setObjectName("username")
        self.server_port = QtWidgets.QLineEdit(self.centralwidget)
        self.server_port.setGeometry(QtCore.QRect(130, 110, 211, 41))
        self.server_port.setObjectName("server_port")
        self.password_lbl = QtWidgets.QLabel(self.centralwidget)
        self.password_lbl.setGeometry(QtCore.QRect(10, 170, 71, 21))
        self.password_lbl.setObjectName("password_lbl")
        self.server_port_lbl = QtWidgets.QLabel(self.centralwidget)
        self.server_port_lbl.setGeometry(QtCore.QRect(10, 120, 81, 21))
        self.server_port_lbl.setObjectName("server_port_lbl")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(130, 160, 211, 41))
        self.password.setObjectName("password")
        self.region = QtWidgets.QLineEdit(self.centralwidget)
        self.region.setGeometry(QtCore.QRect(350, 210, 81, 41))
        self.region.setObjectName("region")
        self.connect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.connect_btn.setGeometry(QtCore.QRect(130, 210, 91, 41))
        self.connect_btn.setObjectName("connect_btn")
        self.disconnect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.disconnect_btn.setGeometry(QtCore.QRect(250, 210, 91, 41))
        self.disconnect_btn.setObjectName("disconnect_btn")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(440, 130, 111, 41))
        self.reset.setObjectName("reset")
        self.AutoNavigate = QtWidgets.QPushButton(self.centralwidget)
        self.AutoNavigate.setGeometry(QtCore.QRect(170, 260, 111, 41))
        self.AutoNavigate.setObjectName("AutoNavigate")
        self.StartPosition = QtWidgets.QLabel(self.centralwidget)
        self.StartPosition.setGeometry(QtCore.QRect(300, 270, 91, 21))
        self.StartPosition.setObjectName("StartPosition")
        self.startpositionvalue = QtWidgets.QLabel(self.centralwidget)
        self.startpositionvalue.setGeometry(QtCore.QRect(410, 270, 31, 21))
        self.startpositionvalue.setObjectName("startpositionvalue")
        self.destinationvalue = QtWidgets.QLabel(self.centralwidget)
        self.destinationvalue.setGeometry(QtCore.QRect(560, 270, 31, 21))
        self.destinationvalue.setObjectName("destinationvalue")
        self.Destination = QtWidgets.QLabel(self.centralwidget)
        self.Destination.setGeometry(QtCore.QRect(450, 270, 91, 21))
        self.Destination.setObjectName("Destination")
        self.currentpositionvalue = QtWidgets.QLabel(self.centralwidget)
        self.currentpositionvalue.setGeometry(QtCore.QRect(740, 270, 31, 21))
        self.currentpositionvalue.setObjectName("currentpositionvalue")
        self.CurrentPosition = QtWidgets.QLabel(self.centralwidget)
        self.CurrentPosition.setGeometry(QtCore.QRect(610, 270, 111, 21))
        self.CurrentPosition.setObjectName("CurrentPosition")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Forward.clicked.connect(self.forward)
        self.Backward.clicked.connect(self.backward)
        self.Left.clicked.connect(self.left)
        self.Right.clicked.connect(self.right)
        self.Stop.clicked.connect(self.stop)
        self.StartCapture.clicked.connect(self.startcapture)
        self.StopCapture.clicked.connect(self.stopCapt)
        self.reset.clicked.connect(self.resetfunc)
        self.AutoNavigate.clicked.connect(self.autonavigate)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def stopCapt(self):
        stopcapture()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Forward.setText(_translate("MainWindow", "Forward"))
        self.Backward.setText(_translate("MainWindow", "Backward"))
        self.Left.setText(_translate("MainWindow", "Left"))
        self.Right.setText(_translate("MainWindow", "Right"))
        self.Stop.setText(_translate("MainWindow", "Stop"))
        self.channel1.setText(_translate("MainWindow", "Channel1"))
        self.RSSI.setText(_translate("MainWindow", "RSSI"))
        self.Position.setText(_translate("MainWindow", "Position"))
        self.sensor2.setText(_translate("MainWindow", "Sensor2"))
        self.channel3val.setText(_translate("MainWindow", "1"))
        self.PosY.setText(_translate("MainWindow", "PosY"))
        self.Distance.setText(_translate("MainWindow", "Distance"))
        self.channel2.setText(_translate("MainWindow", "Channel2"))
        self.channel3.setText(_translate("MainWindow", "Channel3"))
        self.sensor3.setText(_translate("MainWindow", "Sensor3"))
        self.PosX.setText(_translate("MainWindow", "PosX"))
        self.sensor1.setText(_translate("MainWindow", "Sensor1"))
        self.distance2.setText(_translate("MainWindow", "1"))
        self.positionX.setText(_translate("MainWindow", "1"))
        self.distance1.setText(_translate("MainWindow", "1"))
        self.channel1val.setText(_translate("MainWindow", "1"))
        self.positionY.setText(_translate("MainWindow", "1"))
        self.distance3.setText(_translate("MainWindow", "1"))
        self.channel2val.setText(_translate("MainWindow", "1"))
        self.StartCapture.setText(_translate("MainWindow", "Start Capture"))
        self.StopCapture.setText(_translate("MainWindow", "Stop Capture"))
        self.SaveCSV.setText(_translate("MainWindow", "Save CSV"))
        self.server_add_lbl.setText(_translate("MainWindow", "Server Address:"))
        self.username_lbl.setText(_translate("MainWindow", "UserName:"))
        self.password_lbl.setText(_translate("MainWindow", "Password:"))
        self.server_port_lbl.setText(_translate("MainWindow", "Server Port:"))
        self.connect_btn.setText(_translate("MainWindow", "Connect"))
        self.disconnect_btn.setText(_translate("MainWindow", "Disconnect"))
        self.reset.setText(_translate("MainWindow", "Reset UNO"))
        self.AutoNavigate.setText(_translate("MainWindow", "Auto Navigate"))
        self.StartPosition.setText(_translate("MainWindow", "Start Position"))
        self.startpositionvalue.setText(_translate("MainWindow", "8"))
        self.destinationvalue.setText(_translate("MainWindow", "0"))
        self.Destination.setText(_translate("MainWindow", "Destination"))
        self.currentpositionvalue.setText(_translate("MainWindow", "8"))
        self.CurrentPosition.setText(_translate("MainWindow", "Current Position"))
        self.region.setEnabled(True)
        self.region.setText("0")

        global server_info
        self.server_add.setText(server_info["Server_Address"])
        self.server_port.setText(server_info["Server_Port"])
        self.username.setText(server_info["Username"])
        self.password.setText(server_info["Password"])
        # Button Press Events
        self.connect_btn.clicked.connect(connect_with_server)
        self.disconnect_btn.clicked.connect(disconnect_with_server)

        self.server_add.editingFinished.connect(save_server_add)
        self.server_port.editingFinished.connect(save_server_port)
        self.username.editingFinished.connect(save_username)
        self.password.editingFinished.connect(save_password)


def callback(data):
    rtlsmessage = data.data
    parameters = rtlsmessage.split("$")
    #print(parameters)
    global rssi1, rssi2, rssi3, distance1, distance2, distance3, posx, posy
    global writecsv,  writer
    global filename
    rssi1=parameters[0]
    rssi2 = parameters[1]
    rssi3 = parameters[2]
    distance1 = parameters[3]
    distance2 = parameters[4]
    distance3 = parameters[5]
    posx = parameters[6]
    posy = parameters[7]
    if(writecsv == True):
         with open(filename, 'a') as writefile:
            writer = csv.writer(writefile)
            #writer.writerow({'RSSI1': rssi1, 'RSSI2': rssi2, 'RSSI3': rssi3,'Distance1': distance1, 'Distance2': distance2, 'Distance3': distance3, 'PosX': posx,  'PosY': posy})
            writer.writerow([rssi1, rssi2, rssi3, distance1, distance2, distance3, posx, posy])
    #print(rtlsmessage)

@core.pyqtSlot(name="stopcapture")
def stopcapture():
    global writecsv,  writer,  writefile
    writecsv=False
    writefile.close()
    timer1.stop()
    print("Stop capture executed")
    str = "stopcapture"
    client.publish("motorcontrol", str)


@core.pyqtSlot()
def refreshUI():
    global rssi1, rssi2, rssi3, distance1, distance2, distance3, posx, posy
    ui.channel1val.setText(rssi1)
    ui.channel2val.setText(rssi2)
    ui.channel3val.setText(rssi3)
    ui.distance1.setText(distance1)
    ui.distance2.setText(distance2)
    ui.distance3.setText(distance3)
    ui.positionX.setText(posx)
    ui.positionY.setText(posy)
    global toggleflag, states, statecounter
    if(writecsv == True):
        state = states[statecounter]
        # rospy.loginfo(state)
        # pub.publish(String(state))
        statecounter=statecounter+1
        if(statecounter>3):
            statecounter=0

       

if __name__ == "__main__":
    import sys
    
    # rospy.init_node('talker')
    # pub = rospy.Publisher('motorcontrol', String)
    # sub = rospy.Subscriber('RTLSMessage', String, callback)
    import sys

    rssi1= rssi2= rssi3= distance1= distance2= distance3= posx= posy= ""
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()



    timer = core.QTimer()
    timer1 = core.QTimer()
    timer.setInterval(1000)
    timer.timeout.connect(refreshUI)
    timer.start()
    refreshUI()
    sys.exit(app.exec_())

