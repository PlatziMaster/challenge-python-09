'''Module to create a solution from an expected matrix
duplicate the zeros in the array, return a modified array.'''
from typing import List

class Solution:
    """ The class contain the function that job with the array,
     each zero finding in the array duplicate itself"""
    def duplicate_zeros(self, arr: List[int]):
        """The function take an array and in O(n) execution time and in place modification,
        Return an array with duplicated zeros and deleted the values to the left for each one."""
        i = 0
        j = len(arr) - 1
        zero = 0
        while j > i and len(arr) > 1:
            if arr[i] == 0:
                zero += 1
                i += 1
                j -= 1
            else:
                i += 1
        length = len(arr) -1
        while j >= 0:
            arr[length] = arr[j]
            j -= 1
            length -= 1
        if zero > 0:
            for i in range(0, zero):
                arr[i] = 0
        ind_r = 0
        ind_sw = length + 1
        while ind_sw < len(arr) and zero > 0:
            if arr[ind_sw] == 0:
                zero -= 1
                arr[ind_sw], arr[ind_r] = arr[ind_r], arr[ind_sw]
                ind_sw += 1
                ind_r += 2
            else:
                arr[ind_sw], arr[ind_r] = arr[ind_r], arr[ind_sw]
                ind_r += 1
                ind_sw += 1
        return arr
        