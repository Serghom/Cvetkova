# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stats.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatsWindow(object):
    def setupUi(self, StatsWindow):
        StatsWindow.setObjectName("StatsWindow")
        StatsWindow.resize(185, 133)
        self.centralwidget = QtWidgets.QWidget(StatsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.discriptionlabel = QtWidgets.QLabel(self.centralwidget)
        self.discriptionlabel.setObjectName("discriptionlabel")
        self.verticalLayout.addWidget(self.discriptionlabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Privillabel = QtWidgets.QLabel(self.centralwidget)
        self.Privillabel.setObjectName("Privillabel")
        self.horizontalLayout.addWidget(self.Privillabel)
        self.Schetlabel = QtWidgets.QLabel(self.centralwidget)
        self.Schetlabel.setObjectName("Schetlabel")
        self.horizontalLayout.addWidget(self.Schetlabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)
        StatsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StatsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 185, 21))
        self.menubar.setObjectName("menubar")
        StatsWindow.setMenuBar(self.menubar)

        self.retranslateUi(StatsWindow)
        QtCore.QMetaObject.connectSlotsByName(StatsWindow)

    def retranslateUi(self, StatsWindow):
        _translate = QtCore.QCoreApplication.translate
        StatsWindow.setWindowTitle(_translate("StatsWindow", "Типо статистика"))
        self.discriptionlabel.setText(_translate("StatsWindow", "TextLabel"))
        self.Privillabel.setText(_translate("StatsWindow", "Правильность:"))
        self.Schetlabel.setText(_translate("StatsWindow", "TextLabel"))
        self.closeButton.setText(_translate("StatsWindow", "Закрыть"))

