"""
    5. Construir un programa que muestre una ventana a través de la cual se puedan leer 10 datos característicos de una persona.
"""

#importamos las librerias
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Datos Personales')
        self.setGeometry(100, 100, 400, 600)

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.datos_persona = []
        etiquetas = [
            'Nombre Completo', 'Edad', 'Género', 'Dirección', 'Teléfono',
            'Correo Electrónico', 'Ocupación', 'Nacionalidad', 'Estado Civil', 'Hobbies'
        ]

        for etiqueta in etiquetas:
            label = QLabel(f'{etiqueta}:', self)
            input_field = QLineEdit(self)
            self.form_layout.addRow(label, input_field)
            self.datos_persona.append(input_field)

        self.boton = QPushButton('Mostrar Datos', self)
        self.boton.clicked.connect(self.mostrar_datos)
        self.resultado = QLabel('', self)

        #gestionaremos las dimensiones de la ventana 
        layout.addLayout(self.form_layout)
        layout.addWidget(self.boton)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def mostrar_datos(self):
        datos = []
        
        # Con el siguiente ciclo for iremos ejecutando en orden cada dato hasta completar los campos
        for i, input_field in enumerate(self.datos_persona):
            datos.append(f'{self.form_layout.itemAt(i*2).widget().text()}: {input_field.text()}')

        self.resultado.setText('\n'.join(datos))


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec_())