from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QMessageBox, QSplashScreen, qApp, QFileDialog, QTextEdit
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5 import QtCore, QtGui
import sys
from ui.WindowPy.EditText import Ui_TextRedactor
# from EditText import *

# import sys
# sys.path.append("../ui/WindowPy/EditText")

class TextRedactor(QMainWindow):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.red = Ui_TextRedactor()
        self.red.setupUi(self)

        self.fileName = 'fileText/Untitle.txt'
        self.clipboard = QApplication.clipboard()

        # file
        self.red.actionNew.triggered.connect(self.clear)
        self.red.actionOpen.triggered.connect(self.openText)
        self.red.actionSave.triggered.connect(self.saveFile)
        self.red.actionSaveAs.triggered.connect(self.saveFileDialog)
        self.red.actionExit.triggered.connect(self.exitApp)

        # edit
        self.red.actionCopy.triggered.connect(self.red.textEdit.copy)
        self.red.actionPaste.triggered.connect(self.red.textEdit.paste)
        self.red.actionCut.triggered.connect(self.red.textEdit.cut)

        # help
        self.red.actionInfoProgramm.triggered.connect(self.informationProgramm)
        self.red.actionQt.triggered.connect(self.informationQt)


    def exitApp(self):
        self.close()

    def clear(self):
        # self.red.textEdit.setText('')
        self.red.textEdit.clear()
        self.saveFileDialog()


    def informationProgramm(self):
        QMessageBox.information(self, 'Мега информация о программе',
                                "Пишу тута что хочу. Но это типо инфа о проге, ок да?", QMessageBox.Ok,
                                QMessageBox.Ok)

    def informationQt(self):
        QMessageBox.information(self, 'Мега информация о QT',
                                "Пишу тута что хочу. Но это типо инфа о QT, ок да?", QMessageBox.Ok,
                                QMessageBox.Ok)

    def openText(self):
        self.red.textEdit.setText(self.openFile())

    def openFile(self):
        self.text = ''
        self.openFileNameDialog()
        self.file = open(self.fileName)
        for t in self.file:
            self.text += t
        self.file.close()
        return self.text

    def saveFile(self):
        self.text = self.red.textEdit.toPlainText()
        with open(self.fileName, 'a') as f:
            f.write(self.text)
        # with open(self.fileName[:-4:] + 'New.txt', 'a') as f:
        #     f.write(self.text)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self, "Открыть", "",
                                              "All Files (*);;Text Files (*.txt)", options=options)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getSaveFileName(self, "Сохранить как...", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if self.fileName:
            # print(fileName)
            self.text = self.red.textEdit.toPlainText()
            with open(self.fileName, 'a') as f:
                f.write(self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextRedactor()
    window.show()
    sys.exit(app.exec_())