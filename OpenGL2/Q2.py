from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
x1 = 1 
y1 = 1
z1 = 2
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
    glColor3f(0.0,0.0,1.0)
    glutWireTeapot(0.5)
    glFlush()
def Teclado(key,x,y):
    global x1
    global y1
    global z1
    if key == ' ':
            sys.exit()
    elif key == '1':
            x1 = 2 
            y1 = 1
            z1 = 1
            confCamera()
            glutPostRedisplay()
    elif key == '2':
            x1 = 2 
            y1 = 2
            z1 = 1
            confCamera()
            glutPostRedisplay()
    elif key == '3':
            x1 = 1 
            y1 = 2
            z1 = 1
            confCamera()
            glutPostRedisplay()
def confCamera():
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45,1.0,0.5,100)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(x1,y1,z1,0,0,0,0,1,0)
def init():
    glClearColor(0.0,0.0,0.0,0.0)
    confCamera()
    glEnable(GL_DEPTH_TEST)
glutInit()
print("Mudanca de Angulo da Camera:")
print("Clique 1 - 2,1,1","Clique 2 - 2,2,1","Clique 3 - 1,2,1")
print("Clique ESPACO para sair!")
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(300,300)
glutCreateWindow("Questao 01")
glutDisplayFunc(draw)
glutKeyboardFunc(Teclado)
init()
glutMainLoop()