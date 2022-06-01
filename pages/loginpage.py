import os
from PyQt5 import QtGui, uic
import ctypes

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from .customerpage import CustomerWidget

current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, "../ui/login.ui"))

class LoginWidget(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_test.clicked.connect(self.test)
        self.lineEdit_server.setText("localhost")

        
    def test(self):
        try:
            return CustomerWidget.test_func(self.lineEdit_server.text())
        except Exception as e:
            print(e)
            pass
                
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    w = LoginWidget()
    w.show()
    sys.exit(app.exec_())
