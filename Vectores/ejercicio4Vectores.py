#4.  Almacenar en un vector (una lista) 5 números enteros leídos por teclado. Leer a continuación otro número
# y comprobar si está en el vector o no. En el caso de que esté visualizar qué posición ocupa. Sino indicarlo 
# mediante un mensaje. Visualizar también el elemento más pequeño, el más grande y la posición de ambos en el vector.

numeros = []
def introducirNumeros():
	for elemento in ['primer', 'segundo','tercer','cuarto','quinto']:
         texto = u'Introduce el %s número: ' % (elemento)
         numeros.append(int(input(texto)))
         
def comprobarNumero(numeros):
	numeroLider = int(input("Introduzca un número a comprobar entre los elegidos\n>"))
	
	if numeroLider in numeros:
		print("El número está dentro de la lista,en la posición ",numeros.index(numeroLider))
		
		
	else:
		print("El número no está en la lista")

def mostrarNumerosLista(numeros):
	numeroMaximo = max(numeros)
	numeroMinimo = min(numeros)
	print("El número más grande de la lista es el ", numeroMaximo, "y está en la posición ", numeros.index(numeroMaximo))
	print("El número más pequeño de la lista es el ", numeroMinimo, "y está en la posición ", numeros.index(numeroMinimo))




introducirNumeros()
comprobarNumero(numeros)
mostrarNumerosLista(numeros)
###CASOS TEST###
#4,5,6,7,8, elegido el 5 (Caso test OK)
#1,2,3,4,5 elegido el 4 (Caso test OK)
#25,45,68,84,74 elegido el 1 (Caso test OK)
#2,3,52,48,78 elegido el 78 (Caso test OK)
