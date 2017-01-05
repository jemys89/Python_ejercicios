#Lee por teclado dos números enteros positivos y calcula la suma de los números pares e impares comprendidos
# entre los dos números leídos, ambos incluidos. El programa tiene que funcionar independientemente de que el 
#primero de los números tecleados sea mayor o menor que el segundo.
sumaPares = []
sumaImpares = []
def introduceDosNumeros():
	
	primerNumero = int(input("Introduce el primer número positivo"))
	assert primerNumero > 0, "Lo que has introducido es un número negativo... ha de ser un número positivo"
	segundoNumero = int(input("Introduce el segundo número positivo"))
	assert segundoNumero > 0, "Lo que has introducido es un número negativo... ha de ser un número positivo"
	if primerNumero < segundoNumero:
		for numero in range(primerNumero,segundoNumero + 1):
			if numero %2 == 0:
				sumaPares.append(numero)
		
			else:
				sumaImpares.append(numero)
	else:
		for numero in range(segundoNumero,primerNumero + 1):
			if numero %2 == 0:
				sumaPares.append(numero)
		
			else:
				sumaImpares.append(numero)

def mostrarSuma(sumaPares,sumaImpares):
	print ("La suma de sus números pares es:",sum(sumaPares))
	print("La suma de sus números impares es:",sum(sumaImpares))


introduceDosNumeros()
mostrarSuma(sumaPares,sumaImpares)

###Casos Test###
#10,20 caso test ok
#20,10 caso test ok
#-4 caso test ok salta el assert
#5,-8 caso test ok salta el assert