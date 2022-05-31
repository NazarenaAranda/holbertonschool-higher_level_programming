WITH ANTES DE OPEN: Es una buena práctica usar la palabra clave with cuando se trata de objetos de archivo. La ventaja es que el archivo se cierra correctamente después de que finaliza su suite, incluso si se genera una excepción en algún momento.

open() devuelve un objeto de archivo y se usa más comúnmente con dos argumentos posicionales y un argumento de palabra clave: open(filename, mode, encoding=None), "mode" 
es opcional.
