# unavailable_widget

Firstly, big thanks to @eylannesc and the fantastic job he does on Stackoverflow helping others with PYQT inquiries. 

The code comes from this inquiry on Stackoverflow:

https://stackoverflow.com/questions/53899209/load-whole-ui-file-in-an-frame-widget-of-another-ui-file

and the complete code is available on @eyllanesc Github:

https://github.com/eyllanesc/stackoverflow/tree/master/questions/53899209

What is a proper way to refer to widget class to access object in other module, when it is linked to UI file in PYQT5? 

Unfortunately, calling the widget class "CustomerWidget" shows an error "type object 'CustomerWidget' has no attribute 'lineEdit_cust_name'",<br>
calling widget class "CustomerWidget()" shows an error "wrapped C/C++ object of type QLineEdit has been deleted".<br>
Calling widget class "CustomerWidget().parent()." shows an error "'NoneType' object has no attribute 'lineEdit_cust_name'" and finally<br>
calling the widget class "CustomerWidget.parent()." yeilds an error "parent(self): first argument of unbound method must have type 'QObject'".<br>

