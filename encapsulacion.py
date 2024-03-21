#!/usr/bin/env python3
# Ejemplo de encapsulamiento. Ejercicios de entrenamiento en el curso de Python Ofensivo https://hack4u.io
# # 21-03-2024 / rnek0

class MaquinaDeCafe:
    """La maquina de café del pasillo de la gasolinera"""
    _ganancia = 0
    _cafe = "tostado"
    __temperatura_agua = "0"

    def hacer_el_cafe(self, _cafe):
        """Hace el café, pero no sabemos de donde viene, ni como se hace."""

        __temperatura_agua = "60°"
        print(f" [+] Sirviendo el {self._cafe}")

    def caja_fuerte(self, dinero_pagado, cafe):
        """Cobra el monto pagado por el café y manda hacer el café"""
        self._ganancia = self._ganancia + dinero_pagado
        self.hacer_el_cafe(cafe)

    def __init__(self, pasta, tipo_cafe):
        # Atributo protegido.
        print(f" [+] Pediste un {tipo_cafe}\n\tEn preparación...")
        self._monto = pasta
        self._cafe = tipo_cafe
        self.caja_fuerte(pasta, self._cafe)
        print(f"\tGracias por tomar el café con nosotros !\n")

class Banner:
    """Display banner app"""
    title = """\t  __   ____       __       __  
\t / /  / ___|__ _ / _| ___  \ \ 
\t/ /  | |   / _` | |_ / _ \  \ \\
\t\ \  | |__| (_| |  _|  __/  / /
\t \_\  \____\__,_|_|  \___| /_/ 
                               
\t     La maquina del café                           """
    
    @classmethod
    def display_banner(cls):
        return f"\n{cls.title}\n"


print(Banner.display_banner())

mi_cafe = MaquinaDeCafe(1.5, "descafeinado")
try:
    # ATRIBUTO PROTEGIDO se podría acceder pero Python te lo pone difícil (name mangling > mi_cafe._MaquinaDeCafe__temperatura_agua)
    print(f"Pero quiero el agua a 10000° : {mi_cafe.__temperatura_agua}") 
except:
    print("   Stop ! , ESTO NO SE HACE: CODER LAMER !")
finally:
    print("   [!] Guardo el dinero y el café. Llamando al encargado. Sal por patas...")

print(f"\n [!] Hay {mi_cafe._ganancia} € de ganancia dentro de la maquina.")  # ESTO NO SE HACE AUNQUE TECNICAMENTE SE PUEDE HACER (pero rompe la encapsulacion)
print(" [!] Si pides un café, 'solo' debes tener que meter tu moneda y escoger el producto.")
print(" [!] Dando acceso a todo el funcionamiento interno... ")
print(" [!] el cliente te meterá la maquina patas abajo. !!!\n")
print(" [!] Y encima se llevara el dinero !!!\n")
