"""Script que duplica los 0 de una lista sin modificar la longitud de la misma"""
from typing import List

class Solution:
    """Objeto del ejercicio"""
    def duplicate_zeros(self, arr: List[int]):
        """Funcion que duplica los 0s"""
        zeros = 0
        for idx, val in enumerate(arr):
            if val == 0 and idx + zeros < len(arr) - 1:
                zeros += 1
                last_zero = idx

        j = len(arr) - 1
        for _ in arr:
            if j == 0:
                break
            arr[j] = arr[j - zeros]
            if arr[j] == 0 and zeros > 0 and j - zeros <= last_zero:
                arr[j-1] = 0
                zeros -= 1
                j -= 1

            j -= 1
