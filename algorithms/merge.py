# algorithms/merge.py
from .base_sort import BaseSortAlgorithm

class MergeSort(BaseSortAlgorithm):
    def __init__(self, array):
        super().__init__(array)
        self.sorting_state.update({
            'current_level': 1,
            'merge_start': 0
        })
        self.sorted_ranges = []

    def step_sort(self):
        # If sorting is complete, return True
        if self.sorting_state['sorting_complete']:
            self.mark_sorted_elements()
            return True

        # Merge sorting implementation with step-by-step state machine
        level = self.sorting_state['current_level']
        n = len(self.array)

        # If current merge level is larger than array length, sorting is complete
        if level > n:
            self.sorting_state['sorting_complete'] = True
            self.mark_sorted_elements()
            return True

        # Perform merging for the current level
        for start in range(0, n, 2 * level):
            left = start
            mid = min(start + level, n)
            right = min(start + 2 * level, n)

            # Merge two sorted subarrays
            self._merge(left, mid, right)
            
            # Track the sorted range
            self.sorted_ranges.append((left, right))

        # Update sorting state
        self.sorting_state['current_level'] *= 2
        self.sorting_state['merge_start'] = 0

        return False

    def _merge(self, left, mid, right):
        i, j, k = left, mid, left

        # Merge two sorted subarrays
        while i < mid and j < right:
            self.current_comparing_indices = (i, j)
            self.current_key_index = k
            self.comparisons += 1

            if self.array[i] <= self.array[j]:
                self.temp_array[k] = self.array[i]
                i += 1
            else:
                self.temp_array[k] = self.array[j]
                j += 1
            k += 1

        # Copy remaining elements from left subarray
        while i < mid:
            self.current_key_index = k
            self.temp_array[k] = self.array[i]
            i += 1
            k += 1

        # Copy remaining elements from right subarray
        while j < right:
            self.current_key_index = k
            self.temp_array[k] = self.array[j]
            j += 1
            k += 1

        # Copy back to original array
        for p in range(left, right):
            self.array[p] = self.temp_array[p]

    def mark_sorted_elements(self):
        # Mark elements as sorted based on the sorted ranges
        for start, end in self.sorted_ranges:
            for i in range(start, end):
                self.is_sorted[i] = True
        
        # Ensure full array is marked sorted at the end
        if self.sorting_state['sorting_complete']:
            for i in range(len(self.array)):
                self.is_sorted[i] = True