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
        self.lect.textEdit.setText(template.lection[0])
        self.lection = 0

        self.lect.nextButton.clicked.connect(self.UQWind)

        self.lect.testLectAction.triggered.connect(self.setTestLection)
        self.lect.fillLectAction.triggered.connect(self.setFillLection)

    def setTestLection(self):
        self.lect.textEdit.setText(template.lection[0])
        self.lection = 0

    def setFillLection(self):
        self.lect.textEdit.setText(template.lection[1])
        self.lection = 1

    def UQWind(self):
        windowQU.lection = self.lection
        windowQU.setRB()
        windowQU.show()
        window.close()

class StatsWindow(QMainWindow):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.stats = Ui_StatsWindow()
        self.stats.setupUi(self)
        self.stats.closeButton.clicked.connect(self.exit)
        self.score = 0
        self.lection = 0
        self.setlab(self.score)

    def setlab(self, score):
        self.score = score
        if self.score < 7 and self.lection == 0:
            self.stats.discriptionlabel.setText('Я конечно все понимаю, но как ты умудрился тут та проjobать?')
        elif self.score >= 7 and self.lection == 0:
            self.stats.discriptionlabel.setText('Красава, правда тут сложно облажаться')
        elif self.score < 7 and self.lection == 1:
            self.stats.discriptionlabel.setText('Все нормально, философия не такой уж и легкий предмет')
        elif self.score >= 7 and self.lection == 1:
            self.stats.discriptionlabel.setText('Красава, видать ты понимаешь эту "философию"')
        rating = 0
        if self.score < 5:
            rating = 2
        elif 5 <= self.score < 7:
            rating = 3
        elif 7 <= self.score < 9:
            rating = 4
        else:
            rating = 5

        self.stats.Schetlabel.setText(str(self.score) + '/10 | ' + str(self.score * 10) + '% | Оценка: ' + str(rating))

    def exit(self):
        self.close()

class QUWindow(QMainWindow):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.QU = Ui_QUWindow()
        self.QU.setupUi(self)
        self.score = 0
        self.quest = 0
        self.lection = 0

        self.setRB()

        self.QU.nextButton.clicked.connect(self.radioB)

    def radioB(self):
        self.checkAnswer()


    def checkAnswer(self):
        if self.QU.radioButton.isChecked():
            self.answer(template.question1[self.lection][self.quest][0][1])
        if self.QU.radioButton_2.isChecked():
            self.answer(template.question1[self.lection][self.quest][1][1])
        if self.QU.radioButton_3.isChecked():
            self.answer(template.question1[self.lection][self.quest][2][1])
        if self.QU.radioButton_4.isChecked():
            self.answer(template.question1[self.lection][self.quest][3][1])

        if self.quest + 1 != 10:
            self.quest += 1
            self.setRB()
        else:
            windowStats.lection = self.lection
            windowStats.setlab(self.score)
            windowStats.show()
            self.close()

    def answer(self, ans):
        if ans == 1:
            self.score += 1

    def setRB(self):
        if self.lection == 0:
            self.QU.QUtext.setText('Вопрос №' + str(self.quest + 1) + ' | ' + str(self.score))
        else:
            self.QU.QUtext.setText(template.qestion[self.quest])
        self.QU.radioButton.setText(template.question1[self.lection][self.quest][0][0])
        self.QU.radioButton_2.setText(template.question1[self.lection][self.quest][1][0])
        self.QU.radioButton_3.setText(template.question1[self.lection][self.quest][2][0])
        self.QU.radioButton_4.setText(template.question1[self.lection][self.quest][3][0])
        self.QU.radioButton.setChecked(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LectWindow()
    windowQU = QUWindow()
    windowStats = StatsWindow()
    window.show()
    sys.exit(app.exec_())