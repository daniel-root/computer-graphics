from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
movY=0
movX=0
rotar=0
tam=0.3
escX=1.0
escY=1.0
escZ=1.0
def principal():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslated(movX,movY,0.0)
    glRotatef(rotar,0.1,0.1,0.0)
    glScalef(escX,escY,escZ)
    glPushMatrix()
    glutWireSphere(tam, 50, 50)
    glPopMatrix()
    glFlush()
    glutSwapBuffers()
def movimiento(keys,x,y):
    global movX
    global movY
    if keys == GLUT_KEY_RIGHT:
        movX+=0.1
        principal()
        glutPostRedisplay()
    elif keys == GLUT_KEY_LEFT:
        movX-=0.1
        principal()
        glutPostRedisplay()
    elif keys == GLUT_KEY_UP:
        movY+=0.1
        principal()
        glutPostRedisplay()
    elif keys == GLUT_KEY_DOWN:
        movY-=0.1
        principal()
        glutPostRedisplay()
def aumentar(pres,x,y):
    global rotar
    global tam
    global escX
    global escY
    global escZ
    if pres =='a':
        rotar-=4.1
        principal()
        glutPostRedisplay()
    elif pres =='s':
        rotar+=4.1
        principal()
        glutPostRedisplay()
    elif pres =='j':
        tam+=0.3
        principal()
        glutPostRedisplay()
    elif pres =='k':
        tam-=0.3
        principal()
        glutPostRedisplay()
    elif pres =='u':
        escX+=0.1
        principal()
        glutPostRedisplay()
    elif pres =='i':
        escY+=0.1
        principal()
        glutPostRedisplay()
    elif pres =='o':
        escZ+=0.1
        principal()
        glutPostRedisplay()
    elif pres =='b':
        escX-=0.1
        principal()
        glutPostRedisplay()
    elif pres =='n':
        escY-=0.1
        principal()
        glutPostRedisplay()
    elif pres =='m':
        escZ-=0.1
        principal()
        glutPostRedisplay()
    elif pres == ' ':
        exit()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800,800)
    glutInitWindowPosition(450,150)
    glutCreateWindow("Movimiento circulo")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(principal)
    glutSpecialFunc(movimiento)
    glutKeyboardFunc(aumentar)
    glutMainLoop()
main()