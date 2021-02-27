from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
x1 = 1
def prisma():
    glBegin(GL_LINE_LOOP)
    glVertex3f(0.5,-0.3,0.0)
    glVertex3f(-0.25,-0.25,0.0) 
    glVertex3f(-0.25,0.5,0.0)   
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(0.5,-0.3,0.5)
    glVertex3f(-0.25,-0.25,0.5) 
    glVertex3f(-0.25,0.5,0.5)   
    glEnd()
    glBegin(GL_LINES)
    glVertex3f(0.5,-0.3,0.0) 
    glVertex3f(0.5,-0.3,0.5)
    glVertex3f(-0.25,-0.25,0.0) 
    glVertex3f(-0.25,-0.25,0.5)   
    glVertex3f(-0.25,0.5,0.0) 
    glVertex3f(-0.25,0.5,0.5) 
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    #eixo X
    glColor3f(0.0,0.0,0.0)
    glVertex3f(-2.0,0.0,0.0)
    glColor3f(1.0,0.0,0.0)
    glVertex3f(2.0,0.0,0.0)
    #eixo Y
    glColor3f(0.0,0.0,0.0)
    glVertex3f(0.0,-2.0,0.0)
    glColor3f(0.0,1.0,0.0)
    glVertex3f(0.0,2.0,0.0)
    #eixo z
    glColor3f(0.0,0.0,0.0)
    glVertex3f(0.0,0.0,-2.0)
    glColor3f(0.0,0.0,1.0)
    glVertex3f(0.0,0.0,2.0)
    glEnd()
    glColor3f(1.0,1.0,1.0)
    glPushMatrix()
    glRotatef(x1,1,0,0)
    prisma()
    glPopMatrix()
    #glutWireCube(0.5)
    glFlush()
def Teclado(key,x,y):
    global x1
    if key == ' ':
            sys.exit()
    elif key == 't':
            x1 = 20
            draw()
            glutPostRedisplay()
    elif key == 'T':
            x1 = -20
            draw()
            glutPostRedisplay()
def confCamera():
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45,1.0,0.5,100)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(2,1,2,0,0,0,0,1,0)
def init():
    glClearColor(0.0,0.0,0.0,0.0)
    confCamera()
    glEnable(GL_DEPTH_TEST)
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutCreateWindow("Questao 01")
glutDisplayFunc(draw)
glutKeyboardFunc(Teclado)
init()
glutMainLoop()