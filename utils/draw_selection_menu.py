from OpenGL.GL import *
from OpenGL.GLUT import *
from utils.draw_text import draw_text
from constants import  *
from utils.draw_button import draw_button

def draw_menu(x, y, width, height, title):
    """Draw a web-like card component"""
    # Card background
    glColor3f(*COLORS['white'])
    draw_button(x, y, width, height)
    
    # Card title
    glColor3f(*COLORS['primary'])
    draw_text(title, x + 20, y + height - 30, GLUT_BITMAP_HELVETICA_18)
    
    # Separator line
    glColor3f(0.9, 0.9, 0.9)
    glBegin(GL_LINES)
    glVertex2f(x + 10, y + height - 40)
    glVertex2f(x + width - 10, y + height - 40)
    glEnd()