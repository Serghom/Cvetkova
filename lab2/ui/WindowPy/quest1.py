# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quest1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QUWindow(object):
    def setupUi(self, QUWindow):
        QUWindow.setObjectName("QUWindow")
        QUWindow.resize(800, 357)
        QUWindow.setMinimumSize(QtCore.QSize(800, 357))
        QUWindow.setMaximumSize(QtCore.QSize(800, 357))
        self.centralwidget = QtWidgets.QWidget(QUWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.QUtext = QtWidgets.QTextEdit(self.centralwidget)
        self.QUtext.setGeometry(QtCore.QRect(10, 10, 781, 91))
        self.QUtext.setMinimumSize(QtCore.QSize(781, 91))
        self.QUtext.setMaximumSize(QtCore.QSize(781, 91))
        self.QUtext.setReadOnly(True)
        self.QUtext.setObjectName("QUtext")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(720, 310, 75, 23))
        self.nextButton.setObjectName("nextButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 140, 781, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        QUWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QUWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        QUWindow.setMenuBar(self.menubar)

        self.retranslateUi(QUWindow)
        QtCore.QMetaObject.connectSlotsByName(QUWindow)

    def retranslateUi(self, QUWindow):
        _translate = QtCore.QCoreApplication.translate
        QUWindow.setWindowTitle(_translate("QUWindow", "типо вопросы"))
        self.nextButton.setText(_translate("QUWindow", "Дальше"))
        self.radioButton.setText(_translate("QUWindow", "RadioButton"))
        self.radioButton_2.setText(_translate("QUWindow", "RadioButton"))
        self.radioButton_3.setText(_translate("QUWindow", "RadioButton"))
        self.radioButton_4.setText(_translate("QUWindow", "RadioButton"))

