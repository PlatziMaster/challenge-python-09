"""Modulo para duplicar los 0 en una lista y mover los demás elementos a la derecha."""
from typing import List


class Solution:
    """Clase de la Solución al reto"""

    def duplicate_zeros(self, arr: List[int]):
        """ Función que modífica la lista """
        zero_acum = 0
        last = 0
        array_len = len(arr) - 1

        for idx, value in enumerate(arr):
            if value == 0 and idx + zero_acum < array_len:
                zero_acum += 1
                last = idx

        for _ in arr:
            if array_len != 0:
                arr[array_len] = arr[array_len - zero_acum]
                if arr[array_len] == 0 and zero_acum > 0 and array_len - zero_acum <= last:
                    arr[array_len - 1] = 0
                    zero_acum -= 1
                    array_len -= 1
                array_len -= 1
