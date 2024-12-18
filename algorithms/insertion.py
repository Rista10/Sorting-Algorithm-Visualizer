# algorithms/insertion.py
from .base_sort import BaseSortAlgorithm

class InsertionSort(BaseSortAlgorithm):
    def __init__(self, array):
        super().__init__(array)
        self.sorting_state.update({
            'current_pass': 0,
            'current_index': 1,
            'inner_index': 0,
            'key': None
        })

    def step_sort(self):
        # State machine for insertion sort
        if self.sorting_state['sorting_complete']:
            self.mark_sorted_elements()
            return True

        # Mark first element as sorted
        if self.sorting_state['current_pass'] == 0:
            self.is_sorted[0] = True

        # Check if we've gone through all passes
        if self.sorting_state['current_index'] >= len(self.array):
            self.sorting_state['sorting_complete'] = True
            self.mark_sorted_elements()
            return True

        # Get the current key
        if self.sorting_state['key'] is None:
            self.sorting_state['key'] = self.array[self.sorting_state['current_index']]
            self.sorting_state['inner_index'] = self.sorting_state['current_index'] - 1
            self.current_key_index = self.sorting_state['current_index']

        # Inner loop of insertion sort
        if (self.sorting_state['inner_index'] >= 0 and 
            self.array[self.sorting_state['inner_index']] > self.sorting_state['key']):
            # Update current comparing indices
            self.current_comparing_indices = (
                self.sorting_state['inner_index'], 
                self.sorting_state['inner_index'] + 1
            )
            
            # Shift elements
            self.array[self.sorting_state['inner_index'] + 1] = \
                self.array[self.sorting_state['inner_index']]
            self.sorting_state['inner_index'] -= 1
            self.comparisons += 1
            return False

        # Place the key in its correct position
        self.array[self.sorting_state['inner_index'] + 1] = self.sorting_state['key']
        
        # Reset comparing indices
        self.current_comparing_indices = (-1, -1)
        self.current_key_index = -1

        # Move to next pass
        self.sorting_state['current_index'] += 1
        self.sorting_state['key'] = None

        return False

    def mark_sorted_elements(self):
        # Mark elements as sorted up to the current index
        for i in range(self.sorting_state['current_index']):
            self.is_sorted[i] = True