# Revisiones y ejercicios del curso de Python Ofensivo

- <https://hack4u.io>

## Encapsulamiento

Capacidad de un objeto de no mostrar ni dar acceso a su funcionamiento interno, exponiendo al consumidor solamente lo necesario para el buen funcionamiento de la instancia del objeto.

Se trata de los atributos privados y protegidos del objeto que no deben ser accedidos directamente.

- Atributo **privado**   : self.__color  (con 2 barras bajas)
- Atributo **protegido** : self._saldo   (con 1 barra baja)

No se debería nunca referenciar a estas variables internas (en Python es un convenio [PEP8](https://peps.python.org/pep-0008/#method-names-and-instance-variables)) aunque eso sea posible en Python. No es el caso en otros lenguajes que pueden dar error en tiempo de compilación.
Acceder a esos atributos es una violación del encapsulamiento que es castigada por tortura y abducción de aliens (de mala manera)...

---
