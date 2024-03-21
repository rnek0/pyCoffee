# Revisiones y ejercicios del curso de Python Ofensivo

- <https://hack4u.io>

## Encapsulamiento

Capacidad de un objeto de no mostrar ni dar acceso a su funcionamiento interno, exponiendo al consumidor solamente lo necesario para el buen funcionamiento de la instancia del objeto.

Se hace referencia a las variables privadas y protegidas del objeto que no deben ser accedidas directamente.

- Variable **privada**   : self.__color  (con 2 barras bajas)
- Variable **protegida** : self._saldo   (con 1 barra baja)

No se debería nunca referenciar a estas variables internas (en Python es un convenio) aunque eso sea posible en Python. No es el caso de otros lenguajes.
Acceder a esos atributos es una violación del encapsulamiento que es castigada por tortura y abducción de aliens (de mala manera)...


