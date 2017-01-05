#Escribe 	un programa que solicite por teclado 5 números positivos, forzando al usuario a que únicamente
# introduzca valores positivos. A continuación el programa tiene que escribe cuál es el valor más pequeño 
#y cuál es el mayor valor de los introducidos por el usuario.
print("Introduce 5 números positivos")
numeros = []
rango = 5
for i in range(rango):
    numero = int(input("Introduce un número: "))
    assert  numero > 0, "Introduce un número positivo"
    numeros.append(numero)

numeros.sort()

minimo = numeros[0]
maximo = numeros[4]
print("El mayor de los números es:",maximo)
print("El número mínimo es:",minimo)

###CASOS TEST###
#5,9,8,8,10 (caso test OK)
#-1(Caso test OK, salta el assert)
#22,65,65,8,-65(Caso test OK, salta el assert)