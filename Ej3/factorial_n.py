# Rosas Palacios Alan

import sys
from PyQt5 import QtWidgets, QtGui, uic

#Cargar nuestro archivo .ui
form_class = uic.loadUiType("factorial_n.ui")[0]

class MyWindowClass(QtWidgets.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.btn_siguiente.clicked.connect(self.btn_siguiente_clicked)
		self.text_n.setText(str(0))
		self.text_factorial.setText(str(0))

	#evento del boton boton_siguiente
	#sumo 1 a n
	def btn_siguiente_clicked(self):
		var_creciente = int(self.text_n.text()) + 1 
		self.text_n.setText (str(var_creciente))
		#realizo el factorial
		var_factorial = 1 
		for a in range (1 , int(self.text_n.text())):
			var_factorial = var_factorial * (a+1)
		self.text_factorial.setText (str(var_factorial))



app = QtWidgets.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
