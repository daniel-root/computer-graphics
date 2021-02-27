from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
x1 = 1 
y1 = 1
z1 = 2
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
    prisma()
    #glutWireCube(0.5)
    glFlush()
def confCamera():
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45,1.0,0.5,100)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(x1,y1,z1,0,0,0,0,1,0)
def Teclado(key,x,y):
    global x1
    global y1
    global z1
    if key == ' ':
            sys.exit()
    elif key == '1':
            x1 = 1 
            y1 = 1
            z1 = 2
            confCamera()
            glutPostRedisplay()
    elif key == '2':
            x1 = 2 
            y1 = 1
            z1 = 2
            confCamera()
            glutPostRedisplay()
    elif key == '3':
            x1 = 1 
            y1 = 2
            z1 = 2
            confCamera()
            glutPostRedisplay()
def init():
    glClearColor(0.0,0.0,0.0,0.0)
    confCamera()
    glEnable(GL_DEPTH_TEST)
glutInit()
print("Mudanca de Angulo da Camera:")
print("Clique 1 - 1,1,2","Clique 2 - 2,1,2","Clique 3 - 1,2,2")
glutInitWindowSize(300,300)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutCreateWindow("Questao 01")
glutDisplayFunc(draw)
glutKeyboardFunc(Teclado)
init()
glutMainLoop()