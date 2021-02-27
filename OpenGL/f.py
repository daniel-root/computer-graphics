from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-.4,.8)#A
    glVertex2f(.4,.8)#F
    glVertex2f(.2,.6)#G
    glVertex2f(-.2,.6)#Z
    glEnd()
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-.6,-.2)#S
    glVertex2f(-.8,-.4)#T
    glVertex2f(-.8,.4)#U
    glVertex2f(-.6,.2)#V
    glEnd()
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(.6,.2)#I
    glVertex2f(.8,.4)#J
    glVertex2f(.8,-.4)#K
    glVertex2f(.6,-.2)#L
    glEnd()
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(.2,-.6)#N
    glVertex2f(.4,-.8)#O
    glVertex2f(-.4,-.8)#P
    glVertex2f(-.2,-.6)#Q
    glEnd()
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-.2,.6)#Z
    glVertex2f(.2,.6)#G
    glVertex2f(.2,-.6)#N
    glVertex2f(-.2,-.6)#Q
    glEnd()
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-.6,.2)#V
    glVertex2f(.6,.2)#I
    glVertex2f(.6,-.2)#L
    glVertex2f(-.6,-.2)#S
    glEnd()
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-.10,.50)#a
    glVertex2f(.10,.50)#b
    glVertex2f(.10,-.50)#g
    glVertex2f(-.10,-.50)#h
    glEnd()
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex2f(.50,.10)#d
    glVertex2f(.50,-.10)#e
    glVertex2f(-.50,-.10)#j
    glVertex2f(-.50,.10)#k
    glEnd()
    
    glFlush()
def init():
    glClearColor(1,1,1,1)
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutCreateWindow("Questao 06")
glutDisplayFunc(draw)
init()
glutMainLoop()