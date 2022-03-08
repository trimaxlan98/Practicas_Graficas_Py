# Rosas Palacios Alan

import sys
from PyQt5 import QtWidgets, QtGui, uic
import random

#Cargar nuestro archivo .ui
form_class = uic.loadUiType("juego_matematico.ui")[0]

class MyWindowClass(QtWidgets.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.btn_resultado.clicked.connect(self.btn_resultado_clicked)
		self.btn_nuevo_numero.clicked.connect(self.btn_nuevo_numero_clicked)		
		self.l_text_juegos.setText(str(0))
		self.l_text_buenos.setText(str(0))
		self.l_text_malos.setText(str(0))
		self.text_resultado.setText(str(0))
		self.text_1.setText(str(0))
		self.text_2.setText(str(0))
		self.var_alea = 0
		self.var_juegos = 0
		self.var_buenos = 0
		self.var_malos = 0

	#evento de los radio button
	def radio_suma_clicked(self):
		self.l_text_signo.setText('+')

	def radio_resta_clicked(self):
		self.l_text_signo.setText('-')

	def radio_multiplicacion_clicked(self):
		self.l_text_signo.setText('*')

	def radio_division_clicked(self):
		self.l_text_signo.setText('/')


	#evento del boton btn_resultado
	def btn_resultado_clicked(self):
		if  self.var_alea != 0 :
			if self.var_alea == 1 and int(self.text_resultado.text()) == int(self.text_1.text()) + int(self.text_2.text()):
				self.var_buenos += 1
				self.l_text_buenos.setText(str(self.var_buenos))
			elif self.var_alea == 1 and int(self.text_resultado.text()) != int(self.text_1.text()) + int(self.text_2.text()):
				self.var_malos += 1
				self.l_text_malos.setText(str(self.var_malos))
			elif self.var_alea == 2 and int(self.text_resultado.text()) == int(self.text_1.text()) - int(self.text_2.text()):
				self.var_buenos += 1		
				self.l_text_buenos.setText(str(self.var_buenos))
			elif self.var_alea == 2 and int(self.text_resultado.text()) != int(self.text_1.text()) - int(self.text_2.text()):
				self.var_malos += 1
				self.l_text_malos.setText(str(self.var_malos))
			elif self.var_alea == 3 and int(self.text_resultado.text()) == int(self.text_1.text()) * int(self.text_2.text()):
				self.var_buenos += 1
				self.l_text_buenos.setText(str(self.var_buenos))
			elif self.var_alea == 3 and int(self.text_resultado.text()) != int(self.text_1.text()) * int(self.text_2.text()):
				self.var_malos += 1
				self.l_text_malos.setText(str(self.var_malos))
			elif self.var_alea == 4 and int(self.text_resultado.text()) == int(self.text_1.text()) / int(self.text_2.text()):
				self.var_buenos += 1
				self.l_text_buenos.setText(str(self.var_buenos))
			elif self.var_alea == 4 and int(self.text_resultado.text()) != int(self.text_1.text()) / int(self.text_2.text()):
				self.var_malos += 1
				self.l_text_malos.setText(str(self.var_malos))

			self.var_juegos += 1
			self.l_text_juegos.setText(str(self.var_juegos))
		    #presiono el btn_nuevo_numero
			self.btn_nuevo_numero_clicked()


	#evento del boton btn_nuevo_numero
	def btn_nuevo_numero_clicked(self):
		self.var_alea = random.randint( 1 , 4)
		#print str(var_alea)
		if self.var_alea == 1:
			self.radio_suma_clicked()
			self.radio_suma.setChecked (True)
		elif self.var_alea == 2:
			self.radio_resta_clicked()
			self.radio_resta.setChecked(True)
		elif self.var_alea == 3:
			self.radio_multiplicacion_clicked()
			self.radio_multiplicacion.setChecked(True)
		elif self.var_alea == 4:
			self.radio_division_clicked()
			self.radio_division.setChecked(True)
		primer_numero = random.randint(1,50)
		segundo_numero = random.randint(1,50)
		self.text_1.setText(str(primer_numero))
		self.text_2.setText(str(segundo_numero))


app = QtWidgets.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()