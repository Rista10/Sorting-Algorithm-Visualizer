from OpenGL.GL import *
from OpenGL.GLUT import *
from utils.draw_text import draw_text

def draw_field(label, value, x, y, active):
    draw_text(label, x, y+50)
    glColor3f(0.6, 0.6, 0.6)  # More visible input fields
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x+250, y)  # Wider input box
    glVertex2f(x+250, y+50)  # Taller input box
    glVertex2f(x, y+50)
    glEnd()
    glColor3f(1, 1, 1)
    draw_text(value if value else label, x+10, y+20)  # Adjusted text position
    if active:
        draw_text('|', x+10 + len(value)*10, y+20)