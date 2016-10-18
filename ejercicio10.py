#ejercicio10 de programación
#Jamal
#Ejercicio que suma dos números positivos

numero=float(input("teclee un número:" ))
numero1=float(input("teclee el siguiente número:"))
if(numero>=0 and numero1 >=0):
    print(("La suma de los dos números es:"),(numero + numero1))
elif(numero <=0 and numero1 <=0):
    print("No se calcula la suma porque los dos números son negativos.")
elif(numero <0 and numero1 >0):
    print("No se calcula la suma porque el primer número es negativo.")
elif(numero >0 and numero1 <0):
    print("No se calcula la suma porque el segundo número es negativo.")
