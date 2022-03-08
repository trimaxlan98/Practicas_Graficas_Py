# Rosas Palacios Alan

import sys
from PyQt5 import QtWidgets, QtGui, uic

#Cargar nuestro archivo .ui
form_class = uic.loadUiType("peliculas.ui")[0]

class MyWindowClass(QtWidgets.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.btn_aniadir.clicked.connect(self.btn_aniadir_clicked)
		
	#evento del boton btn_aniadir
	def btn_aniadir_clicked(self):
		var_aniadir = self.text_pelicula.text() 
		self.list_peliculas.addItem (var_aniadir)
		self.text_pelicula.setText('')

app = QtWidgets.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
