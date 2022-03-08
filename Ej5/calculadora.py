# Rosas Palacios Alan

import sys
from PyQt5 import QtWidgets, QtGui, uic

#Cargar nuestro archivo .ui
form_class = uic.loadUiType("calculadora.ui")[0]

class MyWindowClass(QtWidgets.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.btn_mas.clicked.connect(self.btn_mas_clicked)
		self.btn_menos.clicked.connect(self.btn_menos_clicked)
		self.btn_reset.clicked.connect(self.btn_reset_clicked)
		self.btn_por.clicked.connect(self.btn_por_clicked)
		self.btn_dividir.clicked.connect(self.btn_dividir_clicked)
		self.btn_porcentaje.clicked.connect(self.btn_porcentaje_clicked)
		self.text_primer.setText (str(float(0)))
		self.text_segundo.setText (str(float(0)))
		self.text_resultado.setText(str(float(0)))

	#evento del boton btn_mas
	def btn_mas_clicked(self):
		var_suma = float(self.text_primer.text()) + float(self.text_segundo.text()) 
		self.text_resultado.setText (str(round(var_suma,2)))

	#evento del boton btn_menos
	def btn_menos_clicked(self):
		var_resta = float(self.text_primer.text()) - float(self.text_segundo.text()) 
		self.text_resultado.setText (str(round(var_resta,2)))
	
	#evento del boton btn_por
	def btn_por_clicked(self):
		var_producto = float(self.text_primer.text()) * float(self.text_segundo.text()) 
		self.text_resultado.setText (str(round(var_producto,2)))
	
	#evento del boton btn_dividir
	def btn_dividir_clicked(self):
		var_division = float(self.text_primer.text()) / float(self.text_segundo.text()) 
		self.text_resultado.setText (str(round(var_division,2)))

	#evento del boton btn_reset
	def btn_reset_clicked(self):
		self.text_resultado.setText (str(float(0)))
		self.text_primer.setText (str(float(0)))
		self.text_segundo.setText (str(float(0)))

	#evento del boton btn_porecentaje
	def btn_porcentaje_clicked(self):
		var_porcentaje = (float(self.text_segundo.text()) / float(self.text_primer.text())) * 100
		self.text_resultado.setText (str(round(var_porcentaje,2)) + '%')



app = QtWidgets.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()