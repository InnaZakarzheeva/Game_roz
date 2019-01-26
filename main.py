import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
    QPushButton, QDesktopWidget, QMainWindow, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication 

class Window(QMainWindow):
    def __init__(self):
        super().__init__() #Функция super() возвращает
        #родительский объект Example с классом, и мы вызываем его конструктор.
        self.initUI()

    def initUI(self):
        lb1=QLabel('P-Junior',self)
        lb1.move(350,100)
        #створення кнопки "старт"
        qbtn=QPushButton('Старт', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(350, 300) #розміщення кнопки
        #створення вікна і його розміщення на екрані
        self.resize(800,600)
        self.center()
        self.setWindowTitle('P-Junior')
        self.setWindowIcon(QIcon('лого.png'))
        self.show()
        self.show()
        

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__=='__main__':
    app=QApplication(sys.argv) #список аргументів командного рядка
    ex=Window()
    sys.exit(app.exec_())
