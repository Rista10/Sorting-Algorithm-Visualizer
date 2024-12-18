# utils/window.py
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw

def init_window(width, height, title):
    if not glfw.init():
        return None
    
    window = glfw.create_window(width, height, title, None, None)
    if not window:
        glfw.terminate()
        return None
    
    glfw.make_context_current(window)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    
    return window