# Rosas Palacios Alan

import sys
from PyQt5 import QtWidgets, QtGui, uic
import random

#Cargar nuestro archivo .ui
form_class = uic.loadUiType("generador_numeros.ui")[0]

class MyWindowClass(QtWidgets.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.btn_generar.clicked.connect(self.btn_generar_clicked)
		self.spin_2.setValue(int(20))

	#evento del boton btn_generar
	def btn_generar_clicked(self):
		var_alea = random.randint(self.spin_1.value(),self.spin_2.value()) 
		self.text_generado.setText(str(var_alea))
	
app = QtWidgets.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()