import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen

from PyQt5.QtCore import Qt

from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.make)
        self.check = False

    def make(self):
        self.check = True
        self.update()
        print('click')

    def paintEvent(self, event):
        if self.check:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.yellow, 15, Qt.SolidLine))
            n = randint(200, 500)
            painter.drawEllipse(640 - int(n / 2) - 100, 310 - int(n / 2), n, n)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
