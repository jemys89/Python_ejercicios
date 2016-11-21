#Escribe	un programa que pida por teclado dos números y que calcule y muestre su suma solamente si:
#a. los dos son pares 
#b. el primero es menor que cincuenta 
#c. y el segundo está dentro del intervalo cerrado 100-500. 
#En el caso de que no se cumplan las condiciones, en vez de la suma ha de visualizarse un mensaje de error.

#Jamal

print("Programa que calcula la suma únicamente si los dos números introducidos son:\n los dos son pares\n el primero es menor que cincuenta\n y el segundo está dentro del intervalo cerrado 100-500")
numeroUno = int(input("teclee un número:"))
numeroDos = int(input("teclee otro número:"))
if numeroUno %2 == 0 and numeroDos %2 == 0:
    print (numeroUno + numeroDos)
elif numeroUno < 50:
	print (numeroUno + numeroDos)
elif numeroDos >100 and numeroDos <500:
	print(numeroUno + numeroDos)
else:
    print("Alguno de los 2 valores no cumplen las condiciones")
    

