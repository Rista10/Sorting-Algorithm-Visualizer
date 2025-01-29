from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLUT import GLUT_BITMAP_HELVETICA_18

def draw_text(text, x, y, font=GLUT_BITMAP_HELVETICA_18):  # Larger font
    glRasterPos2f(x, y)
    for c in text:
        glutBitmapCharacter(font, ord(c))