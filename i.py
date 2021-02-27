from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

cameraDistance = 12
cameraAngle = 0
#angles = { Y rotation at shoulder, Z rotation at shoulder, Z rotation at elbow, X rotation at wrist }
arm_angles = [0, 0, 0, 0, 0]
enum = [SHOULDER_Y, SHOULDER_Z, ELBOW_Z, WRIST_X, WRIST_Z]
def change_angle(angle,delta, minimum = 0, maximum = 180):
    arm_angles[angle] = (arm_angles[angle] + delta) % 360
    arm_angles[angle] = max(arm_angles[angle], minimum)
    arm_angles[angle] = min(arm_angles[angle], maximum)
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    x = cameraDistance * sin(cameraAngle)
    z = cameraDistance * cos(cameraAngle)
    gluLookAt (x, 0.0, z, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glPushMatrix()
    glRotatef(arm_angles[SHOULDER_Y], 0., 1., 0.)
    glRotatef(arm_angles[SHOULDER_Z], 0., 0., 1.)
    glTranslatef(1., 0., 0.)
    glPushMatrix()
    glScalef(2.0, 0.4, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    glutWireCube(1.)
    glPopMatrix()
    glTranslatef(1., 0., 0.)
    glRotatef(arm_angles[ELBOW_Z], 0., 0., 1.)
    glTranslatef(1., 0., 0.)
    glPushMatrix()
    glScalef(2.0, 0.4, 1.0)
    glColor3f(249./255., 238./255., 153./255.)
    glutWireCube(1.)
    glPopMatrix()
    glTranslatef(1., 0., 0.)
    glRotatef(arm_angles[WRIST_Z], 0., 0., 1.)
    glRotatef(arm_angles[WRIST_X], 1., 0., 0.)
    glTranslatef(1., 0., 0.)
    glPushMatrix()
    glScalef(2.0, 0.4, 1.0)
    glColor3f(207./255., 106./255., 76./255.)
    glutWireCube(1.)
    glPopMatrix()
    glPopMatrix()
    glutSwapBuffers()
def reshape(w,h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum (-1.0, 1.0, -1.0, 1.0, 1.5, 300.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
def specialKeys(key,x,y):
    distanceDelta = 1.0
    angleDelta = 5 * M_PI / 180.0
    if(key == GLUT_KEY_UP):
        cameraDistance -= distanceDelta;
        cameraDistance = max(2.0, cameraDistance)
    if(key == GLUT_KEY_DOWN):
        cameraDistance += distanceDelta
    if(key == GLUT_KEY_LEFT):
        cameraAngle -= angleDelta
    if(key == GLUT_KEY_RIGHT):
        cameraAngle += angleDelta
    glutPostRedisplay()
def keyboard(key,x,y):
    delta = 5
    if key == 27:
        exit(0)
    elif key =='q':
        change_angle(SHOULDER_Y, delta, -180, 0)
    elif key == 'a':
        change_angle(SHOULDER_Y, -delta, -180, 0)
    elif key =='w':
        change_angle(SHOULDER_Z, delta, -90, 90)
    elif key == 's':
        change_angle(SHOULDER_Z, -delta, -90, 90)
    elif key == 'e':
        change_angle(ELBOW_Z, delta, 0, 135)
    elif key == 'd':
        change_angle(ELBOW_Z, -delta, 0, 135)
    elif key == 'r':
        change_angle(WRIST_X, delta, -45, 45)
    elif key == 'f':
        change_angle(WRIST_X, -delta, -45, 45)
    elif key == 't':
        change_angle(WRIST_Z, delta, -15, 90)
    elif key =='g':
        change_angle(WRIST_Z, -delta, -15, 90)
    glutPostRedisplay()
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(700, 700)
glutCreateWindow("Brazo Robot")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutSpecialFunc(specialKeys)
glutKeyboardFunc(keyboard)
glClearColor(0.0, 0.0, 0.0, 1.0)
glutMainLoop();