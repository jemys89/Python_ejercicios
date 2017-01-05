#Escribe un programa que visualice los n-primeros múltiplos de 2, siendo n un valor leído por teclado.

numero = int(input("Introduce un valor: "))

print ("Los ", numero, " primeros múltiplos de 2 son:")

for elemento in range(numero*2+1):
	if elemento == 0:
	  continue
	elif elemento %2 == 0:
		print (elemento)