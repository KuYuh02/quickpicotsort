import quicksort

class Submission(quicksort.QSortBase):
    def pivot(self, lo, hi, depth, breadth):        
        middle_index = lo + (hi - lo) // 2
        values = [self.array[lo], self.array[middle_index], self.array[hi]]
        
        # Sort the three values and return the median
        values.sort()
        
        return values[1]
