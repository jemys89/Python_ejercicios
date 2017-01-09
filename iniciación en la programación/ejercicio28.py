#-Modifica el programa anterior para que no permita al usuario introducir notas mayores que 10. 
#-El proceso de lectura finaliza cuando se introduzca una nota negativa. 
#-El programa puede ser ejecutado varias veces, para ello después de realizar el proceso para un alumno
#se visualiza el mensaje: ¿Desea calcular la media de otro alumno? Teclee S/N. 
#-Si el usuario teclea S el programa vuelve a ejecutarse. Si teclea N finaliza su ejecución.
notas = []
def solicitarNotas():
	rango = int(input("¿Cuántas notas vas a introducir?\n>"))
	for i in range(rango):
		notasIntroducidas = float(input("Introduce aquí las notas\n>"))
		while notasIntroducidas > 10:
				notasIntroducidas = float(input("Introduce una nota inferior o igual a 10\n>"))


		notas.append(notasIntroducidas)
	print("La nota media de sus notas és ", sum(notas)/rango)

def menu():
	print("¿Desea calcular la media de otro alumno?\nTeclee 1 para reiniciar el programa\n Teclee 2 para salir")
	opciones = input("Introduce una opción\n>")
	if opciones == "1":
		return solicitarNotas()
	elif opciones == "2":
		pass
	else:
		print("No corresponde a ninguna opción")


	
	




	




###CASOS TEST###
solicitarNotas()
menu()
#5 notas, 3,4,7,8,9 nota media 6.2 (CASO TEST OK)
#3 notas, 4,5,7 nota media 5.33 (CASO TEST OK)
