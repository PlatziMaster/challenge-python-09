"""Challenge-python-09"""
from typing import List

class Solution:
    """Solición al reto"""
    def duplicate_zeros(self, arr: List[int]):
        """Función que duplica los ceros en una lista"""
        zeros = 0
        last = 0
        len_arr = len(arr)
        for idx, value in enumerate(arr):
            if value == 0 and idx + zeros < len_arr - 1:
                zeros += 1
                last = idx
        idx = len_arr - 1
        for _ in arr:
            if idx == 0:
                break
            if zeros > 0 and idx - zeros >= 0:
                arr[idx] = arr[idx - zeros]
                if arr[idx - zeros] == 0 and idx - zeros <= last:
                    idx -= 1
                    arr[idx] = 0
                    zeros -= 1
            idx -= 1
        return arr
