# Rosas Palacios Alan

import sys
from PyQt5 import uic,QtWidgets

#Cargar nuestro archivo .ui
form_class = uic.loadUiType("contador_decreciente.ui")[0]

class MyWindowClass(QtWidgets.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.boton_decreciente.clicked.connect(self.boton_decreciente_clicked)
		self.text_decreciente.setText(str(88))

	#evento del boton boton_decreciente
	def boton_decreciente_clicked(self):
		var_decreciente = int(self.text_decreciente.text()) - 1 
		
		if var_decreciente == -1:
			var_decreciente = 0
		else:
			self.text_decreciente.setText (str(var_decreciente))


app = QtWidgets.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
