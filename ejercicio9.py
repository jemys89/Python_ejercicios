#Escribe un programa que nos pida por teclado dos números enteros y que a continuación
# muestre en pantalla la suma de los dos números solamente si son los dos positivos.
# Si no se cumple que los dos números sean positivos se visualizará un mensaje indicándolo.
# La salida ha de tener el siguiente formato: “La suma de los dos números es: XXX” o “No se 
#calcula la suma porque alguno de los números o los dos no son positivos”.
#Jamal


numeroUno = float(input("teclee un número:" ))
numeroDos = float(input("teclee el siguiente número:"))
if numeroUno >=0 and numeroDos >=0:
    print("La suma de los dos números es:",numeroUno + numeroDos)
else:
    print("No se calcula la suma porque alguno de los números o los dos no son positivos")

