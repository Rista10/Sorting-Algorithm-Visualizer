# main.py
import pygame
import sys
import glfw
from OpenGL.GLUT.special import glutInit
from OpenGL.GLUT import *
import time

from algorithms.heap_sort import HeapSort
from algorithms.quick_sort import QuickSort
from algorithms.selection_sort import SelectionSort
from utils.window import init_window
from visualizations.visualizer import SortingVisualizer
from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort

# Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

def main():
    try:
        user_config = {
            'num_elements': 100,
            'algorithm': 'Insertion Sort',
            'update_interval': 0.01
        }
    except Exception:
        print("Visualization setup cancelled.")
        return

    window = init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Sorting Algorithm Visualizer")
    if window is None:
        return

    glutInit()

    visualizer = SortingVisualizer(
        num_elements=user_config['num_elements'],
        screen_width=SCREEN_WIDTH,
        screen_height=SCREEN_HEIGHT
    )

    # Initialize the selected sorting algorithm
    if user_config['algorithm'] == 'Insertion Sort':
        visualizer.set_sorter(InsertionSort)
    elif user_config['algorithm'] == "Merge Sort":
        visualizer.set_sorter(MergeSort)
    elif user_config['algorithm'] == "Selection Sort":
        visualizer.set_sorter(SelectionSort)
    elif user_config['algorithm'] == "Quick Sort":
        visualizer.set_sorter(QuickSort)
    elif user_config['algorithm'] == "Heap Sort":
        visualizer.set_sorter(HeapSort)

    # Keep track of last update time
    last_update = time.time()

    while not glfw.window_should_close(window):
        current_time = time.time()

        # Check if it's time for the next update
        if current_time - last_update >= user_config['update_interval']:
            # Perform one step of sorting if not complete
            if not visualizer.sorter.sorting_state['sorting_complete']:
                visualizer.sorter.step_sort()
                # Update the visualization's sorted status
                visualizer.is_sorted = visualizer.sorter.is_sorted
                last_update = current_time

        # Clear and draw current state
        visualizer.draw_bars()
        
        # Swap buffers to display the new frame
        glfw.swap_buffers(window)
        
        # Process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()