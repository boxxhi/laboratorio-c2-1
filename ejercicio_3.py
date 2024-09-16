"""
    3. Construir un programa que muestre una ventana a través de la cual se pueda leer su número de cédula y su nombre completo.
"""

# Importamos las librerias de PyQt5 y otras
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QGridLayout, QPushButton, QMessageBox

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("EJERCICIO 3")
        self.setGeometry(100, 100, 400, 200)
        
        # Instanciamos nuestras `labels`
        self.nombre_l = QLabel("Nombre:", self)
        self.dui_l = QLabel("DUI:", self)

        # Ahora los inputs
        self.nombre_in = QLineEdit(self)
        self.dui_in = QLineEdit(self)

        layout = QGridLayout()

        layout.addWidget(self.nombre_l, 0, 0)
        layout.addWidget(self.nombre_in, 0, 1)

        layout.addWidget(self.dui_l, 1, 0)
        layout.addWidget(self.dui_in, 1, 1)

        # un buton para mostrar los datos
        btn = QPushButton("Mostrar")
        btn.clicked.connect(self.mostrar)

        layout.addWidget(btn, 2, 1)

        self.setLayout(layout)
        # Mostramos la ventana
        self.show()

    def mostrar(self):
        # Obtenemos el texto de los inputs
        dui = self.dui_in.text()
        nombre = self.nombre_in.text()
        
        msg = QMessageBox()
        if nombre == "" or dui == "":
            msg.setWindowTitle("ERROR")
            msg.setText("Datos invalidos!")
            msg.setStandardButtons(QMessageBox.Ok)

        else:
            msg.setWindowTitle("DATOS")
            msg.setText(f"DUI: {dui}\nNombre: {nombre}")
            msg.setStandardButtons(QMessageBox.Ok)
        
        msg.exec_()

# Instanceamos las clases
app = QApplication([])
window = Window()

# Empezamos la ejecucion
sys.exit(app.exec())