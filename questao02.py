from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glShadeModel(GL_FLAT)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0.0,0.0)
    glVertex3f(-0.9,-0.5,0.0)
    glColor3f(-0.1,1.0,0.0)
    glVertex3f(-0.9,0.5,0.0)
    glColor3f(0.0,0.0,2.0)
    glVertex3f(-0.1,-0.5,0.0)
    glEnd()
    glShadeModel(GL_SMOOTH)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,0.0,0.0)
    glVertex3f(0.1,-0.5,0.0)
    glColor3f(0.0,1.0,0.0)
    glVertex3f(0.1,0.5,0.0)
    glColor3f(0.0,0.0,1.0)
    glVertex3f(0.9,-0.5,0.0)
    glEnd()
    glFlush()
def init():
    glClearColor(0.0,0.0,0.0,0.0)
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(draw)
init()
glutMainLoop()