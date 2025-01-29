import quicksort

class Submission(quicksort.QSortBase):
    def pivot(self, lo, hi, depth, breadth):        
        middle_index = lo + (hi - lo) // 2
        a, b, c = self.array[lo], self.array[middle_index], self.array[hi]

        # Find the median manually
        if (a <= b <= c) or (c <= b <= a):
            return b
        elif (b <= a <= c) or (c <= a <= b):
            return a
        else:
            return c
