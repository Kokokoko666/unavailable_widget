# unavailable_widget

What is a proper way to refer to widget class to access object in other module, when it is linked to UI file in PYQT5? 

Unfortunately, calling the widget class "CustomerWidget" shows an error "type object 'CustomerWidget' has no attribute 'lineEdit_cust_name'",
calling widget class "CustomerWidget()" shows an error "wrapped C/C++ object of type QLineEdit has been deleted".
Calling widget class "CustomerWidget().parent()." shows an error "'NoneType' object has no attribute 'lineEdit_cust_name'" and finally
calling the widget class "CustomerWidget.parent()." yeilds an error "parent(self): first argument of unbound method must have type 'QObject'".

