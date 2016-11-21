#Escribe un programa que escriba en pantalla los 30 primeros números naturales (del 1 al 30), así como su media aritmética.

suma = 0
for numero in range(31):
	print (numero)
	suma = suma + numero

print ("La media aritmética del 1 al 30 es:",suma/30)