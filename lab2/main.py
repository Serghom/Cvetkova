from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QMessageBox, QSplashScreen, qApp, QFileDialog, QTextEdit
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5 import QtCore, QtGui
import sys
import template

from ui.WindowPy.lect import Ui_LectWindow
from ui.WindowPy.quest1 import Ui_QUWindow
from ui.WindowPy.stats import Ui_StatsWindow


class LectWindow(QMainWindow):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.lect = Ui_LectWindow()
        self.lect.setupUi(self)
        self.lect.textEdit.setText(template.lection)

        self.lect.nextButton.clicked.connect(self.UQWind)

    def UQWind(self):
        windowQU.show()
        window.close()

class StatsWindow(QMainWindow):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.stats = Ui_StatsWindow()
        self.stats.setupUi(self)
        self.stats.closeButton.clicked.connect(self.exit)
        self.score = 0
        self.setlab(self.score)

    def setlab(self, score):
        self.score = score
        if self.score < 7:
            self.stats.discriptionlabel.setText('Я конечно все понимаю, но как ты умудрился тут та проjobать?')
        else:
            self.stats.discriptionlabel.setText('Красава, правда тут сложно облажаться')

        self.stats.Schetlabel.setText(str(self.score) + '/10 | ' + str(self.score * 10) + '%')

    def exit(self):
        self.close()

class QUWindow(QMainWindow):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.QU = Ui_QUWindow()
        self.QU.setupUi(self)
        self.score = 0
        self.quest = 0

        self.setRB()

        self.QU.nextButton.clicked.connect(self.radioB)

    def radioB(self):
        self.checkAnswer()


    def checkAnswer(self):
        if self.QU.radioButton.isChecked():
            self.answer(template.question1[self.quest][0][1])
        if self.QU.radioButton_2.isChecked():
            self.answer(template.question1[self.quest][1][1])
        if self.QU.radioButton_3.isChecked():
            self.answer(template.question1[self.quest][2][1])
        if self.QU.radioButton_4.isChecked():
            self.answer(template.question1[self.quest][3][1])

        if self.quest + 1 != 10:
            self.quest += 1
            self.setRB()
        else:
            windowStats.setlab(self.score)
            windowStats.show()
            self.close()

    def answer(self, ans):
        if ans == 1:
            self.score += 1

    def setRB(self):
        self.QU.QUtext.setText('Вопрос №' + str(self.quest + 1) + ' | ' + str(self.score))
        self.QU.radioButton.setText(template.question1[self.quest][0][0])
        self.QU.radioButton_2.setText(template.question1[self.quest][1][0])
        self.QU.radioButton_3.setText(template.question1[self.quest][2][0])
        self.QU.radioButton_4.setText(template.question1[self.quest][3][0])
        self.QU.radioButton.setChecked(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LectWindow()
    windowQU = QUWindow()
    windowStats = StatsWindow()
    window.show()
    sys.exit(app.exec_())