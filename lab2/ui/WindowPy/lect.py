# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lect.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LectWindow(object):
    def setupUi(self, LectWindow):
        LectWindow.setObjectName("LectWindow")
        LectWindow.resize(751, 454)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LectWindow.sizePolicy().hasHeightForWidth())
        LectWindow.setSizePolicy(sizePolicy)
        LectWindow.setMinimumSize(QtCore.QSize(751, 454))
        LectWindow.setMaximumSize(QtCore.QSize(751, 454))
        self.centralwidget = QtWidgets.QWidget(LectWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 0, 731, 401))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(484, 400, 261, 23))
        self.nextButton.setObjectName("nextButton")
        LectWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LectWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        LectWindow.setMenuBar(self.menubar)
        self.testLectAction = QtWidgets.QAction(LectWindow)
        self.testLectAction.setObjectName("testLectAction")
        self.fillLectAction = QtWidgets.QAction(LectWindow)
        self.fillLectAction.setObjectName("fillLectAction")
        self.menu.addAction(self.testLectAction)
        self.menu.addAction(self.fillLectAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(LectWindow)
        QtCore.QMetaObject.connectSlotsByName(LectWindow)

    def retranslateUi(self, LectWindow):
        _translate = QtCore.QCoreApplication.translate
        LectWindow.setWindowTitle(_translate("LectWindow", "Типо лекция"))
        self.nextButton.setText(_translate("LectWindow", "Приступить к тесту"))
        self.menu.setTitle(_translate("LectWindow", "Лекции"))
        self.testLectAction.setText(_translate("LectWindow", "Тестовая Лекция"))
        self.fillLectAction.setText(_translate("LectWindow", "Философия"))

