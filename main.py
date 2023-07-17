import sys
from gen import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import random
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Dialog()
ui.setupUi(MainWindow)
MainWindow.show()

def generate():
    ui.label_3.setText(str(random.randint(1,180)))

ui.pushButton.clicked.connect(generate)
sys.exit(app.exec_())