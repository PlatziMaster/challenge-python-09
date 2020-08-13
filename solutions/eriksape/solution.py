"""Solution module"""
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
        index = 0
        zeroes = 0
        limit = len(arr) - 1
        while index + zeroes < limit:
            if arr[index] == 0:
                zeroes += 1
            index += 1
        while limit - zeroes >= 0 and zeroes >= 0:
            arr[limit] = arr[limit - zeroes]
            if arr[limit] == 0 and limit - zeroes < index:
                arr[limit - 1] = 0
                limit -= 1
                zeroes -= 1
            limit -= 1
        return arr
