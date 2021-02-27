from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
x1 = 100 
y1 = 40
z1 = 100
rA = 0
rB = 0
rA1 = 0
rB1 = 0
rC = 0
rC1 = 0
rD = 0
rD1 = 0
angle = 45
fAspect = 1
def main():
    glutInit()
    print("Use o Mouse")
    print("Clique Left - Zoon in", "Clique Right Zoon out")
    print("Use o teclado")
    print("Clique X e x movimenta no eixo")
    print("Clique Y e y movimenta no eixo")
    print("Clique Z e z movimenta no eixo")
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(300,300)
    glutCreateWindow("Visualizacao 3D")
    Inicializa()
    glutDisplayFunc(Desenha)
    glutReshapeFunc(AlteraTamanhoJanela)
    glutKeyboardFunc(Teclado)
    glutMouseFunc(GerenciaMouse)
    glutMainLoop()
def Desenha():
    glClear (GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslate(-4,1,1)
    glutSolidTeapot(0.5)
    glPopMatrix()
    glPushMatrix()
    glRotatef(rB1, 0., 0., 1.)
    glRotatef(rB, 1., 0., 0.)
    glTranslatef(1., 0., 0.)
    glPushMatrix()
    glScalef(2.0, 0.4, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    glutWireCube(1.)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(1, 0, -0.5)
    glutWireCylinder(0.25,1,12,1)
    glPopMatrix()
    glTranslatef(1., 0., 0.)
    glRotatef(rC1, 0., 0., 1.)
    glRotatef(rC, 1., 0., 0.)
    glTranslatef(1., 0., 0.)
    glPushMatrix()
    glScalef(2.0, 0.4, 1.0)
    glColor3f(249./255., 238./255., 153./255.)
    glutWireCube(1.)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(1, 0, -0.5)
    glutWireCylinder(0.25,1,12,1)
    glPopMatrix()
    glTranslatef(1., 0., 0.)
    glRotatef(rD1, 0., 0., 1.)
    glRotatef(rD, 1., 0., 0.)
    glTranslatef(1., 0., 0.)
    glPushMatrix()
    glScalef(2.0, 0.4, 1.0)
    glColor3f(207./255., 106./255., 76./255.)
    glutWireCube(1.)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(1, 0, -0.25)
    glutWireCylinder(0.25,0.5,12,1)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(1., 0., 0.)
    #glRotatef(rA1, 0., 0., 1.)
    glRotatef(rA, 0., 0., 1.)
    glTranslatef(0.5, 0., 0.)
    
    glScalef(1.5, 0.2, 0.5)
    glColor3f(100./255., 106./255., 76./255.)
    glutWireCube(1.)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(1., 0., 0.)
    glRotatef(rA1, 0., 0., 1.)
    #glRotatef(rA, 0., 0., 1.)
    glTranslatef(0.5, 0., 0.)
    
    glScalef(1.5, 0.2, 0.5)
    glColor3f(100./255., 106./255., 76./255.)
    glutWireCube(1.)
    glPopMatrix()
    glPopMatrix()
    glutSwapBuffers()
def Inicializa ():
    glClearColor(0, 0, 0, 1.0)
    angle = 50
def EspecificaParametrosVisualizacao():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(angle,fAspect,0.1,0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(x1,y1,z1, 0,0,0, 0,0,1)
def AlteraTamanhoJanela(w,h):
    global fAspect
    if ( h == 0 ): h = 1
    glViewport(0, 0, w, h)
    fAspect = w/h
    EspecificaParametrosVisualizacao()
def Teclado(key,x,y):
    global x1
    global y1
    global z1
    global rA
    global rB
    global rC
    global rD
    global rA1
    global rB1
    global rC1
    global rD1
    if key == ' ':
            sys.exit()
    elif key == 'x':
            x1 = x1 + 1
            EspecificaParametrosVisualizacao()
            glutPostRedisplay()
    elif key == 'y': 
            y1 = y1 + 1
            EspecificaParametrosVisualizacao()
            glutPostRedisplay()
    elif key == 'z':
            z1 = z1 + 1
            EspecificaParametrosVisualizacao()
            glutPostRedisplay()
    elif key == 'X':
            x1 = x1 - 1
            EspecificaParametrosVisualizacao()
            glutPostRedisplay()
    elif key == 'Y': 
            y1 = y1 - 1
            EspecificaParametrosVisualizacao()
            glutPostRedisplay()
    elif key == 'Z':
            z1 = z1 - 1
            EspecificaParametrosVisualizacao()
            glutPostRedisplay()
    elif key == 'e':
            rB=(rB + 5) % 360
            Desenha()
            glutPostRedisplay()
    elif key == 'q':
            if (rD1>=0 and rD1<=80) or (rD1>=280 and rD1<=355):
                rD1=(rD1 + 5) % 360
                Desenha()
                glutPostRedisplay()
    elif key == 'w':
            if (rC1>=0 and rC1<=80) or (rC1>=280 and rC1<=355):
                rC1=(rC1 + 5) % 360
                Desenha()
                glutPostRedisplay()
    elif key == 'd':
            rB1=(rB1 + 5) % 360
            Desenha()
            glutPostRedisplay()
    elif key == 'E':
            rB=(rB - 5) % 360
            Desenha()
            glutPostRedisplay()
    elif key == 'Q':
            if (rD1>=0 and rD1<=85) or (rD1>=285 and rD1<=360):
                rD1=(rD1 - 5) % 360
                Desenha()
                glutPostRedisplay()
    elif key == 'W':
            if (rC1>=0 and rC1<=85) or (rC1>=285 and rC1<=360):
                    rC1=(rC1 - 5) % 360
                    Desenha()
                    glutPostRedisplay()
    elif key == 'D':
            rB1=(rB1 - 5) % 360
            Desenha()
            glutPostRedisplay()
    elif key == 'a':
            if rA>=0 and rA<=80:
                rA1=(rA1 - 5) % 360
                rA=(rA + 5) % 360
                Desenha()
                glutPostRedisplay()
    elif key == 'A':
            if rA>=5 and rA<=85:
                rA1=(rA1 + 5) % 360
                rA=(rA - 5) % 360
                Desenha()
                glutPostRedisplay()
def GerenciaMouse(button, state, x, y):
    global angle
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            if (angle >= 10):
                angle = angle - 5
                EspecificaParametrosVisualizacao()
                glutPostRedisplay()
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):
            if(angle <= 130):
                angle = angle + 5
                EspecificaParametrosVisualizacao()
                glutPostRedisplay()

if __name__ == "__main__":
	main()
