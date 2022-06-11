import SistemaGraficoUI
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = SistemaGraficoUI.Ui_SGI()
        self.ui.setupUi(self)
        self.atribuirBotoes()
        timer = QtCore.QTimer(self)
        timer.setInterval(20)   # period, in milliseconds
        timer.timeout.connect(self.ui.openGLWidget.updateGL)
        timer.start()

    def atribuirBotoes(self):
        self.ui.btTriangulo.clicked.connect(self.desenharTriangulo)
        self.ui.btPonto.clicked.connect(self.desenharPonto)
        self.ui.btPoli.clicked.connect(self.desenharPoligono)
        self.ui.btReset.clicked.connect(self.reset)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_8:
            self.ui.openGLWidget.setRotY(1)
        if e.key() == Qt.Key_5:
            self.ui.openGLWidget.setRotY(-1)
        if e.key() == Qt.Key_4:
            self.ui.openGLWidget.setRotX(-1)
        if e.key() == Qt.Key_6:
            self.ui.openGLWidget.setRotX(1)
    
    def reset(self):
        self.ui.openGLWidget.verticesTriangulo = self.ui.openGLWidget.verticesTrianguloOriginal
        self.ui.openGLWidget.verticesPonto = self.ui.openGLWidget.verticesPontoOriginal

    def desenharPonto(self):
        if( not (self.ui.xPonto.displayText() == "" or self.ui.yPonto.displayText() == "")):
            self.ui.openGLWidget.verticesPonto[0] = float(self.ui.xPonto.displayText())
            self.ui.openGLWidget.verticesPonto[1] = float(self.ui.yPonto.displayText())
    
    def desenharTriangulo(self):
        if(not (self.ui.xTriang1.displayText() == "" or self.ui.yTriang1.displayText() == "")):
            self.ui.openGLWidget.verticesTriangulo[0] = float(self.ui.xTriang1.displayText())
            self.ui.openGLWidget.verticesTriangulo[1] = float(self.ui.yTriang1.displayText())

        if( not (self.ui.xTriang2.displayText() == "" or self.ui.yTriang2.displayText() == "")):
            self.ui.openGLWidget.verticesTriangulo[3] = float(self.ui.xTriang2.displayText())
            self.ui.openGLWidget.verticesTriangulo[4] = float(self.ui.yTriang2.displayText())

        if( not (self.ui.xTriang3.displayText() == "" or self.ui.yTriang3.displayText() == "")):
            self.ui.openGLWidget.verticesTriangulo[6] = float(self.ui.xTriang3.displayText())
            self.ui.openGLWidget.verticesTriangulo[7] = float(self.ui.yTriang3.displayText())
    
    def desenharPoligono(self):
        print("alo")

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())