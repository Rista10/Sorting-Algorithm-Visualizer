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
        pass

    def _merge(self, left, mid, right):
        pass

    def mark_sorted_elements(self):
        pass