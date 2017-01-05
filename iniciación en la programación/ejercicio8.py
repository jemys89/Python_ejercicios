#Escribe	un programa que pida por teclado dos números y que muestre en pantalla uno de los dos mensajes
# siguientes en función de los números leídos: a) el primer número (valor) es mayor que el segundo (valor)(introduciendo
# el valor de los números en el mensaje); b) el primer número (valor) es menor que el segundo (valor; c)
# los dos números son iguales (valor).

#Jamal



numero = float(input("teclee un número:" ))
numeroUno = float(input("teclee el siguiente número a valorar:"))
if numero == numeroUno:
    print(("sus números"),(numero),("y"),(numeroUno),("son iguales"))
elif numero > numeroUno:
    print(("su primer número"),(numero),("es mayor que"),(numeroUno))
else:
    print(("su primer número"),(numero),("es menor que"),(numeroUno))

