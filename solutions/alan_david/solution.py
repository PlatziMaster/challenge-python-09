""" AlanDavd's solution """
from typing import List


class Solution:
    """ Duplicate zeros in-place class
        This function returns nothing.
    """

    def duplicate_zeros(self, arr: List[int]):
        """ Duplicate zeros in an array with fixed length """
        zeros = 0
        array_length = len(arr) - 1

        # Recollect the amount of 0 occurrences
        for item in range(array_length + 1):
            # Prevent counting zeros that won't be in array while duplicating
            if item > array_length - zeros:
                break

            if arr[item] == 0:
                # There's no more space, item is the last element that could be included
                if item == array_length - zeros:
                    arr[array_length] = 0
                    array_length -= 1
                    break
                zeros += 1

        last_zero = array_length - zeros

        # From right to left
        for item in range(last_zero, -1, -1):
            if arr[item] == 0:
                arr[item + zeros] = 0
                zeros -= 1
                arr[item + zeros] = 0
            else:
                arr[item + zeros] = arr[item]
