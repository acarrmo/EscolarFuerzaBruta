# EscolarFuerzaBruta
Práctica fuerza bruta en inicio de sesión Wordpress

# Comenzando 
Estas instrucciones te permitirán obtener una copia de la práctica en tu máquina local para propósitos de desarrollo y pruebas.

# Pre-requisitos 
Python
Editor de código
PIP
Importar xmlrpc.client
Verificar más detalles en https://www.youtube.com/watch?v=5lFmjjf9Z0o&list=LLykeHMrEd0vl4aZUT9AeJBQ&index=2&t=0s

# Ejecutando las pruebas
Se utiliza una librería de Python llamada xmlrpc para poder encontrar la contraseña de un login en Wordpress, mediante fuerza bruta.
Antes que todo, se verifica que el sitio en Wordpress soporte esta librería, por lo que al finalizer la url del sitio, se agrega /xmlrpc.php
Si la respuesta es que acepta POST, es suficiente para poder utilizar este código. 
Para versiones 2 de Python, la librería simplemente es xmlrpclib. Sin embargo, para versiones 3 es necesario utilizar en su lugar xmlrpc.client tanto al inicio del código
como al utilizar la variable blog, donde se especifica la url a atacar. La variable password especifica el diccionario de contraseñas a probar, para efectos
de la práctica solo se escriben 8. En la variable resultado se irán obteniendo los posts en el sitio especificado, con un usuario (se prueba con usuarios específicos)
Se entiende que si la longitud del resultado es mayor a 0, ya se podrá tomar en cuenta como que existe una contraseña por probar.
Al correr el ataque, va probando cada palabra del diccionario. Y al ingresar la correcta, aparecerá Login, indicando que esa es la correcta.

# Construido con Python

# Autora
Angélica CarrMo 
