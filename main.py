from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
import random
import time

# constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

# variables
array_elements = []
is_sorted = []
num_elements = 10
s_time = 0.5
comparisons = 0

def init_window():
    if not glfwInit():
        return None
    
    window = glfwCreateWindow(SCREEN_WIDTH,SCREEN_HEIGHT,"Sorting ALgorithm Visualizer",None,None)

    if not window:
        glfwTerminate()
        return None
    
    glfwMakeContextCurrent(window)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,SCREEN_WIDTH,0,SCREEN_HEIGHT)
    glMatrixMode(GL_MODELVIEW)

    return window
    

def generate_numbers():
    global array_elements, is_sorted
    is_sorted.clear()
    array_elements.clear()
    
    for i in range(num_elements):
        array_elements.append(random.random() * SCREEN_HEIGHT * 0.8)
        is_sorted.append(False)

def draw_bars(x,y):
    glClear(GL_COLOR_BUFFER_BIT)
    quad_size = (SCREEN_WIDTH -2 * (num_elements + 1))/num_elements

    for i in range(num_elements):
        if(i==x or i==y):
            glColor3f(1.0,0.0,0.0)
        elif (is_sorted[i]):
            glColor3f(0.0,1.0,0.0)
        else:
            glColor3f(1.0,1.0,1.0)

        glBegin(GL_POLYGON)
        glVertex2f(2 + i * (2 + quad_size),0)
        glVertex2f(2 + i * (2 + quad_size),array_elements[i])
        glVertex2f(2 + i * (2 + quad_size) + quad_size,array_elements[i])
        glVertex2f(2 + i * (2 + quad_size) + quad_size,0)
        glEnd()

def insertion_sort(window):
    global comparisons
    is_sorted[0] = True
    draw_bars(-1, -1)
    glfwSwapBuffers(window)  

    for i in range(1, num_elements):
        key = array_elements[i]
        j = i - 1
        while j >= 0 and array_elements[j] > key:
            draw_bars(j, j + 1)
            glfwSwapBuffers(window)  
            time.sleep(s_time)
            array_elements[j + 1] = array_elements[j]
            array_elements[j] = key
            j -= 1
            comparisons += 1
            draw_bars(-1,-1)
            time.sleep(s_time)

        array_elements[j+1] = key
        is_sorted[j+1] = True
        draw_bars(-1,-1) 
        time.sleep(s_time)           

def main():
    window = init_window()

    if window is None:
        return
    
    generate_numbers()
    
    while not glfwWindowShouldClose(window):
        glfwPollEvents()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
       
        insertion_sort(window)

        glfwSwapBuffers(window)

    glfwTerminate()
    

if __name__ == "__main__":
    main()


