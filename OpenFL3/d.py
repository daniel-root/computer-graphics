from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
a = 1
b = 0.5
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
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(0,0)
    glVertex2f(a,0)
    glVertex2f(b,a)
    glEnd()
    glFlush()
def Teclado(key,x,y):
    global a
    global b
    if key == ' ':
            sys.exit()
    elif key == 't':
            a = -1
            b = -0.5
            draw()
            glutPostRedisplay()
    elif key == 'T':
            a = 1
            b = 0.5
            draw()
            glutPostRedisplay()
def init():
    glClearColor(1.0,1.0,1.0,1.0)
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutCreateWindow("Questao 03 - 1")
glutDisplayFunc(draw)
glutKeyboardFunc(Teclado)
init()
glutMainLoop()