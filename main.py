import UI_MW
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = UI_MW.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.buttonPonto.clicked.connect(self.ponto)
        self.ui.buttonTriangulo.clicked.connect(self.triangulo)
        self.ui.buttonQuadrado.clicked.connect(self.quadrado)

        timer = QtCore.QTimer(self)
        timer.setInterval(20)
        timer.timeout.connect(self.ui.openGLWidget.updateGL)
        timer.start()

        self.ui.actionFiguras.triggered.connect(self.figuras)
        self.ui.actionCurva.triggered.connect(self.curva)

    def figuras(self, a):
        self.ui.openGLWidget.menuIndex = 0
    def curva(self, a):
        self.ui.openGLWidget.menuIndex = 1

    def keyPressEvent(self, e):
        if(self.ui.openGLWidget.menuIndex == 1):
            if e.key() == Qt.Key_W:
                self.ui.openGLWidget.vCurva[1] += 0.05
                self.ui.openGLWidget.desenharCurva(self.ui.openGLWidget.vCurva)
            if e.key() == Qt.Key_S:
                self.ui.openGLWidget.vCurva[1] -= 0.05
                self.ui.openGLWidget.desenharCurva(self.ui.openGLWidget.vCurva)
            if e.key() == Qt.Key_A:
                self.ui.openGLWidget.vCurva[0] -= 0.05
                self.ui.openGLWidget.desenharCurva(self.ui.openGLWidget.vCurva)
            if e.key() == Qt.Key_D:
                self.ui.openGLWidget.vCurva[0] += 0.05
                self.ui.openGLWidget.desenharCurva(self.ui.openGLWidget.vCurva)

            if e.key() == Qt.Key_T:
                self.ui.openGLWidget.vCurva[7] += 0.05
                self.ui.openGLWidget.desenharCurva(self.ui.openGLWidget.vCurva)
            if e.key() == Qt.Key_G:
                self.ui.openGLWidget.vCurva[7] -= 0.05
                self.ui.openGLWidget.desenharCurva(self.ui.openGLWidget.vCurva)
            if e.key() == Qt.Key_F:
                self.ui.openGLWidget.vCurva[6] -= 0.05
                self.ui.openGLWidget.desenharCurva(self.ui.openGLWidget.vCurva)
            if e.key() == Qt.Key_H:
                self.ui.openGLWidget.vCurva[6] += 0.05
                self.ui.openGLWidget.desenharCurva(self.ui.openGLWidget.vCurva)

            if e.key() == Qt.Key_I:
                self.ui.openGLWidget.vCurva[13] += 0.05
                self.ui.openGLWidget.desenharCurva(self.ui.openGLWidget.vCurva)
            if e.key() == Qt.Key_K:
                self.ui.openGLWidget.vCurva[13] -= 0.05
                self.ui.openGLWidget.desenharCurva(self.ui.openGLWidget.vCurva)
            if e.key() == Qt.Key_J:
                self.ui.openGLWidget.vCurva[12] -= 0.05
                self.ui.openGLWidget.desenharCurva(self.ui.openGLWidget.vCurva)
            if e.key() == Qt.Key_L:
                self.ui.openGLWidget.vCurva[12] += 0.05
                self.ui.openGLWidget.desenharCurva(self.ui.openGLWidget.vCurva)

        if e.key() == Qt.Key_1:
            self.ui.openGLWidget.w = self.ui.openGLWidget.w + 25
            self.ui.openGLWidget.h = self.ui.openGLWidget.h + 25
        if e.key() == Qt.Key_3:
            if(self.ui.openGLWidget.w - 25 >= 0 and self.ui.openGLWidget.h - 25 >= 0):
                self.ui.openGLWidget.w = self.ui.openGLWidget.w - 25
                self.ui.openGLWidget.h = self.ui.openGLWidget.h - 25
        if e.key() == Qt.Key_6:
            self.ui.openGLWidget.xVp = self.ui.openGLWidget.xVp + 25
        if e.key() == Qt.Key_4:
            self.ui.openGLWidget.xVp = self.ui.openGLWidget.xVp - 25
        if e.key() == Qt.Key_5:
            self.ui.openGLWidget.yVp = self.ui.openGLWidget.yVp - 25
        if e.key() == Qt.Key_8:
            self.ui.openGLWidget.yVp = self.ui.openGLWidget.yVp + 25
    
    def ponto(self):
        if( self.ui.ponto_le_x.displayText() != "" or self.ui.ponto_le_y.displayText() != "")and(-1 <= float(self.ui.ponto_le_x.displayText()) <=1)and(-1 <= float(self.ui.ponto_le_y.displayText()) <=1):
            self.ui.openGLWidget.vp[0] = float(self.ui.ponto_le_x.displayText())
            self.ui.openGLWidget.vp[1] = float(self.ui.ponto_le_y.displayText())
        self.ui.openGLWidget.desenharPonto(self.ui.openGLWidget.vp)
    
    def triangulo(self):
        if (self.ui.triangulo_le_x_1.displayText() != "" or self.ui.triangulo_le_y_1.displayText() != "")and(-1 <= float(self.ui.triangulo_le_x_1.displayText()) <=1)and(-1 <= float(self.ui.triangulo_le_y_1.displayText()) <=1):
            self.ui.openGLWidget.vt[0] = float(self.ui.triangulo_le_x_1.displayText())
            self.ui.openGLWidget.vt[1] = float(self.ui.triangulo_le_y_1.displayText())

        if( self.ui.triangulo_le_x_2.displayText() != "" or self.ui.triangulo_le_y_2.displayText() != "")and(-1 <= float(self.ui.triangulo_le_x_2.displayText()) <=1)and(-1 <= float(self.ui.triangulo_le_y_2.displayText()) <=1):
            self.ui.openGLWidget.vt[3] = float(self.ui.triangulo_le_x_2.displayText())
            self.ui.openGLWidget.vt[4] = float(self.ui.triangulo_le_y_2.displayText())

        if( self.ui.triangulo_le_x_3.displayText() != "" or self.ui.triangulo_le_y_3.displayText() != "")and(-1 <= float(self.ui.triangulo_le_x_3.displayText()) <=1)and(-1 <= float(self.ui.triangulo_le_y_3.displayText()) <=1):
            self.ui.openGLWidget.vt[6] = float(self.ui.triangulo_le_x_3.displayText())
            self.ui.openGLWidget.vt[7] = float(self.ui.triangulo_le_y_3.displayText())
        self.ui.openGLWidget.desenharTriangulo(self.ui.openGLWidget.vt)

    def quadrado(self):
        if(self.ui.quadrado_le_x_1.displayText() != "" or self.ui.quadrado_le_y_1.displayText() != "")and(-1 <= float(self.ui.quadrado_le_x_1.displayText()) <=1)and(-1 <= float(self.ui.quadrado_le_y_1.displayText()) <=1):
            self.ui.openGLWidget.vq[0] = float(self.ui.quadrado_le_x_1.displayText())
            self.ui.openGLWidget.vq[1] = float(self.ui.quadrado_le_y_1.displayText())
            self.ui.openGLWidget.vq[15] = float(self.ui.quadrado_le_x_1.displayText())
            self.ui.openGLWidget.vq[16] = float(self.ui.quadrado_le_y_1.displayText())

        if(self.ui.quadrado_le_x_2.displayText() != "" or self.ui.quadrado_le_y_2.displayText() != "")and(-1 <= float(self.ui.quadrado_le_x_2.displayText()) <=1)and(-1 <= float(self.ui.quadrado_le_y_2.displayText()) <=1):
            self.ui.openGLWidget.vq[3] = float(self.ui.quadrado_le_x_2.displayText())
            self.ui.openGLWidget.vq[4] = float(self.ui.quadrado_le_y_2.displayText())

        if(self.ui.quadrado_le_x_3.displayText() != "" or self.ui.quadrado_le_y_3.displayText() != "")and(-1 <= float(self.ui.quadrado_le_x_3.displayText()) <=1)and(-1 <= float(self.ui.quadrado_le_y_3.displayText()) <=1):
            self.ui.openGLWidget.vq[6] = float(self.ui.quadrado_le_x_3.displayText())
            self.ui.openGLWidget.vq[7] = float(self.ui.quadrado_le_y_3.displayText())
            self.ui.openGLWidget.vq[9] = float(self.ui.quadrado_le_x_3.displayText())
            self.ui.openGLWidget.vq[10] = float(self.ui.quadrado_le_y_3.displayText())

        if(self.ui.quadrado_le_x_4.displayText() != "" or self.ui.quadrado_le_y_4.displayText() != "")and(-1 <= float(self.ui.quadrado_le_x_4.displayText()) <=1)and(-1 <= float(self.ui.quadrado_le_y_4.displayText()) <=1):
            self.ui.openGLWidget.vq[12] = float(self.ui.quadrado_le_x_4.displayText())
            self.ui.openGLWidget.vq[13] = float(self.ui.quadrado_le_y_4.displayText())
        self.ui.openGLWidget.desenharQuadrado(self.ui.openGLWidget.vq)

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())