from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
def WireCirculo(raio,cx,cy): 
    glLineWidth(2) 
    glColor3f(1,1,1)
    glBegin(GL_LINE_LOOP)
    for i in range(0,360):
        ang = (i*pi)/180.0
        x = cx + (cos(ang)*raio)
        y = cy + (sin(ang)*raio)
        glVertex2f(x,y)
    glEnd()
def SolidCirculo(raio,cx,cy):
    glLineWidth(2) 
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for i in range(0,360):
        ang = (i*pi)/180.0
        x = cx + (cos(ang)*raio)
        y = cy + (sin(ang)*raio)
        glVertex2f(x,y)
    glEnd()
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    SolidCirculo(0.4,0.5,0)
    WireCirculo(-0.4,-0.5,0)
    glutSwapBuffers()
def init():
    glClearColor(0,0,0,0)
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutCreateWindow("Questao 05")
glutDisplayFunc(draw)
init()
glutMainLoop()