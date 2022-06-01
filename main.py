import os
from PyQt5 import QtGui, uic, QtCore, QtWidgets
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from functools import partial

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "ui/main.ui"))

class MainWidget(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
  
		buttons = (self.loginbutton,self.customerbutton)
		for i, button in enumerate(buttons):
			button.clicked.connect(partial(self.stackedWidget.setCurrentIndex, i))

if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle("Breeze")		
	w = MainWidget()
	w.show()
	sys.exit(app.exec_())
