SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

# Color scheme
COLORS = {
    'primary': (0.2, 0.6, 1.0),    # Blue
    'secondary': (0.3, 0.3, 0.3),  # Dark gray
    'background': (0.95, 0.95, 0.95),  # Light gray
    'white': (1.0, 1.0, 1.0),
    'text': (0.2, 0.2, 0.2),       # Dark text
    'error': (0.8, 0.2, 0.2),      # Red
    'success': (0.2, 0.7, 0.2),    # Green
    'hover': (0.25, 0.65, 1.0)     # Lighter blue
}

# UI state
algorithm_options = ['Insertion Sort', 'Merge Sort', 'Selection Sort', 'Quick Sort', 'Heap Sort']
algorithm_descriptions = {
        'Insertion Sort': 'Best for small or nearly sorted data (O(n²))',
        'Merge Sort': 'Stable, efficient for large datasets (O(n log n))',
        'Selection Sort': 'Simple but inefficient (O(n²))',
        'Quick Sort': 'Fastest in practice for large datasets (O(n log n))',
        'Heap Sort': 'Efficient, in-place sorting (O(n log n))'
    }

input_fields = {'num_elements': '100', 'update_interval': '0.01'}
