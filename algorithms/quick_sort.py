from .base_sort import BaseSortAlgorithm

class QuickSort(BaseSortAlgorithm):
    def __init__(self, array):
        super().__init__(array)
        # Initialize state to start partitioning from the full array
        self.sorting_state.update({
            'recursion_stack': [(0, len(array) - 1)],  # Stack of (low, high) ranges
            'partition_state': None,  # Will hold state during partitioning
            'current_operation': 'start_partition'  # Possible states: start_partition, partitioning, finish_partition
        })

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def step_sort(self):
        if not self.sorting_state['recursion_stack']:
            self.sorting_state['sorting_complete'] = True
            self.mark_sorted_elements()
            return True

        if self.sorting_state['current_operation'] == 'start_partition':
            # Initialize a new partition operation
            low, high = self.sorting_state['recursion_stack'][-1]
            self.sorting_state['partition_state'] = {
                'low': low,
                'high': high,
                'pivot': self.array[high],
                'i': low - 1,
                'j': low
            }
            self.sorting_state['current_operation'] = 'partitioning'
            return False

        elif self.sorting_state['current_operation'] == 'partitioning':
            # Continue partitioning process
            state = self.sorting_state['partition_state']
            
            # If we haven't finished scanning the array
            if state['j'] < state['high']:
                self.current_comparing_indices=(state['j'],state['high'])
                if self.array[state['j']] < state['pivot']:
                    state['i'] += 1
                    self.swap(state['i'], state['j'])
                state['j'] += 1
                return False
            else:
                # Finished scanning, place pivot in correct position
                pivot_position = state['i'] + 1
                self.swap(state['high'], pivot_position)
                self.is_sorted[pivot_position] = True  # Mark pivot as sorted
                
                # Set up recursive calls
                low, high = self.sorting_state['recursion_stack'].pop()
                
                # Add subarrays to recursion stack (if they exist)
                if pivot_position + 1 < high:
                    self.sorting_state['recursion_stack'].append(
                        (pivot_position + 1, high))
                if low < pivot_position - 1:
                    self.sorting_state['recursion_stack'].append(
                        (low, pivot_position - 1))
                
                self.sorting_state['current_operation'] = 'start_partition'
                return False

        return False

    def mark_sorted_elements(self):
        """Mark all elements as sorted when the algorithm completes"""
        for i in range(len(self.array)):
            self.is_sorted[i] = True

    def is_element_sorted(self, index):
        """Check if an element at the given index is in its final sorted position"""
        return self.is_sorted[index]