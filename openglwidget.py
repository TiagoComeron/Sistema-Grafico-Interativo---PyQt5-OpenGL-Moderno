from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class OpenGLWidget(QOpenGLWidget):

    verticesPontoOriginal = [
        0, 0, -1,
    ]
    verticesPonto = [
        -0, 0, -1,
    ]

    verticesTrianguloOriginal = [
        -0.75, 0.0, 0.0,
        -0.55, 0.0, 0.0,
        -0.65, 0.25, 0.0
    ]
    verticesTriangulo = [
        -0.75, 0.0, 0.0,
        -0.55, 0.0, 0.0,
        -0.65, 0.25, 0.0
    ]
    def __init__(self, parent=None):
        QOpenGLWidget.__init__(self, parent)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(0)
    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)
    def paintGL(self):
        glMatrixMode(GL_PROJECTION)
        glClearColor(0.0, 0.0, 1.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_TRIANGLES)
        glVertex3f(self.verticesTriangulo[0], self.verticesTriangulo[1], self.verticesTriangulo[2])
        glVertex3f(self.verticesTriangulo[3], self.verticesTriangulo[4], self.verticesTriangulo[5])
        glVertex3f(self.verticesTriangulo[6], self.verticesTriangulo[7], self.verticesTriangulo[8])
        glEnd()
        
        glEnable(GL_POINT_SMOOTH)
        glPointSize(5)
        glBegin(GL_POINTS)
        glColor3d(1, 1, 1)
        glVertex3d(self.verticesPonto[0], self.verticesPonto[1], self.verticesPonto[2])
        #glBegin(GL_TRIANGLES)
        #glColor3d(1, 1, 1)
        #glVertex3d(0, 0, 0)
        glEnd()
    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
    