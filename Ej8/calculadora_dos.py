# Rosas Palacios Alan

import sys
from PyQt5 import QtWidgets, QtGui, uic

#Cargar nuestro archivo .ui
form_class = uic.loadUiType("calculadora_dos.ui")[0]


class MyWindowClass(QtWidgets.QMainWindow, form_class):
	
	
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.btn_calcular.clicked.connect(self.btn_calcular_clicked)
		self.radio_suma.clicked.connect(self.radio_suma_clicked)
		self.radio_resta.clicked.connect(self.radio_resta_clicked)
		self.radio_multiplicacion.clicked.connect(self.radio_multiplicacion_clicked)
		self.radio_division.clicked.connect(self.radio_division_clicked)
		self.text_valor_uno.setText (str(float(0)))
		self.text_valor_dos.setText (str(float(0)))
		self.text_resultado.setText (str(float(0)))
		self.radios = ''

	#evento del boton btn_calcular
	def btn_calcular_clicked(self):
		print (self.radios)
		if self.radios == self.radio_suma.text():
			self.text_resultado.setText(str(round(float(self.text_valor_uno.text()) + float(self.text_valor_dos.text()),2)))
		elif self.radios == self.radio_resta.text():
			self.text_resultado.setText(str(round(float(self.text_valor_uno.text()) - float(self.text_valor_dos.text()),2)))
		elif self.radios == 'multiplicacion':
			self.text_resultado.setText(str(round(float(self.text_valor_uno.text()) * float(self.text_valor_dos.text()),2)))
		elif self.radios == 'division':
			self.text_resultado.setText(str(round(float(self.text_valor_uno.text()) / float(self.text_valor_dos.text()),2)))

	#cargo la variable self.radios con los radiobutton
	def radio_suma_clicked(self):
			self.radios = self.radio_suma.text()

	def radio_resta_clicked(self):
			self.radios = self.radio_resta.text()

	def radio_multiplicacion_clicked(self):
			self.radios = 'multiplicacion'

	def radio_division_clicked(self):
			self.radios = 'division'	

app = QtWidgets.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()