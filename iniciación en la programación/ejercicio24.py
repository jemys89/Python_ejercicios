#Repite el programa anterior, pero obligando al usuario a que los dos números introducidos sean positivos,
# es decir, si el usuario introduce algún valor negativo, se visualiza un mensaje de aviso y se vuelve a pedir otro número.
sumaPares = []
sumaImpares = []
def introduceDosNumeros():
	primerNumero = int(input("Introduce el primer número positivo"))
	while primerNumero < 0:
        	 print ('ERROR, Introduce un número positivo')
        	 primerNumero=(int(input("Introduce el número positivo: ")))	
	segundoNumero = int(input("Introduce el segundo número positivo"))
	while segundoNumero < 0:
             print ('ERROR, Introduce un número positivo')
             segundoNumero=(int(input("Introduce un número positivo: ")))
	
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
#-4 caso test ok salta el mensaje de error y vuelve ha pedir que introduzca el primer número positivo
#5,-8 caso test ok salta el mensaje de error y vuelva a pedir que introduza el segundo número 
	
	