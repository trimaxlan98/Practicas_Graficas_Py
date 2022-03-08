# Rosas Palacios Alan

import sys
from PyQt5 import QtWidgets, QtGui, uic

#Cargar nuestro archivo .ui
form_class = uic.loadUiType("contador.ui")[0]

class MyWindowClass(QtWidgets.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.btn_mas.clicked.connect(self.btn_mas_clicked)
		self.btn_menos.clicked.connect(self.btn_menos_clicked)
		self.btn_reset.clicked.connect(self.btn_reset_clicked)
		self.text_contador.setText(str(0))

	#evento del boton btn_creciente
	def btn_mas_clicked(self):
		var_creciente = int(self.text_contador.text()) +1 
		self.text_contador.setText (str(var_creciente))

	#evento del boton btn_menos
	def btn_menos_clicked(self):
		var_decreciente = int(self.text_contador.text()) -1 
		if var_decreciente == -1:
			var_decreciente = 0
		else:
			self.text_contador.setText (str(var_decreciente))

	#evento del boton btn_reset
	def btn_reset_clicked(self):
		self.text_contador.setText (str(0))


app = QtWidgets.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
