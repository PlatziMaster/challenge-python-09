"""Challenge 9"""
from typing import List


class Solution:
    """Class of challenge solution."""

    def duplicate_zeros(self, arr: List[int]):
        """Function that duplicates 0s without altering the memory used."""
        count_zeros = 0
        array_len = len(arr)
        secure_zone_to_write = -1
        for i, v in enumerate(arr):
            if v == 0:
                secure_zone_to_write = i if secure_zone_to_write == -1 else secure_zone_to_write
                if i + count_zeros + 1 < array_len:
                    count_zeros += 1
                else:
                    break
        final_array_index = array_len - 1
        index = final_array_index - count_zeros
        secure_zone_to_write = secure_zone_to_write + (count_zeros * 2)
        while index >= 0:
            if arr[index] != 0:
                arr[final_array_index] = arr[index]
                final_array_index -= 1
            else:
                if final_array_index == array_len-1 and (array_len - secure_zone_to_write) % 2 == 1:
                    arr[final_array_index] = 0
                    final_array_index -= 1
                    count_zeros -= 1
                else:
                    arr[final_array_index] = 0
                    arr[final_array_index-1] = 0
                    final_array_index -= 2
                    count_zeros -= 1
            index -= 1
