import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from pyqt5_plugins.examplebuttonplugin import QtGui

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 700)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 570, 281, 81))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Git \u0438 \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u044b\u0435 \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u044c", None))
    # retranslateUi


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.setMouseTracking(True)
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.do_paint = True
        self.figure = 'circle'
        self.repaint()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        if self.do_paint and self.figure == 'circle':
            qp = QPainter()
            qp.begin(self)
            size = random.randint(10, self.width() // 4)
            qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            qp.drawEllipse(440 - size // 2, 300 - size // 2, size, size)
            qp.end()
            self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
