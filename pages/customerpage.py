
from PyQt5 import QtGui, uic
from PyQt5.QtCore import QSize, Qt, QSortFilterProxyModel
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtWidgets import (
	QApplication,
	QLabel,
	QLineEdit,
	QMainWindow,
	QWidget,
	QMessageBox
)

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "../ui/customer.ui"))


class CustomerWidget(Base, Form):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__(parent)
		self.setupUi(self)
		self.lineEdit_cust_name.setText("")

	def test_func(name):
		print(name)
		CustomerWidget.parent().lineEdit_cust_name.setText(name)

if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	w = CustomerWidget()
	w.show()
	sys.exit(app.exec_())
