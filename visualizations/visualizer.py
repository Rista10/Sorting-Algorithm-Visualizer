from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT.fonts import GLUT_BITMAP_HELVETICA_18, GLUT_BITMAP_TIMES_ROMAN_24
import random

class SortingVisualizer:
    def __init__(self, num_elements, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.num_elements = num_elements
        self.array_elements = []
        self.is_sorted = []
        self.sorter = None
        self.algorithm_name = ""
        self.show_back_button = True
        self.back_button_clicked = False
        
        # Colors for UI elements
        self.colors = {
            'primary': (0.2, 0.6, 1.0),    # Blue
            'white': (1.0, 1.0, 1.0),
            'yellow': (1.0, 1.0, 0.0),
            'green': (0.0, 1.0, 0.0),
            'hover': (0.25, 0.65, 1.0)     # Lighter blue
        }

    def generate_numbers(self):
        # Clear existing arrays
        self.array_elements.clear()
        self.is_sorted.clear()
        
        # Generate new random numbers
        for _ in range(self.num_elements):
            self.array_elements.append(random.random() * self.screen_height * 0.7)  # Reduced height to make room for UI
            self.is_sorted.append(False)

    def set_sorter(self, sorter_class, algorithm_name):
        # Generate numbers if not already done
        if not self.array_elements:
            self.generate_numbers()
        
        # Create sorter with current array
        self.sorter = sorter_class(self.array_elements)
        self.algorithm_name = algorithm_name
        
        # Ensure is_sorted list is synchronized
        self.is_sorted = [False] * len(self.array_elements)
        self.array_elements = self.sorter.array

    def draw_navbar(self):
        """Draw a website-like navigation bar"""
        # Nav background
        glColor3f(*self.colors['primary'])
        glBegin(GL_QUADS)
        glVertex2f(0, self.screen_height - 60)
        glVertex2f(self.screen_width, self.screen_height - 60)
        glVertex2f(self.screen_width, self.screen_height)
        glVertex2f(0, self.screen_height)
        glEnd()



        # Draw algorithm name
        glColor3f(*self.colors['white'])
        self.draw_text(f"Algorithm: {self.algorithm_name}", 100, self.screen_height - 35, GLUT_BITMAP_TIMES_ROMAN_24)

    def draw_stats_panel(self):
            """Draw statistics panel"""
            # Stats background
            glColor3f(*self.colors['primary'])
            glBegin(GL_QUADS)
            glVertex2f(10, self.screen_height - 100)
            glVertex2f(250, self.screen_height - 100)
            glVertex2f(250, self.screen_height - 180)
            glVertex2f(10, self.screen_height - 180)
            glEnd()

            # Stats text
            curr_algo = "Algorithm: " + self.algorithm_name
            self.draw_text(curr_algo, 20, self.screen_height - 80, GLUT_BITMAP_TIMES_ROMAN_24)
            glColor3f(*self.colors['white'])
            self.draw_text(f"Comparisons: {self.sorter.comparisons}", 20, self.screen_height - 125, GLUT_BITMAP_HELVETICA_18)
            progress = sum(self.is_sorted) / len(self.is_sorted) * 100
            self.draw_text(f"Progress: {progress:.1f}%", 20, self.screen_height - 150, GLUT_BITMAP_HELVETICA_18)

    def draw_bars(self):
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Ensure array and is_sorted are in sync
        if len(self.array_elements) != len(self.is_sorted):
            self.is_sorted = [False] * len(self.array_elements)
        
        # Draw visualization area background
        glColor3f(0.1, 0.1, 0.1)  # Dark background
        glBegin(GL_QUADS)
        glVertex2f(0, 0)
        glVertex2f(self.screen_width, 0)
        glVertex2f(self.screen_width, self.screen_height - 60)
        glVertex2f(0, self.screen_height - 60)
        glEnd()

        quad_size = (self.screen_width - 2 * (self.num_elements + 1)) / self.num_elements
        
        for i in range(len(self.array_elements)):
            # Determine color based on state
            if i in self.sorter.current_comparing_indices:
                glColor3f(*self.colors['yellow'])  # Yellow for comparison
            elif self.is_sorted[i]:
                glColor3f(*self.colors['green'])  # Green for sorted
            else:
                glColor3f(*self.colors['white'])  # White for unsorted
            
            # Draw bar
            glBegin(GL_POLYGON)
            glVertex2f(2 + i * (2 + quad_size), 0)
            glVertex2f(2 + i * (2 + quad_size), self.array_elements[i])
            glVertex2f(2 + i * (2 + quad_size) + quad_size, self.array_elements[i])
            glVertex2f(2 + i * (2 + quad_size) + quad_size, 0)
            glEnd()

        # Draw UI elements
        self.draw_navbar()
        self.draw_stats_panel()

    def draw_text(self, text, x, y, font=GLUT_BITMAP_HELVETICA_18):
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, self.screen_width, 0, self.screen_height)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        
        glRasterPos2f(x, y)
        for char in text:
            glutBitmapCharacter(font, ord(char))
        
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

