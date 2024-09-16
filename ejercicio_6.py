"""

- Después de realizar los cinco ejercicios realizar un ejercicio con la 
librería de PyQt que utilice al menos dos de estos widgets: 
radiobox, combobox y spinbox. El ejercicio debe permitir la entrada 
de datos. Además, proporcionen una explicación detallada sobre 
qué hace el programa y qué problema resuelve. -

- Explicacion
Este programa puede resolver un problema de selección y 
compra de productos en una interfaz gráfica sencilla. 
Podría ser utilizado, por ejemplo, para una aplicación 
de supermercado en línea, donde los usuarios deben 
seleccionar una categoría de productos, una opción 
específica dentro de esa categoría y la cantidad que 
desean comprar. Al final, muestra la selección realizada.

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QComboBox, QSpinBox, QPushButton, QMessageBox

class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        # Label para la categoría de productos
        self.label_category = QLabel('Selecciona una categoría de producto:', self)
        layout.addWidget(self.label_category)
        
        # ComboBox para las categorías
        self.combo = QComboBox(self)
        self.combo.addItem('Electrónica')
        self.combo.addItem('Ropa')
        self.combo.addItem('Alimentos')
        layout.addWidget(self.combo)
        
        # Label para las opciones del producto
        self.label_option = QLabel('Selecciona una opción:', self)
        layout.addWidget(self.label_option)
        
        # RadioButtons para las opciones del producto
        self.radio1 = QRadioButton('Opción A')
        self.radio2 = QRadioButton('Opción B')
        self.radio1.setChecked(True)
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        
        # Label para la cantidad
        self.label_quantity = QLabel('Selecciona la cantidad:', self)
        layout.addWidget(self.label_quantity)
        
        # SpinBox para la cantidad
        self.spinbox = QSpinBox(self)
        self.spinbox.setMinimum(1)
        self.spinbox.setMaximum(100)
        layout.addWidget(self.spinbox)
        
        # Botón para confirmar la selección
        self.button = QPushButton('Confirmar', self)
        self.button.clicked.connect(self.mostrar_seleccion)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        
        self.setWindowTitle('Selector de productos')
        self.show()
    

    def mostrar_seleccion(self):
        # Obtener la categoría seleccionada del ComboBox
        category = self.combo.currentText()
        
        # Obtener la opción seleccionada de los RadioButtons
        if self.radio1.isChecked():
            option = 'Opción A'
        else:
            option = 'Opción B'
        
        # Obtener la cantidad seleccionada del SpinBox
        quantity = self.spinbox.value()
        
        # Crear y mostrar un mensaje con la selección
        QMessageBox.information(self, 'Selección', f'Has seleccionado:\nCategoría: {category}\nOpción: {option}\nCantidad: {quantity}')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
