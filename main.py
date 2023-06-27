
import sys
import Window
from PyQt5 import uic, QtWidgets
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Window.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Window.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.Btn_registrar.clicked.connect(self.registrar)
        self.Btn_limpiar.clicked.connect(self.limpiar)
    # Área de los Slots

    def registrar(self):
        try:
            if self.Rb_hombre.isChecked():
                self.sexo = "Hombre"

            elif self.Rb_mujer.isChecked():
                self.sexo = "Mujer"

            self.textEdit.setText('Nombre del usuario: ' + self.txt_nombre.text() + ' ' + self.txt_apellidos.text() + '\nSexo: ' + self.sexo
                                  + '\nFecha de nacimiento: ' + self.txt_fnacimiento.text() + '\nEstado: ' + self.txt_estado.text() + '\nCiudad: ' + self.txt_ciudad.text()
                                  + '\nTelefono: ' + self.txt_telefono.text() + '\nCorreo electronico: ' + self.txt_correo.text())
        except Exception as e:
            self.textEdit.setText("No dejes campos vacios")




    def limpiar(self):
        self.txt_nombre.setText("")
        self.txt_apellidos.setText("")
        self.txt_fnacimiento.setText("")
        self.txt_estado.setText("")
        self.txt_ciudad.setText("")
        self.txt_telefono.setText("")
        self.txt_correo.setText("")
        self.textEdit.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())