# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\87211\Desktop\DL_P\project_1\search_route.ui'
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
        self.route2main = QtWidgets.QPushButton(self.centralwidget)
        self.route2main.setGeometry(QtCore.QRect(100, 90, 181, 111))
        self.route2main.setObjectName("route2main")
        self.line_route = QtWidgets.QLineEdit(self.centralwidget)
        self.line_route.setGeometry(QtCore.QRect(200, 380, 601, 61))
        self.line_route.setObjectName("line_route")
        self.search_route = QtWidgets.QPushButton(self.centralwidget)
        self.search_route.setGeometry(QtCore.QRect(890, 370, 141, 81))
        self.search_route.setObjectName("search_route")
        self.empty_warn = QtWidgets.QLabel(self.centralwidget)
        self.empty_warn.setGeometry(QtCore.QRect(420, 480, 491, 31))
        self.empty_warn.setObjectName("empty_warn")
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
        self.route2main.setText(_translate("MainWindow", "返回主菜单"))
        self.search_route.setText(_translate("MainWindow", "查询"))
        self.empty_warn.setText(_translate("MainWindow", "TextLabel"))