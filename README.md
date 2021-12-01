# Detalles
La solución presentada, requiere un archivo de texto como I/O que se encuentra en:

**# Input**

Ruta > "BackChallenge\data\input"

**# Output**

Ruta > "BackChallenge\data\output"


# Testing

Para ejecutar el caso de prueba que esta localizado en _"reto_test.py"_

**Ruta >** "BackChallenge\tests\reto_test.py"

**# Modificar nombres de los archivos I/O**

**input** = 'TestCase.txt'

**output** = 'TestCase.txt'

Para ello se importó la librería unittest, en el que se compara el output esperado al input mencionado en el problema.

# Solución

En primera instancia se hace una diferencia del promedio total gastado con respecto al gasto individual. Con este diferencia obtenemos valores positivos y negativos.

Se requiere la cantidad total que tiene que ser intercambiada, para ello se realiza una sumatoria de los valores positivos y finalmente obtenemos el resultado que se almacena en un buffer para retornarlo y ser comparado con un TDD.
