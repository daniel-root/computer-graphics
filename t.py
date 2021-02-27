from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
tx = ty = 0.0
sx = sy = 1
def Desenha():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(tx, ty, 0.0)
    glScalef(sx, sy, 0)
    glBegin(GL_QUADS)
    glVertex2i(100,150)
    glVertex2i(100,100)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(150,100)
    glVertex2i(150,150)
    glEnd()
    glFlush()
'''def GerenciaMouse(button, state, x, y):
    global tx
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            tx = tx - 1
            Desenha()
            glutPostRedisplay()
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):
            tx = tx + 1
            Desenha()
            glutPostRedisplay()'''
def Teclado(key,x,y):
    global tx
    global ty
    global sx
    global sy
    if key == ' ':
            sys.exit()
    elif key == 'w':
            ty = ty + 1
            Desenha()
            glutPostRedisplay()
    elif key == 's':
            ty = ty - 1
            Desenha()
            glutPostRedisplay()
    elif key == 'a':
            tx = tx - 1
            Desenha()
            glutPostRedisplay()
    elif key == 'd':
            tx = tx + 1
            Desenha()
            glutPostRedisplay()
    elif key == 'X':
            sx = sx + 1
            sy = sx
            Desenha()
            glutPostRedisplay()
    elif key == 'x':
            sx = sx - 1
            sy = sx
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
print("W - up","A - left", "S - down","D - right")
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400,350)
glutInitWindowPosition(10,10)
glutCreateWindow("Quadrado")
glutDisplayFunc(Desenha)
glutReshapeFunc(AlteraTamanhoJanela)
#glutMouseFunc(GerenciaMouse)
glutKeyboardFunc(Teclado)
Inicializa()
glutMainLoop()