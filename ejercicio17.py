#Escribe un programa que calcule y escriba la suma de los números pares por un lado, 
#y de los impares por otro, de los números comprendidos entre dos número introducidos por teclado.
primerNumero = int(input("Introduce un número :"))
segundoNumero = int(input("Introduce un segundo número"))

sumaImpares = []
sumaPares = []
for numero in range(primerNumero,segundoNumero + 1):
	if numero %2 == 0:
		sumaPares.append(numero)
		
	else:
		sumaImpares.append(numero)
		
	

print ("La suma de sus números pares es:",sum(sumaPares))
print("La suma de sus números impares es:",sum(sumaImpares))