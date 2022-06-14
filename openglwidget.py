from PyQt5 import QtOpenGL
import OpenGL.GL as gl
import OpenGL.GL.shaders
import numpy as np
import ctypes

class GLWidget(QtOpenGL.QGLWidget):

    vertex_shader = """
    #version 330
    in vec3 pos;
    void main()
    {
    gl_Position = vec4(pos, 1.0);
    }
    """

    fragment_shader = """
    #version 330
    void main()
    {
    gl_FragColor = vec4(1.0f, 1.0f, 1.0f, 1.0f);
    }
    """

    vp = [ 0.0,  0.0, 0.0 ]
    vp = np.array(vp, dtype=np.float32)

    vt = [ -0.7,  0.3, 0.0,
        -0.3,  0.3, 0.0,
        -0.5, 0.7, 0.0]
    vt = np.array(vt, dtype=np.float32)

    vq = [  0.3,  -0.7, 0.0,
            0.7,  -0.7, 0.0,
            0.7,  -0.3, 0.0,
            0.7,  -0.3, 0.0,
            0.3,  -0.3, 0.0,
            0.3,  -0.7, 0.0,]
    vq = np.array(vq, dtype=np.float32)

    vCurva = [   
        -0.5,  0.0, 0.0,
        -0.25,  0.3, 0.0,
        0.0,  0.6, 0.0,
        0.25, 0.3, 0.0,
        0.5, 0.0, 0.0]
    vCurva = np.array(vCurva, dtype=np.float32)

    menuIndex = 0

    def __init__(self, parent=None):
        self.parent = parent
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.resize(300, 300)
        

    def initializeGL(self):
        gl.glClearColor(0.0, 0.2, 0.3, 1.0)
        gl.glEnable(gl.GL_DEPTH_TEST)
        self.shaderFiguras = OpenGL.GL.shaders.compileProgram(
            OpenGL.GL.shaders.compileShader(self.vertex_shader, gl.GL_VERTEX_SHADER),
            OpenGL.GL.shaders.compileShader(self.fragment_shader, gl.GL_FRAGMENT_SHADER)
        )
        self.desenharPonto(self.vp)
        self.desenharTriangulo(self.vt)
        self.desenharQuadrado(self.vq)

        self.shaderCurva = OpenGL.GL.shaders.compileProgram(
            OpenGL.GL.shaders.compileShader(self.vertex_shader, gl.GL_VERTEX_SHADER),
            OpenGL.GL.shaders.compileShader(self.fragment_shader, gl.GL_FRAGMENT_SHADER)
        )
        self.desenharCurva(self.vCurva)
        

    def resizeGL(self, width, height):
        self.w = width
        self.h = height
        self.xVp = 0
        self.yVp = 0
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glMatrixMode(gl.GL_MODELVIEW)

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glViewport(self.xVp, self.yVp, self.w, self.h)
        if(self.menuIndex == 0):
            gl.glClearColor(0.0, 0.2, 0.3, 1.0)
            gl.glUseProgram(self.shaderFiguras)
            gl.glBindVertexArray( self.vaoPonto )
            gl.glDrawArrays(gl.GL_POINTS, 0, 1)
            gl.glBindVertexArray( self.vaoTriangulo )
            gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)
            gl.glBindVertexArray( self.vaoQuadrado )
            gl.glDrawArrays(gl.GL_TRIANGLES, 0, 6)
            gl.glBindVertexArray( 0 )

        if(self.menuIndex == 1):
            gl.glClearColor(0.0, 0.0, 0.0, 1.0)
            gl.glUseProgram(self.shaderCurva)
            gl.glBindVertexArray( self.vaoCurva )
            gl.glDrawArrays(gl.GL_POINTS, 0, int(len(self.vCurva)/3))
            gl.glBindVertexArray( self.vaoCurvaPontos )
            gl.glDrawArrays(gl.GL_LINE_STRIP, 0, int(len(self.novosVertices)/3))
            gl.glBindVertexArray( 0 )
            gl.glUseProgram(0)

    def desenharPonto(self, v):
        self.vaoPonto = gl.glGenVertexArrays(1)
        gl.glBindVertexArray( self.vaoPonto )
        vertex_buffer = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vertex_buffer)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, 12, v, gl.GL_STATIC_DRAW)
        gl.glEnableVertexAttribArray(0)
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, False, 0, ctypes.c_void_p(0))
        gl.glBindVertexArray( 0 )
        gl.glDisableVertexAttribArray(0)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)

    def desenharTriangulo(self, v):
        self.vaoTriangulo = gl.glGenVertexArrays(1)
        gl.glBindVertexArray( self.vaoTriangulo )
        vertex_buffer = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vertex_buffer)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, 36, v, gl.GL_STATIC_DRAW)
        gl.glEnableVertexAttribArray(0)
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, False, 0, ctypes.c_void_p(0))
        gl.glBindVertexArray( 0 )
        gl.glDisableVertexAttribArray(0)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)

    def desenharQuadrado(self, v):
        self.vaoQuadrado = gl.glGenVertexArrays(1)
        gl.glBindVertexArray( self.vaoQuadrado )
        vertex_buffer = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vertex_buffer)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, 96, v, gl.GL_STATIC_DRAW)
        gl.glEnableVertexAttribArray(0)
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, False, 0, ctypes.c_void_p(0))
        gl.glBindVertexArray( 0 )
        gl.glDisableVertexAttribArray(0)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)

    def desenharCurva(self, vertices):
        self.novosVertices = []
        self.gerarPontosCurva(self.vCurva, 5)
        self.vaoCurva = gl.glGenVertexArrays(1)
        gl.glBindVertexArray( self.vaoCurva )
        vertex_buffer = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vertex_buffer)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, 15*4, vertices, gl.GL_STATIC_DRAW)
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, False, 0, ctypes.c_void_p(0))
        gl.glEnableVertexAttribArray(0)
        gl.glBindVertexArray( 0 )
        gl.glDisableVertexAttribArray(0)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)

        self.vaoCurvaPontos = gl.glGenVertexArrays(1)
        gl.glBindVertexArray( self.vaoCurvaPontos )
        vertex_buffer = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vertex_buffer)
        self.novosVertices = np.array(self.novosVertices, dtype=np.float32)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, 30*4, self.novosVertices, gl.GL_STATIC_DRAW)
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, False, 0, ctypes.c_void_p(0))
        gl.glEnableVertexAttribArray(0)
        gl.glBindVertexArray( 0 )
        gl.glDisableVertexAttribArray(0)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)

    def gerarPontosCurva(self, vertices, nivel):
        if(nivel < 2):
            self.novosVertices.append(vertices[0])
            self.novosVertices.append(vertices[1])
            self.novosVertices.append(0.0)
            return
        aux = []
        i = 0
        while i < len(vertices) and (len(vertices) - i > 3):
            pontoX = vertices[i]
            if(vertices[i] != vertices[i+3]):
                auxX = ( max(vertices[i], vertices[i+3]) - min(vertices[i], vertices[i+3]) )
                pontoX = (max(vertices[i], vertices[i+3]) - ( auxX / 2 ) )

            pontoY = vertices[i+1]
            if(vertices[i+1] != vertices[i+1+3]):
                auxY = ( max(vertices[i+1], vertices[i+1+3]) - min(vertices[i+1], vertices[i+1+3]) )
                pontoY = (max(vertices[i+1], vertices[i+1+3]) - ( auxY / 2 ) )
            
            aux.append(pontoX)
            aux.append(pontoY)
            aux.append(0.0)
            i = i + 3
        self.novosVertices.append(vertices[0])
        self.novosVertices.append(vertices[1])
        self.novosVertices.append(0.0)
        self.gerarPontosCurva(aux, nivel-1)
        self.novosVertices.append(vertices[len(vertices)-3])
        self.novosVertices.append(vertices[len(vertices)-2])
        self.novosVertices.append(0.0)

