from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glShadeModel(GL_SMOOTH)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,0.0)
    glVertex2f(0,1)
    glColor3f(0.0,1.0,0.0)
    glVertex2f(1,1)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(1,0)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(0,0)
    glEnd()
    glFlush()
def init():
    glClearColor(1.0,1.0,1.0,1.0)
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutCreateWindow("Questao 02 - 4")
glutDisplayFunc(draw)
init()
glutMainLoop()