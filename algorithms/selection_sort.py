from .base_sort import BaseSortAlgorithm

class SelectionSort(BaseSortAlgorithm):
    def __init__(self, array):
        super().__init__(array)
        self.sorting_state.update({
            'i' : 0,
            'j': 1,
            "min_index": 0,
            'inner_loop_active': False
        })

    def step_sort(self):
        if self.sorting_state['sorting_complete']:
            return
        
        i = self.sorting_state['i']
        j = self.sorting_state['j']
        min_index = self.sorting_state['min_index']

        if j >= len(self.array):
            temp = self.array[i]
            self.array[i] = self.array[min_index]
            self.array[min_index] = temp

            self.sorting_state['i'] +=1

            if self.sorting_state['i'] >= len(self.array):
                self.sorting_state['sorting_completed'] = True
                self.mark_sorted_elements()
                return
            
            self.sorting_state['j'] = self.sorting_state['i'] + 1
            self.sorting_state['min_index'] = self.sorting_state['i']
            self.current_comparing_indices=(-1,-1)
            self.mark_sorted_elements()
            return

        self.current_comparing_indices=(min_index,j)
        self.comparisons += 1

        if self.array[j] < self.array[min_index]:
            self.sorting_state['min_index'] = j

        self.sorting_state['j'] += 1
        
    def mark_sorted_elements(self):
        for k in range(self.sorting_state['i']):
            self.is_sorted[k] = True