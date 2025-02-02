import glfw
import time
from constants import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLUT import GLUT_BITMAP_HELVETICA_18, GLUT_BITMAP_TIMES_ROMAN_24

from algorithms.heap_sort import HeapSort
from algorithms.quick_sort import QuickSort
from algorithms.selection_sort import SelectionSort
from utils.draw_text import draw_text
from utils.window import init_window
from visualizations.visualizer import SortingVisualizer
from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort
from utils.draw_button import draw_button
from utils.draw_navbar import draw_navbar
from utils.draw_selection_menu import draw_menu


def main():
    while True:
        window = init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Sorting Algorithm Visualizer")
        
        if window is None:
            return

        selected_algorithm = 0
        active_input_field = None
        start_button_clicked = False
        error_message = ''
        char_buffer = []
        backspace_pressed = False

        # GLFW callbacks (same as before)
        def on_char(window, codepoint):
            char_buffer.append(chr(codepoint))
        glfw.set_char_callback(window, on_char)

        def on_key(window, key, scancode, action, mods):
            nonlocal backspace_pressed, start_button_clicked
            if key == glfw.KEY_BACKSPACE and action == glfw.PRESS:
                backspace_pressed = True
            elif key == glfw.KEY_R and action == glfw.PRESS:
                start_button_clicked = False  # Reset to go back to home

        glfw.set_key_callback(window, on_key)

        # UI loop
        while not glfw.window_should_close(window) and not start_button_clicked:
            glfw.poll_events()

            if glfw.window_should_close(window):  
                 glfw.terminate()
                 exit()

            
            # Handle input (same mouse and keyboard handling as before)
            if glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS:
                xpos, ypos = glfw.get_cursor_pos(window)
                ypos = SCREEN_HEIGHT - ypos  # Convert to OpenGL coords

                # Check algorithm selection
                algo_y = 620
                for i, algo in enumerate(algorithm_options):
                    if 40 <= xpos <= 300 and (algo_y - 25) <= ypos <= (algo_y + 15):
                        selected_algorithm = i
                    algo_y -= 60

                # Check input fields
                y_pos = 620
                if 360 <= xpos <= 720 and 580 <= ypos <= 610:
                    active_input_field = 'num_elements'
                elif 360 <= xpos <= 720 and 500 <= ypos <= 530:
                    active_input_field = 'update_interval'
                else:
                    active_input_field = None

                # Check start button
                if 340 <= xpos <= 640 and 350 <= ypos <= 390:
                    try:
                        num = int(input_fields['num_elements'])
                        interval = float(input_fields['update_interval'])
                        if num <= 0 or interval <= 0:
                            raise ValueError
                        start_button_clicked = True
                        error_message = ''
                    except ValueError:
                        error_message = 'Invalid input! Must be positive numbers.'

            # Handle keyboard input
            if backspace_pressed and active_input_field:
                input_fields[active_input_field] = input_fields[active_input_field][:-1]
                backspace_pressed = False

            for char in char_buffer:
                if active_input_field == 'num_elements' and char.isdigit():
                    input_fields['num_elements'] += char
                elif active_input_field == 'update_interval':
                    if char.isdigit() or (char == '.' and '.' not in input_fields['update_interval']):
                        input_fields['update_interval'] += char
            char_buffer.clear()

            
            # Render web-styled UI
            glClearColor(*COLORS['background'], 1.0)
            glClear(GL_COLOR_BUFFER_BIT)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT, -1, 1)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

            # Draw navbar
            draw_navbar()

            # Main content area
            # Algorithm selection card
            draw_menu(20, 300, 300, 400, "Select Algorithm")
            algo_y = 620
            for i, algo in enumerate(algorithm_options):
                if i == selected_algorithm:
                    glColor3f(*COLORS['primary'])
                    draw_button(40, algo_y - 25, 260, 40)
                    glColor3f(*COLORS['white'])
                else:
                    glColor3f(*COLORS['text'])
                draw_text(algo, 50, algo_y, GLUT_BITMAP_HELVETICA_18)
                if i == selected_algorithm:
                    glColor3f(*COLORS['white'])
                    draw_text(algorithm_descriptions[algo], 50, algo_y - 20, GLUT_BITMAP_HELVETICA_18)
                algo_y -= 60

            # Configuration card
            draw_menu(340, 300, 400, 400, "Configuration")
            
            # Input fields with modern styling
            glColor3f(*COLORS['text'])
            y_pos = 620
            # Number of Elements input field
            draw_text("Number of Elements", 360, 620, GLUT_BITMAP_HELVETICA_18)
            if active_input_field == 'num_elements':
                glColor3f(*COLORS['primary'])
            else:
                glColor3f(*COLORS['secondary'])
            draw_button(360, 580, 360, 30)
            glColor3f(*COLORS['white'])
            draw_text(input_fields['num_elements'], 370, 590, GLUT_BITMAP_HELVETICA_18)
            
            # Update Interval input field
            glColor3f(*COLORS['text'])
            draw_text("Update Interval (s)", 360, 540, GLUT_BITMAP_HELVETICA_18)
            if active_input_field == 'update_interval':
                glColor3f(*COLORS['primary'])
            else:
                glColor3f(*COLORS['secondary'])
            draw_button(360, 500, 360, 30)
            glColor3f(*COLORS['white'])
            draw_text(input_fields['update_interval'], 370, 510, GLUT_BITMAP_HELVETICA_18)

            # Start button with web-like styling
            xpos, ypos = glfw.get_cursor_pos(window)
            ypos = SCREEN_HEIGHT - ypos
            
            if 340 <= xpos <= 640 and 350 <= ypos <= 390:
                glColor3f(*COLORS['hover'])
            else:
                glColor3f(*COLORS['primary'])
            
            draw_button(340, 350, 400, 40)
            glColor3f(*COLORS['white'])
            draw_text("Start Visualization", 370, 365, GLUT_BITMAP_HELVETICA_18)

            # Error message
            if error_message:
                glColor3f(*COLORS['error'])
                draw_text(error_message, 340, 320, GLUT_BITMAP_HELVETICA_18)

            glfw.swap_buffers(window)

        # Visualization logic
        if start_button_clicked:
            user_config = {
                'num_elements': int(input_fields['num_elements']),
                'algorithm': algorithm_options[selected_algorithm],
                'update_interval': float(input_fields['update_interval'])
            }

            visualizer = SortingVisualizer(
                num_elements=user_config['num_elements'],
                screen_width=SCREEN_WIDTH,
                screen_height=SCREEN_HEIGHT
            )


            # Set up visualizer and sorting algorithm (same as before)
            if user_config['algorithm'] == 'Insertion Sort':
                visualizer.set_sorter(InsertionSort,"Insertion Sort")
            elif user_config['algorithm'] == "Merge Sort":
                visualizer.set_sorter(MergeSort,"Merge Sort")
            elif user_config['algorithm'] == "Selection Sort":
                visualizer.set_sorter(SelectionSort,"Selection Sort")
            elif user_config['algorithm'] == "Quick Sort":
                visualizer.set_sorter(QuickSort,"Quick Sort")
            elif user_config['algorithm'] == "Heap Sort":
                visualizer.set_sorter(HeapSort,"Heap Sort")

            

            # Visualization loop with web-styled overlay
            last_update = time.time()
            while not glfw.window_should_close(window):
                current_time = time.time()

                if glfw.get_key(window, glfw.KEY_R) == glfw.PRESS:
                    start_button_clicked = False  # Reset to return to selection screen
                    break

                if current_time - last_update >= user_config['update_interval']:
                    if not visualizer.sorter.sorting_state['sorting_complete']:
                        visualizer.sorter.step_sort()
                        visualizer.is_sorted = visualizer.sorter.is_sorted
                        last_update = current_time

                visualizer.draw_bars()
                draw_navbar()

                glfw.swap_buffers(window)
                glfw.poll_events()

        glfw.destroy_window(window)

if __name__ == "__main__":
    main()