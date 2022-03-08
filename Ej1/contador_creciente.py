# Rosas Palacios Alan

import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets

#Cargar nuestro archivo .ui
form_class = uic.loadUiType("contador_creciente.ui")[0]

class MyWindowClass(QtWidgets.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.boton_creciente.clicked.connect(self.boton_creciente_clicked)
		self.text_creciente.setText(str(0))

	#evento del boton boton_creciente
	def boton_creciente_clicked(self):
		var_creciente = int(self.text_creciente.text()) +1 
		self.text_creciente.setText (str(var_creciente))


app = QtWidgets.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
