# Duplicando 0s

Dada una lista de enteros `arr`, duplica cada 0 que encuentres moviendo
todos los elementos a la derecha un lugar.

Observa que los elementos que terminen en una posición fuera del tamaño
original del arreglo no deben ser escritos.

Resuelve este reto *in-place*, es decir, sin utilizar memoria adicional
y modificando el arreglo recibido.

**Ejemplo 1**:
 * **Entrada**: `[1,0,2,3,0,4,5,0]`
 * **Salida**: `None`
 * **Why?**: Después de llamar tu función, el arreglo de entrada es modificado
   para formar `[1,0,0,2,3,0,0,4]`.

**Ejemplo 2**:
 * **Entrada**: `[1, 2, 3]`
 * **Salida**: `None`
 * **Why?**: Después de llamar tu función, el arreglo de entrada es modificado
   para formar `[1,2,3]`.

**Notas**: Existe una solución `O(n)` en tiempo.

## Como subir mi solución?

* Agrega un directorio con tu username de GitHub al directorio `solutions`, por ejemplo: `solutions/pablotrinidad`.
* El directorio que agregues debe contener dos archivos; `__init__.py` (vacío) y `solution.py`.
* El archivo `solution.py` debe contener lo siguiente:

```python
from typing import List


class Solution:

    def duplicate_zeros(self, arr: List[int]):
        # AQUÍ VA TU SOLUCIÓN
```

* Cuando tu solución esté lista, abre un PR en este repositorio.
* El repositorio correrá pruebas de legibilidad (*readability*).
* El repositorio probará que tu solución sea correcta.
* Cuando las dos pruebas (`grading` y `linting`) pasen, alguien del team revisará y hará merge de tu PR.
* Enjoy 💕.

### Debugging

* Puedes revisar que tu solución sea correcta en tu compu corriendo el comando `python3 grader/main.py`.
* Puedes verificar la legibilidad corriendo `pylint solutions/` (tal vez necesites
`pip install pylint` antes).
