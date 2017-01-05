#Repite el programa anterior, pero en vez de leer 5 números, el usuario ha de indicar antes
# cuántos números van a ser leídos, indicándolo mediante el mensaje: Introduzca cuántos números
# tienen que leerse por teclado: _

numeros = []
rango = int(input("Introduce la cantidad de números que quieras introducir:"))
for i in range(rango):
    numero = int(input("Introduce un número: "))
    assert  numero > 0, "Introduce un número positivo"
    numeros.append(numero)

numeros.sort()

minimo = numeros[0]
maximo = numeros[-1]
print("El mayor de los números es:",maximo)
print("El número mínimo es:",minimo)

###CASOS TEST###
#5,9,8,8,10 (caso test OK)
#-1(Caso test OK, salta el assert)
#22,65,65,8,-65(Caso test OK, salta el assert)
