"""
    4. Construir un programa que muestre una ventana a través de la cual se pueda leer tres datos básicos de 3 mascotas diferentes. 
"""

# Importamos las librerias de PyQt5 y otras
import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QGridLayout, QGroupBox, QMessageBox, QPushButton

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("EJERCICIO 3")
        self.setGeometry(100, 100, 400, 400)

        # Se me esta acabando el tiempo asi que 
        # no comentare este
        # Bueno ahora si lo comentare
        
        # Creamos un layout principal
        lla = QGridLayout()

        # Contador para las columnas
        j = 0

        # Son 3 caracteristicas por mascota entonces...
        for i in range(0, 3):

            # Creamos un GroupBox para semerar las mascotas
            q = QGroupBox(f"Mascota {i + 1}")

            # Un GroupBox requiere su propio layout
            layout = QGridLayout()
            q.setLayout(layout)

            label = QLabel(f"Nombre de mascota: ", self)
            qinput1 = QLineEdit(self)
            btn = QPushButton("Mostrar")
                
            layout.addWidget(label, i + j, 0)
            layout.addWidget(qinput1, i + j, 1)

            # Aumentamos en uno para la siguiente columna
            j += 1

            label = QLabel(f"Especie de mascota: ", self)
            qinput2 = QLineEdit(self)
                
            layout.addWidget(label, i+j, 0)
            layout.addWidget(qinput2, i+j, 1)

            # Aumentamos en uno para la siguiente columna
            j += 1

            label = QLabel(f"Edad de mascota: ", self)
            qinput3 = QLineEdit(self)

            layout.addWidget(label, i+j, 0)
            layout.addWidget(qinput3, i+j, 1)
    
            # Aumentamos en uno para la siguiente columna
            j += 1

            # Para los eventos use una tecnica muy comun en javascript
            # llamada closure, consiste en basicamente devolver una funcion
            btn.clicked.connect(self.mostrar(qinput1, qinput2, qinput3))
            layout.addWidget(btn, i+j, 2)

            lla.addWidget(q)


        self.setLayout(lla)
        # Mostramos la ventana
        self.show()

    def mostrar(self, c1, c2, c3):

        # Devolvemos una funcion
        def closure():
            nombre = c1.text()
            especie = c2.text()
            edad = c3.text()
            msg = QMessageBox()

            msg.setWindowTitle("Datos")
            msg.setText(f"Nombre: {nombre}\nEspecie: {especie}\nEdad: {edad}")
            msg.setStandardButtons(QMessageBox.Ok)
            
            msg.exec_()

        return closure

# Instanceamos las clases
app = QApplication([])
window = Window()

# Empezamos la ejecucion
sys.exit(app.exec())