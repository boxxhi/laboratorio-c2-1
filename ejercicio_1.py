"""
    1. Construir un programa que muestre una ventana en la cual aparezca su nombre completo y su edad centrados. 
"""

# Importamos las librerias de PyQt5 y otras
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("EJERCICIO 1")
        self.setGeometry(100, 100, 400, 200)
        
        # Instanciamos nuestras `labels`
        self.nombre = QLabel("Nombre: DIEGO SAMUEL REYES MORENO", self)
        self.edad = QLabel("Edad: 20", self)

        # Colocamos el ancho de nombre y lo alineamos al centro, esto
        # para que no quede alineado a la izquierda
        self.edad.setFixedWidth(208)
        self.edad.setAlignment(Qt.AlignCenter)

        # La mejor manera que encontre para centrar
        # Se podria usar un layout pero queda mucho espacio entre las columnas
        # por el tamano de la ventana
        self.nombre.move(100, 70)
        self.edad.move(100, 90)

        # Mostramos la ventana
        self.show()

# Instanceamos las clases
app = QApplication([])
window = Window()

# Empezamos la ejecucion
sys.exit(app.exec())