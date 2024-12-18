# algorithms/base_sort.py
class BaseSortAlgorithm:
    def __init__(self, array):
        self.array = array
        self.comparisons = 0
        self.is_sorted = [False] * len(array)
        self.sorting_state = {
            'sorting_complete': False
        }
        self.current_comparing_indices = (-1, -1)
        self.current_key_index = -1
        self.temp_array = array.copy()

    def step_sort(self):
        """Must be implemented by child classes"""
        raise NotImplementedError("Subclasses must implement step_sort method")

    def mark_sorted_elements(self):
        """
        Method to be overridden by specific sorting algorithms 
        to mark which elements are sorted during the sorting process
        """
        pass