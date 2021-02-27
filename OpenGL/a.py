from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_QUADS)
    glVertex2f(.5,.5)
    glVertex2f(-.5,.5)
    glVertex2f(-.5,-.5)
    glVertex2f(.5,-.5)
    glEnd()
    glFlush()
def init():
    glClearColor(0.0,0.0,0.0,0.0)
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutCreateWindow("Questao 01")
glutDisplayFunc(draw)
init()
glutMainLoop()