#Escribe un programa que pida por teclado dos valores de tipo numérico que se han de guardar
#en sendas variables. ¿Qué instrucciones habría que utilizar para intercambiar su contenido? 
#(es necesario utilizar una variable auxiliar). Para comprobar que el algoritmo ideado es correcto, 
#muestra en pantalla el contenido de las variables una vez leídas, y vuelve a mostrar su contenido una
# vez hayas intercambiado sus valores.

#Jamal

numeroUno=float(input("teclee cualquier número: " ))
numeroDos=float(input("Teclee un número diferente al anterior: "))
print ("Sus números elegidos son:",numeroUno, numeroDos)
numeroAuxiliar= numeroDos
print("Sus números han sido cambiados de preferencia ",numeroAuxiliar,numeroUno)

