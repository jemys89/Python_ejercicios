#27.Escribe 	un programa que calcule la nota media de un alumno. El programa pregunta en primer lugar 
#cuántas calificaciones tiene del alumno, solicitando a continuación las notas, y  calculando y mostrando
# en consola la nota media.

notas = []
def solicitarNotas():
	rango = int(input("¿Cuántas notas vas a introducir?\n>"))
	for i in range(rango):
		notasIntroducidas = float(input("Introduce aquí las notas\n>"))
		#assert notasIntroducidas == "", "ERROR, lo introducido no es un número"
		notas.append(notasIntroducidas)
	print("La nota media de sus notas és ", sum(notas)/rango)



	




###CASOS TEST###
solicitarNotas()
#5 notas, 3,4,7,8,9 nota media 6.2 (CASO TEST OK)
#3 notas, 4,5,7 nota media 5.33 (CASO TEST OK)