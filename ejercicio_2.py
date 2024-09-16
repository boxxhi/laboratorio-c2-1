"""
    2. Construir un programa que muestre una ventana y que lea una clave secreta sin mostrar los caracteres que la componen.
"""

# Importamos las librerias de PyQt5 y otras
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QWidget, QGridLayout, QPushButton

CONTRA_REAL = "Vicio2024"

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EJERCICIO 2")
        self.setGeometry(100, 100, 400, 100)

        # Instanciamos nuestros Widgets
        self.verificar = QPushButton("Verificar", self)
        self.label = QLabel("Contraseña:", self)
        self.respuesta = QLabel("", self)
        self.contra = QLineEdit(self)
        
        # Colocamos en modo contrasena para que no se 
        # muestren los caracteres
        self.contra.setEchoMode(QLineEdit.EchoMode.Password)

        # Conectamos con el metodo verificar_contra
        self.verificar.clicked.connect(self.verificar_contra)
        
        layout = QGridLayout()

        layout.addWidget(self.label,     0, 0)
        layout.addWidget(self.contra,    0, 1)
        layout.addWidget(self.verificar, 1, 0)
        layout.addWidget(self.respuesta, 1, 1)

        # Alineamos para el centro
        layout.setAlignment(Qt.AlignCenter)
        
        # Mostramos la ventana y colocamos el layout
        self.setLayout(layout)
        self.show()

    def verificar_contra(self):
        if self.contra.text() == CONTRA_REAL:
            self.respuesta.setText('Contrasena valida!')
        else:
            self.respuesta.setText('Contrasena invalida!')


# Instanceamos las clases
app = QApplication([])
window = Window()

# Empezamos la ejecucion
sys.exit(app.exec())