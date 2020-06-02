""""
KorKux Solution Module
"""
from typing import List


class Solution:
    """
    Class representing the challenge solution
    """
    def duplicate_zeros(self, arr: List[int]):
        """
        Given an array number doubles the zeros of the array without modifying the size of the array

        Arguments:
            arr {List[int]} -- [Array of numbers that will duplicate the zeros it contains]
        """
        i, j = 0, 0
        length = len(arr)
        while j < length:  # O(n)
            if arr[i] == 0:
                j += 1
            i += 1
            j += 1
        i -= 1

        if arr[i] != 0:
            j -= 1
        else:
            if j - 1 < length:
                arr[j-1] = 0
            arr[j-2] = 0
            i -= 1
            j -= 3

        while i >= 0: # O(n)
            if arr[i] == 0:
                arr[j] = 0
                arr[j-1] = 0
                j -= 2
                i -= 1
            else:
                arr[j] = arr[i]
                j -= 1
                i -= 1
        # Complex = O(n) + O(n) = O(2n) = O(n)
