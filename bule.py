#! /usr/bin/env python
''' 
Code is a reduced version of http://www.seethroughskin.com/blog/?p=771
'''
import OpenGL 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import time, sys

class dizzyTea:

    global rotY

    def __init__(self):
        self.main()

    def InitGL(self,Width, Height):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glShadeModel(GL_SMOOTH)  
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()       
        gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)     

    # The main drawing function. 
    def DrawGLScene(self):
        global rotY
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()                    # Reset The View 
        glTranslatef(-0.5, 0.0, -6.0)
        glRotatef(rotY,0.0,1.0,0.0)
        glutWireTeapot(1.0)
        glScalef(0.3,0.3,0.3)
        glutSwapBuffers()
        rotY += 1.0

    # The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
    def keyPressed(self,*args):

        # If escape is pressed, kill everything.
        if args[0] == ' ':
            sys.exit()
        elif args[0] == 'm':
            print "Now meteoring otherwise peaceful teapot"
            # meteor shenanigans

    def main(self):
        global window
        global rotY
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(0, 0)
        window = glutCreateWindow("Jeff Molofee's desecrated GL Code Tutorial")
        glutDisplayFunc(self.DrawGLScene)
        glutIdleFunc(self.DrawGLScene)
        glutKeyboardFunc(self.keyPressed)
        self.InitGL(800, 600)
        rotY = 0.0
        glutMainLoop()

if __name__ == "__main__":
    x = dizzyTea()