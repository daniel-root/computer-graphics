from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
shoulder = 0
elbow = 0

def init():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)
def display():
    glClear (GL_COLOR_BUFFER_BIT)
    glPushMatrix()
        glTranslatef (-1.0, 0.0, 0.0)
        glRotatef (shoulder, 0.0, 0.0, 1.0)
        glTranslatef (1.0, 0.0, 0.0)
        glPushMatrix()
            glScalef (2.0, 0.4, 1.0)
            glutWireCube (1.0)
        glPopMatrix()
            glTranslatef (1.0, 0.0, 0.0)
            glRotatef (elbow, 0.0, 0.0, 1.0)
            glTranslatef (1.0, 0.0, 0.0)
        glPushMatrix()
            glScalef (2.0, 0.4, 1.0)
            glutWireCube (1.0)
        glPopMatrix()
    glPopMatrix()
    glutSwapBuffers()
def reshape (w,h):
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluPerspective(65.0, w/h, 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef (0.0, 0.0, -5.0)
def keyboard (key,x,y):
    global shoulder
    global elbow
    if key == 's':
        shoulder = (shoulder + 5) % 360
        glutPostRedisplay()
    elif key == 'S':
        shoulder = (shoulder - 5) % 360
        glutPostRedisplay()
    elif key == 'e':
        elbow = (elbow + 5) % 360
        glutPostRedisplay()
    elif key == 'E':
        elbow = (elbow - 5) % 360
        glutPostRedisplay()
    elif key == 27:
        exit(0)
glutInit()
glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize (500, 500)
glutInitWindowPosition (100, 100)
glutCreateWindow ("Braco")
init ()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMainLoop()