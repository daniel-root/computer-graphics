from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
x1 = 200 
y1 = 80
z1 = 200
angle = 45
fAspect = 1
def cadeira():
    glBegin(GL_LINE_LOOP)
    glVertex3f(-40,40,0.0)
    glVertex3f(-20,40,0.0)
    glVertex3f(-20,20,0.0)
    glVertex3f(-40,20,0.0)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(20,40,0.0)
    glVertex3f(40,40,0.0) 
    glVertex3f(40,20,0.0)
    glVertex3f(20,20,0.0)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(-40,-20,0.0)
    glVertex3f(-20,-20,0.0) 
    glVertex3f(-20,-40,0.0)
    glVertex3f(-40,-40,0.0)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(20,-20,0.0)
    glVertex3f(40,-20,0.0) 
    glVertex3f(40,-40,0.0)
    glVertex3f(20,-40,0.0)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(-40,40,50)
    glVertex3f(-20,40,50)
    glVertex3f(-20,20,50)
    glVertex3f(-40,20,50)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(20,40,50)
    glVertex3f(40,40,50) 
    glVertex3f(40,20,50)
    glVertex3f(20,20,50)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(-40,-20,50)
    glVertex3f(-20,-20,50) 
    glVertex3f(-20,-40,50)
    glVertex3f(-40,-40,50)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(20,-20,50)
    glVertex3f(40,-20,50) 
    glVertex3f(40,-40,50)
    glVertex3f(20,-40,50)
    glEnd()
    glBegin(GL_LINES)
    glVertex3f(-40,40,0.0)
    glVertex3f(-40,40,50)
    glVertex3f(-20,40,0.0)
    glVertex3f(-20,40,50)
    glVertex3f(-20,20,0.0)
    glVertex3f(-20,20,50)
    glVertex3f(-40,20,0.0)
    glVertex3f(-40,20,50)
    glVertex3f(20,40,0.0)
    glVertex3f(20,40,50)
    glVertex3f(40,40,0.0)
    glVertex3f(40,40,50) 
    glVertex3f(40,20,0.0)
    glVertex3f(40,20,50)
    glVertex3f(20,20,0.0)
    glVertex3f(20,20,50)
    glVertex3f(-40,-20,0.0)
    glVertex3f(-40,-20,50)
    glVertex3f(-20,-20,0.0)
    glVertex3f(-20,-20,50) 
    glVertex3f(-20,-40,0.0)
    glVertex3f(-20,-40,50)
    glVertex3f(-40,-40,0.0)
    glVertex3f(-40,-40,50)
    glVertex3f(20,-20,0.0)
    glVertex3f(20,-20,50)
    glVertex3f(40,-20,0.0)
    glVertex3f(40,-20,50) 
    glVertex3f(40,-40,0.0)
    glVertex3f(40,-40,50)
    glVertex3f(20,-40,0.0)
    glVertex3f(20,-40,50)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(-40,40,50)
    glVertex3f(40,40,50)
    glVertex3f(40,-40,50)
    glVertex3f(-40,-40,50)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(-40,40,60)
    glVertex3f(40,40,60)
    glVertex3f(40,-40,60)
    glVertex3f(-40,-40,60)
    glEnd()
    glBegin(GL_LINES)
    glVertex3f(-40,40,50)
    glVertex3f(-40,40,60)
    glVertex3f(40,40,50)
    glVertex3f(40,40,60)
    glVertex3f(40,-40,50)
    glVertex3f(40,-40,60)
    glVertex3f(-40,-40,50)
    glVertex3f(-40,-40,60)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(-40,40,60)
    glVertex3f(-20,40,60)
    glVertex3f(-20,20,60)
    glVertex3f(-40,20,60)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(-40,-20,60)
    glVertex3f(-20,-20,60) 
    glVertex3f(-20,-40,60)
    glVertex3f(-40,-40,60)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(-40,-20,100)
    glVertex3f(-20,-20,100) 
    glVertex3f(-20,-40,100)
    glVertex3f(-40,-40,100)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(-40,40,100)
    glVertex3f(-20,40,100)
    glVertex3f(-20,20,100)
    glVertex3f(-40,20,100)
    glEnd()
    glBegin(GL_LINES)
    glVertex3f(-40,40,60)
    glVertex3f(-40,40,100)
    glVertex3f(-20,40,60)
    glVertex3f(-20,40,100)
    glVertex3f(-20,20,60)
    glVertex3f(-20,20,100)
    glVertex3f(-40,20,60)
    glVertex3f(-40,20,100)
    glVertex3f(-40,-20,60)
    glVertex3f(-40,-20,100)
    glVertex3f(-20,-20,60)
    glVertex3f(-20,-20,100) 
    glVertex3f(-20,-40,60)
    glVertex3f(-20,-40,100)
    glVertex3f(-40,-40,60)
    glVertex3f(-40,-40,100)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(-40,40,100)
    glVertex3f(-20,40,100)
    glVertex3f(-20,-40,100)
    glVertex3f(-40,-40,100)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glVertex3f(-40,40,110)
    glVertex3f(-20,40,110)
    glVertex3f(-20,-40,110)
    glVertex3f(-40,-40,110)
    glEnd()
    glBegin(GL_LINES)
    glVertex3f(-40,40,100)
    glVertex3f(-40,40,110)
    glVertex3f(-20,40,100)
    glVertex3f(-20,40,110)
    glVertex3f(-20,-40,100)
    glVertex3f(-20,-40,110)
    glVertex3f(-40,-40,100)
    glVertex3f(-40,-40,110)
    glEnd()
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
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    cadeira()
    #glutWireTeapot(50.0)
    glutSwapBuffers()
def Inicializa ():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    angle = 45
def EspecificaParametrosVisualizacao():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(angle,fAspect,0.1,500)
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
