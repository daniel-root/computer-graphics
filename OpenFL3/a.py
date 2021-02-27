from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
x0 = 1
y0 = 1
x1 = 1
y1 = 1
def Desenha():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(x0,y0, 0.0)
    glScalef(x1,y1, 0)
    glBegin(GL_QUADS)
    glVertex2i(100,150)
    glVertex2i(100,100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(150,100)
    glVertex2i(150,150)
    glEnd()
    glFlush()
def Teclado(key,x,y):
    global x0
    global y0
    global x1
    global y1
    if key == ' ':
            sys.exit()
    elif key == 't': 
            x0 = 100
            y0 = 100
            x1 = 1
            y1 = .5
            Desenha()
            glutPostRedisplay()
    elif key == 'T':
            x0 = 1
            y0 = 1
            x1 = 1
            y1 = 1
            Desenha()
            glutPostRedisplay()
def Inicializa ():
    glClearColor(0.0, 0.0, 0.0, 1.0)
def AlteraTamanhoJanela(w,h):
    if(h == 0): h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if (w <= h): gluOrtho2D (0.0, 250.0, 0.0, 250.0*h/w)
    else: gluOrtho2D (0.0, 250.0*w/h, 0.0, 250.0)
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400,350)
glutInitWindowPosition(10,10)
glutCreateWindow("Quadrado")
glutDisplayFunc(Desenha)
glutReshapeFunc(AlteraTamanhoJanela)
glutKeyboardFunc(Teclado)
Inicializa()
glutMainLoop()