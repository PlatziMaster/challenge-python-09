"""Solution module"""
from typing import List


class Solution:
    """Class solution of challenge """

    def duplicate_zeros(self, arr: List[int]):
        """Duplicate the zeros in a list"""
        zeros = 0
        last_index = 0

        arr_len = len(arr)
        for index, item in enumerate(arr):
            if item == 0:
                if index + zeros + 1 < arr_len:
                    zeros += 1
                    last_index = index
                else:
                    break

        index = arr_len - 1

        while zeros > 0 and index - zeros >= 0:
            arr[index] = arr[index - zeros]

            if arr[index - zeros] == 0 and index - zeros <= last_index:
                arr[index - 1] = 0
                zeros -= 1
                index -= 1
            index -= 1
