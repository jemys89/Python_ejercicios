#Lee por teclado 5 números enteros positivos, y escribe cuál es el mayor de los números introducidos.  	
#Repite el programa anterior, pero chequeando que el usuario no introduzca números negativos.
#Si se da esta circunstancia hay que visualizar un mensaje de error, forzando al usuario a que introduzca números positivos.

numeroMayor = 0
rango = 5
for i in range(rango):
    numero = int(input("Introduce un numero: "))
    assert  numero > 0, "Introduce un número positivo"
    if numero > numeroMayor:
        numeroMayor = numero
        
print ("el numero mas alto es " + str(numeroMayor))




#######CASOS TEST########
#5,9,8,8,10 (caso test OK)
#-1(Caso test OK, salta el assert)
#22,65,65,8,-65(Caso test OK, salta el assert)
