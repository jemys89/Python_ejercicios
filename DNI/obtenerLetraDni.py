#Hacer un programa que dado un número de DNI obtenga la letra del NIF. La letra correspondiente a un número de DNI se calcula mediante el siguiente algoritmo: 
#Se obtiene el resto de dividir el número de DNI entre 23. 
#El número resultante nos indica la posición de la letra correspondiente a ese DNI, en la siguiente cadena:

dni = input("Introduce los números de tu dni para saber que letra le corresponde\n>")
assert len(dni) == 8, "El DNI debe tener 8 números"

def comprobarNumerosDni(dni):
	numeros = "0123456789"
	
	for n in dni:
		

		if n in numeros:
			pass
		else:
			print("Los 8 primeros caracteres  de '{}' no son números".format(dni))

	return dni





def obternerLetraDni(dni):
	tablaAsignacion = {
        0:"t",1:"r", 2:"w", 3:"a", 4:"g", 5:"m", 
        6:"y", 7:"f", 8:"p", 9:"d", 10:"x", 11:"b", 
        12:"n", 13:"j", 14:"z", 15:"s", 16:"q", 17:"v",
        18:"h", 19:"l", 20:"c", 21:"k", 22:"e"}
	numeroEnteroDni = int (dni)
	restoDni = numeroEnteroDni % 23
	dni = str(numeroEnteroDni) + tablaAsignacion[restoDni]
	return  print("Su DNI con la letra correspondiente añadida \n==>'{}' ".format(dni))




comprobarNumerosDni(dni)
obternerLetraDni(dni)













