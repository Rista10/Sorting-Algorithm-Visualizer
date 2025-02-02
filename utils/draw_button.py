from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_button(x, y, width, height):
    """Draw a simple rectangle to simulate web-like buttons"""
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()