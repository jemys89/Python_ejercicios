#Escribe un programa que pida por teclado el radio de una circunferencia, 
#y que a continuación calcule y escriba en pantalla la longitud de la circunferencia y del área del círculo.
#Ejercicios propuestos de programación
#Jamal El Boutaibi


from math import pi
radio = float(input ("Introduce el radio de una circunferencia: "))
print ("Su longitud es",(2 * pi * radio))
print ("Su área es",(pi * (radio**2)))
