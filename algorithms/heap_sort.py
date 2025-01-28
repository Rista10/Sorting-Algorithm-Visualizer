from .base_sort import BaseSortAlgorithm

class HeapSort(BaseSortAlgorithm):
    def __init__(self, array):
        super().__init__(array)
        self.heap_size = len(array)
        # Initialize state for heapify and sorting phases
        self.sorting_state.update({
            'phase': 'build_heap',  # Phases: build_heap, extract_max
            'current_index': len(array) // 2 - 1,  # Start from last non-leaf node
            'heapify_stack': [],
            'sorted_boundary': len(array) - 1
        })

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
        
    def get_largest(self, i, heap_size):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < heap_size and self.array[left] > self.array[largest]:
            largest = left
            
        if right < heap_size and self.array[right] > self.array[largest]:
            largest = right
            
        return largest

    def step_heapify(self, i, heap_size):
        largest = self.get_largest(i, heap_size)
        
        if largest != i:
            self.swap(i, largest)
            return largest
        return None

    def step_sort(self):
        if self.sorting_state.get('sorting_complete', False):
            return True
            
        if self.sorting_state['phase'] == 'build_heap':
            # Building max heap phase
            if self.sorting_state['heapify_stack']:
                # Continue heapifying current node
                i = self.sorting_state['heapify_stack'][-1]
                next_i = self.step_heapify(i, self.heap_size)
                
                if next_i is None:
                    self.sorting_state['heapify_stack'].pop()
                else:
                    self.sorting_state['heapify_stack'].append(next_i)
            else:
                # Start heapifying new node
                if self.sorting_state['current_index'] >= 0:
                    self.sorting_state['heapify_stack'].append(self.sorting_state['current_index'])
                    self.sorting_state['current_index'] -= 1
                else:
                    # Finished building heap, move to extraction phase
                    self.sorting_state['phase'] = 'extract_max'
                    self.heap_size = len(self.array)
                    
        elif self.sorting_state['phase'] == 'extract_max':
            if self.sorting_state['heapify_stack']:
                # Continue heapifying after extraction
                i = self.sorting_state['heapify_stack'][-1]
                next_i = self.step_heapify(i, self.heap_size)
                
                if next_i is None:
                    self.sorting_state['heapify_stack'].pop()
                else:
                    self.sorting_state['heapify_stack'].append(next_i)
            else:
                # Extract maximum element
                if self.heap_size > 1:
                    self.swap(0, self.heap_size - 1)
                    self.is_sorted[self.heap_size - 1] = True
                    self.heap_size -= 1
                    self.sorting_state['heapify_stack'].append(0)
                else:
                    # Mark first element as sorted and complete sorting
                    self.is_sorted[0] = True
                    self.sorting_state['sorting_complete'] = True
                    
        return self.sorting_state['sorting_complete']

    def mark_sorted_elements(self):
        for i in range(len(self.array)):
            self.is_sorted[i] = True