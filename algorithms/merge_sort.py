from .base_sort import BaseSortAlgorithm

class MergeSort(BaseSortAlgorithm):
    def __init__(self, array):
        super().__init__(array)
        self.sorting_state.update({
            'recursion_stack': [('split', 0, len(array) - 1)],  # Stack to track recursive calls
            'completed_ranges': set()  # Track completed merge operations
        })
        self.sorted_ranges = []

    def step_sort(self):
        # If sorting is complete, return True
        if not self.sorting_state['recursion_stack']:
            self.sorting_state['sorting_complete'] = True
            self.mark_all_sorted()
            return True

        # Get the current operation from the stack
        operation = self.sorting_state['recursion_stack'][-1][0]
        
        if operation == 'split':
            return self._handle_split_phase()
        else:  # merge phase
            return self._handle_merge_phase()

    def _handle_split_phase(self):
        # Get current range from call stack
        _, left, right = self.sorting_state['recursion_stack'].pop()

        # Base case: single element
        if left >= right:
            # Mark single element as sorted
            self.is_sorted[left] = True
            return False

        # Calculate mid point
        mid = (left + right) // 2

        # Push operations onto stack in reverse order of execution
        self.sorting_state['recursion_stack'].append(('merge', left, mid, right))
        self.sorting_state['recursion_stack'].append(('split', mid + 1, right))
        self.sorting_state['recursion_stack'].append(('split', left, mid))
        

    def _handle_merge_phase(self):
        # Get merge operation details
        _, left, mid, right = self.sorting_state['recursion_stack'].pop()
        
        # Skip if this range was already merged
        merge_key = (left, right)
        if merge_key in self.sorting_state['completed_ranges']:
            return False

        # Perform merge operation
        self._merge(left, mid, right)
        
        # Mark this range as merged and sorted
        self.sorting_state['completed_ranges'].add(merge_key)
        
        return False

    def _merge(self, left, mid, right):
        # Calculate sizes of two subarrays
        size_of_la = mid - left + 1
        size_of_ra = right - mid

        # Create temporary arrays
        left_array = [0] * size_of_la
        right_array = [0] * size_of_ra

        # Copy data to temporary arrays
        for i in range(size_of_la):
            left_array[i] = self.array[left + i]

        for i in range(size_of_ra):
            right_array[i] = self.array[mid + 1 + i]

        # Merge the temporary arrays back into array[left..right]
        i = 0  # Initial index of left subarray
        j = 0  # Initial index of right subarray
        k = left  # Initial index of merged subarray

        while i < size_of_la and j < size_of_ra:
            self.comparisons += 1
            
            if left_array[i] <= right_array[j]:
                self.array[k] = left_array[i]
                i += 1
            else:
                self.array[k] = right_array[j]
                j += 1
            k += 1

        # Copy remaining elements of left_array if any
        while i < size_of_la:
            self.array[k] = left_array[i]
            i += 1
            k += 1

        # Copy remaining elements of right_array if any
        while j < size_of_ra:
            self.array[k] = right_array[j]
            j += 1
            k += 1

        self.mark_range_sorted(left, right + 1)

    def mark_range_sorted(self, start, end):
        """Mark a range of elements as sorted"""
        for i in range(start, end):
            self.is_sorted[i] = True
            
    def mark_all_sorted(self):
        """Mark all elements as sorted"""
        for i in range(len(self.array)):
            self.is_sorted[i] = True