#programacion en parejas (revisar de clase de nuevo)
from stack import Stack  # suponiendo que tiene una clase Stack definida en un archivo separado

def match_tags(html):
    stack = Stack()
    i = 0
    while i < len(html):
        if html[i] == '<':  # se encontró una etiqueta de apertura
            j = html.find('>', i+1)  # encontrar el índice del cierre de etiqueta
            if j == -1:  # si no se encuentra la etiqueta de cierre correspondiente, no se puede hacer coincidir
                return False
            tag = html[i+1:j]  # extraer la etiqueta sin los signos < y >
            if tag.startswith('/'):  # se encontró una etiqueta de cierre
                if stack.is_empty() or stack.pop() != tag[1:]:  # no hay etiqueta abierta que coincida o no coincide con la etiqueta cerrada
                    return False
            else:  # se encontró una etiqueta de apertura
                stack.push(tag)
            i = j + 1  # saltar al siguiente carácter después de la etiqueta de cierre
        else:
            i += 1  # saltar al siguiente carácter si no es una etiqueta
    return stack.is_empty()  # todas las etiquetas se cerraron correctamente si la pila está vacía al final

# ejemplo de uso
html = '''
<html>
  <head>
    <title>Mi sitio web</title>
  </head>
  <body>
    <h1>Bienvenido a mi sitio</h1>
    <p>Este es un párrafo de ejemplo.</p>
    <img src="foto.jpg">
  </body>
</html>
'''

if match_tags(html):
    print('Todas las etiquetas coinciden')
else:
    print('Las etiquetas no coinciden')
