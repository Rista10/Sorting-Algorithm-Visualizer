from OpenGL.GL import *
from OpenGL.GLUT import *
from utils.draw_text import draw_text
from constants import  *

def draw_navbar():
    """Draw a navigation bar"""
    glColor3f(*COLORS['primary'])
    glBegin(GL_QUADS)
    glVertex2f(0, SCREEN_HEIGHT - 60)
    glVertex2f(SCREEN_WIDTH, SCREEN_HEIGHT - 60)
    glVertex2f(SCREEN_WIDTH, SCREEN_HEIGHT)
    glVertex2f(0, SCREEN_HEIGHT)
    glEnd()
    
    glColor3f(*COLORS['white'])
    draw_text("Sorting Algorithm Visualizer", 20, SCREEN_HEIGHT - 40, GLUT_BITMAP_TIMES_ROMAN_24)