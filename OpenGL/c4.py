from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glShadeModel(GL_FLAT)
    glBegin(GL_LINES)
    glColor3f(0.0,1.0,0.0)
    glVertex2f(0,1)
    glVertex2f(0,-1)
    glColor3f(0.0,1.0,0.0)
    glVertex2f(1,0)
    glVertex2f(-1,0)
    glEnd()
    glShadeModel(GL_FLAT)
    glBegin(GL_LINE_STRIP)
    glColor3f(0.0,0.0,1.0)
    glVertex2f(.4,.6)
    glVertex2f(.8,.0)
    glVertex2f(.4,-.6)
    glVertex2f(-.4,-.6)
    glVertex2f(-.8,0)
    glVertex2f(-.4,.6)
    glEnd()
    glFlush()
def init():
    glClearColor(1.0,1.0,1.0,1.0)
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutCreateWindow("Questao 03 - 4")
glutDisplayFunc(draw)
init()
glutMainLoop()