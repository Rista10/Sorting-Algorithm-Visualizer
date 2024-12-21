from .base_sort import BaseSortAlgorithm

class InsertionSort(BaseSortAlgorithm):
    def __init__(self, array):
        super().__init__(array)
        self.sorting_state.update({
            'i': 1, 
            'j': 0, 
            'key': None, 
            'inner_loop_active': False 
        })
        self.is_sorted[0] = True

    def step_sort(self):
        if self.sorting_state['sorting_complete']:
            return

        i = self.sorting_state['i']
        j = self.sorting_state['j']

        if self.sorting_state['key'] is None:
            if i >= len(self.array):
                self.sorting_state['sorting_complete'] = True
                self.mark_sorted_elements()
                return
            
            self.sorting_state['key'] = self.array[i]
            self.sorting_state['j'] = i - 1
            self.sorting_state['inner_loop_active'] = True
            return

        if self.sorting_state['inner_loop_active']:
            if j >= 0 and self.sorting_state['key'] < self.array[j]:
                self.current_comparing_indices = (j, j + 1)
                self.comparisons += 1

                self.array[j + 1] = self.array[j]
                self.sorting_state['j'] -= 1
                return
            else:
                self.sorting_state['inner_loop_active'] = False
                return

        self.array[j + 1] = self.sorting_state['key']
        
        self.sorting_state['i'] += 1
        self.sorting_state['key'] = None
        self.current_comparing_indices = (-1, -1)
        self.mark_sorted_elements()

    def mark_sorted_elements(self):
        for k in range(self.sorting_state['i']):
            self.is_sorted[k] = True