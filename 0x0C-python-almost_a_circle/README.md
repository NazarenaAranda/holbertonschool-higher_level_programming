Qué significan *args y **kwargs como parámetros:
- - - - - - - - - - -  - - -  - - - - - - - - - - 
*ARGS:
------
En Python, el parámetro especial *args en una función se usa para pasar (de forma opcional) un número variable de argumentos posicionales.
Más detalladamente sería:
-------------------------
- Lo que realmente indica que el parámetro es de este tipo es el símbolo ‘*’, el nombre args se usa por convención.
- El parámetro recibe los argumentos como una tupla.
- Es un parámetro opcional. Se puede invocar a la función haciendo uso del mismo, o no.
- El número de argumentos al invocar a la función es variable.
- Son parámetros posicionales, por lo que, a diferencia de los parámetros con nombre, su valor depende de la posición en la que se pasen a la función.

Se usaría el parámetra *args en el caso de que no quieras limitar a tu funcion, es decir, en vez de darle determinado valor, al usar *args podemos pasar tantos argumentos 
como queramos.
- - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - -

**KWARGS:
---------
En Python, el parámetro especial **kwargs en una función se usa para pasar (de forma opcional) un número variable de argumentos con nombre.
Diferencias con *ARGS:
-----------------------
- Lo que realmente indica que el parámetro es de este tipo es el símbolo ‘**’, el nombre kwargs se usa por convención.
- El parámetro recibe los argumentos como un diccionario.
- Al tratarse de un diccionario, el orden de los parámetros no importa. Los parámetros se asocian en función de las claves del diccionario.

Se usaría cuando no se sabe cuantos argumentos se le va a dar al diccionarío.
- -  - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - 

