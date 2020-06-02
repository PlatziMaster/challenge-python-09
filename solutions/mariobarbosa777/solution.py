"""This module has the solution"""

from typing import List

class Solution:
    """This class has the solution"""
    def duplicate_zeros(self, arr: List[int]):
        """This fuction has the solution"""
        zeros = 0
        last_index = 0
        len_arr = len(arr)
        for index in range(len_arr-1):
            if arr[index] == 0 and index + zeros + 1 < len_arr:
                zeros += 1
                last_index = index
        index = len_arr - 1
        while zeros > 0 and index - zeros >= 0:
            arr[index] = arr[index - zeros]
            if arr[index - zeros] == 0 and index - zeros <= last_index:
                zeros -= 1
                index -= 1
                arr[index] = 0
            index -= 1
            