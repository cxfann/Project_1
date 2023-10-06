# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\87211\Desktop\DL_P\project_1\search_station.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1136, 797)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.station2main = QtWidgets.QPushButton(self.centralwidget)
        self.station2main.setGeometry(QtCore.QRect(440, 570, 261, 111))
        font = QtGui.QFont()
        font.setFamily("霞鹜文楷")
        font.setPointSize(20)
        self.station2main.setFont(font)
        self.station2main.setObjectName("station2main")
        self.line_station = QtWidgets.QLineEdit(self.centralwidget)
        self.line_station.setGeometry(QtCore.QRect(440, 330, 421, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.line_station.setFont(font)
        self.line_station.setObjectName("line_station")
        self.search_station = QtWidgets.QPushButton(self.centralwidget)
        self.search_station.setGeometry(QtCore.QRect(900, 330, 151, 91))
        font = QtGui.QFont()
        font.setFamily("霞鹜文楷")
        font.setPointSize(20)
        self.search_station.setFont(font)
        self.search_station.setObjectName("search_station")
        self.empty_warn = QtWidgets.QLabel(self.centralwidget)
        self.empty_warn.setGeometry(QtCore.QRect(600, 440, 511, 81))
        font = QtGui.QFont()
        font.setFamily("霞鹜文楷")
        font.setPointSize(12)
        font.setUnderline(True)
        self.empty_warn.setFont(font)
        self.empty_warn.setObjectName("empty_warn")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 0, 361, 741))
        self.listView.setStyleSheet("background-image: url(\"C:background.jpg\")")
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 60, 431, 81))
        self.label.setStyleSheet("font: 28pt \"霞鹜文楷\";\n"
"text-decoration: underline;")
        self.label.setObjectName("label")
        self.listView.raise_()
        self.station2main.raise_()
        self.line_station.raise_()
        self.search_station.raise_()
        self.empty_warn.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1136, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.station2main.setText(_translate("MainWindow", "返回主菜单"))
        self.search_station.setText(_translate("MainWindow", "查询"))
        self.empty_warn.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "查找公交站点"))
