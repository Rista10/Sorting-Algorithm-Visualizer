# visualizations/visualizer.py
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT.fonts import GLUT_BITMAP_HELVETICA_18
import random

class SortingVisualizer:
    def __init__(self, num_elements, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.num_elements = num_elements
        self.array_elements = []
        self.is_sorted = []
        self.sorter = None

    def generate_numbers(self):
        # Clear existing arrays
        self.array_elements.clear()
        self.is_sorted.clear()
        
        # Generate new random numbers
        for _ in range(self.num_elements):
            self.array_elements.append(random.random() * self.screen_height * 0.8)
            self.is_sorted.append(False)

    def set_sorter(self, sorter_class):
        # Generate numbers if not already done
        if not self.array_elements:
            self.generate_numbers()
        
        # Create sorter with current array
        self.sorter = sorter_class(self.array_elements)
        
        # Ensure is_sorted list is synchronized
        self.is_sorted = [False] * len(self.array_elements)
        self.array_elements = self.sorter.array

    def draw_bars(self):
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Ensure array and is_sorted are in sync
        if len(self.array_elements) != len(self.is_sorted):
            self.is_sorted = [False] * len(self.array_elements)
        
        quad_size = (self.screen_width - 2 * (self.num_elements + 1)) / self.num_elements

        for i in range(len(self.array_elements)):
            # Determine color based on state
            if i in self.sorter.current_comparing_indices:
                glColor3f(1.0, 1.0, 0.0)  # Yellow for comparison
            elif self.is_sorted[i]:
                glColor3f(0.0, 1.0, 0.0)  # Green for sorted
            else:
                glColor3f(1.0, 1.0, 1.0)  # White for unsorted

            # Draw bar
            glBegin(GL_POLYGON)
            glVertex2f(2 + i * (2 + quad_size), 0)
            glVertex2f(2 + i * (2 + quad_size), self.array_elements[i])
            glVertex2f(2 + i * (2 + quad_size) + quad_size, self.array_elements[i])
            glVertex2f(2 + i * (2 + quad_size) + quad_size, 0)
            glEnd()

        # Draw comparisons text
        glColor3f(1.0, 1.0, 1.0)
        self.draw_text(f"Comparisons: {self.sorter.comparisons}", 10, self.screen_height - 30)

    def draw_text(self, text, x, y):
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, self.screen_width, 0, self.screen_height)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        glRasterPos2f(x, y)
        for char in text:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)