from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
x0 = 1
y0 = 1
x1 = 1
y1 = 1
x2 = 1
y2 = 1

def triangulo():
    glPushMatrix()
    glScalef(x0,y0, 0)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(6,18)#A
    glVertex2f(14,18)#F
    glVertex2f(12,16)#G
    glVertex2f(8,16)#Z
    glEnd()
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(5,8)#S erro
    glVertex2f(2,6)#T erro
    glVertex2f(2,14)#U erro
    glVertex2f(5,12)#V erro
    glEnd()
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(16,12)#I
    glVertex2f(18,14)#J
    glVertex2f(18,6)#K
    glVertex2f(16,8)#L
    glEnd()
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(12,5)#N
    glVertex2f(14,2)#O
    glVertex2f(6,2)#P
    glVertex2f(8,5)#Q
    glEnd()
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(8,16)#Z
    glVertex2f(12,16)#G
    glVertex2f(12,4)#N
    glVertex2f(8,4)#Q
    glEnd()
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(5,12)#V
    glVertex2f(16,12)#I
    glVertex2f(16,8)#L
    glVertex2f(5,8)#S
    glEnd()
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex2f(9,15)#a
    glVertex2f(11,15)#b
    glVertex2f(11,5)#g
    glVertex2f(9,5)#h
    glEnd()
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex2f(15,11)#d
    glVertex2f(15,9)#e
    glVertex2f(5,9)#j
    glVertex2f(5,11)#k
    glEnd()
    glPopMatrix()
def quadrado():
    glPushMatrix()
    glScalef(x2,y2, 0)
    glShadeModel(GL_SMOOTH)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,0.0)
    glVertex2f(30,30)
    glColor3f(0.0,1.0,0.0)
    glVertex2f(30,50)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(50,50)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(50,30)
    glEnd()
    glPopMatrix()
def triangulo_():
    glPushMatrix()
    glScalef(x1,y1, 0)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2i(10,10)
    glVertex2i(10,20)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(20,10)
    glEnd()
    glPopMatrix()
def Desenha():
    glMatrixMode(GL_MODELVIEW)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    quadrado()
    triangulo()
    triangulo_()
    glFlush()
def Teclado(key,x,y):
    global x0
    global y0
    global x1
    global y1
    global x2
    global y2
    if key == ' ':
        sys.exit()
    elif key == 'r':
        x0 = 5
        y0 = 10
        triangulo()
        glutPostRedisplay()
    elif key == 't':
        x2 = 5
        y2 = 1
        triangulo_()
        glutPostRedisplay()
    elif key == 'y':
        x1 = 10
        y1 = 0.5
        quadrado()
        glutPostRedisplay()
def Inicializa():
    glClearColor(1.0,1.0, 1.0, 1.0)
def AlteraTamanhoJanela(w,h):
    if(h == 0): h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if (w <= h): gluOrtho2D (0.0, 250.0, 0.0, 250.0*h/w)
    else: gluOrtho2D (0.0, 250.0*w/h, 0.0, 250.0)
glutInit()
print("Precione:")
print("r - Cruz de Malta")
print("t - Quadrado")
print("y - Triangulo")
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400,350)
glutInitWindowPosition(10,10)
glutCreateWindow("C")
glutDisplayFunc(Desenha)
glutReshapeFunc(AlteraTamanhoJanela)
glutKeyboardFunc(Teclado)
Inicializa()
glutMainLoop()