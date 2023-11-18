import io
from random import randint
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import QPoint


class MyPillow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton(self)
        self.btn.setText('Рисовать')
        self.btn.move(250, 400)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        r = randint(20, 100)
        qp.drawEllipse(QPoint(150, 150), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyPillow()
    w.show()
    sys.exit(app.exec())
