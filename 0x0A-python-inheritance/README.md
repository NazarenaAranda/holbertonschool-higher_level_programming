Inheritance en python
---------------------------
Inheritance = Herencia

La herencia es utilizada para heredar: campos de datos, métodos de acceso de otra clase, y ademas puede añadir nuestros propios métodos y campos. Por lo 
tanto la herencia nos proporciona una manera de organizar el código para no tener que volver a repetir código

dir ()
------------
dir () es una funcion que devuelve una lista de los atributos y métodos de cualquier objeto (por ejemplo, funciones, módulos, cadenas, listas, diccionarios, etc.) dir () intenta devolver una lista válida de atributos del objeto al que se llamaI.

----------------------------------------------------------------------------------

## Las funciones de comparación de objetos son útiles para todos los objetos, y llevan el nombre de los operadores de comparación enriquecida que soportan:

operator.lt(a, b)
operator.le(a, b)
operator.eq(a, b)
operator.ne(a, b)
operator.ge(a, b)
operator.gt(a, b)
operator.__lt__(a, b)
operator.__le__(a, b)
operator.__eq__(a, b)
operator.__ne__(a, b)
operator.__ge__(a, b)
operator.__gt__(a, b)
Realiza «comparaciones enriquecidas» entre a y b. Específicamente, lt(a, b) es equivalente a a < b, le(a, b) es equivalente a a <= b, eq(a, b) es equivalente a a == b, ne(a, b) es equivalente a a != b, gt(a, b) es equivalente a a > b y ge(a, b) es equivalente a a >= b. Tenga en cuenta que estas funciones pueden retornar cualquier valor, que puede o no ser interpretable como un valor booleano

---------------------------------------------------------------------------

## La función incorporada hasattr() toma como argumentos un objeto y el nombre de un atributo y retorna True si el objeto contiene dicho atributo.


``` class Rectangulo:
    def __init__(self, b, h):
        self.b = b
        self.h = h

rect = Rectangulo(10, 5)
print(hasattr(rect, "b"))     # True
print(hasattr(rect, "area"))  # False
```

### La función opera haciendo uso de getattr() y caputurando AttributeError, de modo que es similar a:

``` def hasattr(obj, attr):
    try:
        getattr(obj, attr)
    except AttributeError:
        return False
    return True ```
    
-------------------------------------------------------------------------

## Función super

### Esta función nos permite invocar y conservar un método o atributo de una clase padre (primaria) desde una clase hija (secundaria) sin tener que nombrarla explícitamente. Esto nos brinda la ventaja de poder cambiar el nombre de la clase padre (base) o hija (secundaria) cuando queramos y aún así mantener un código funcional, sencillo  y mantenible. no necesitamos especificar la clase padre, por lo que podremos cambiarle el nombre en cualquier momento y nuestro código seguirá funcional.

``` class Padre(object): #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas
        
class Hijo(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        super().__init__(ojos, cejas)#Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara #Especificamos el nuevo atributo para Hijo
        
Tomas = Hijo('Marrones', 'Negras', 'Larga')
print (Tomas.ojos, Tomas.cejas, Tomas.cara)
```
