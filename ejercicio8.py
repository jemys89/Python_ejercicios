#Ejercicio8 de programación
#Jamal
#Ejercicio que se basa en la valoración de 2 números


numero=float(input("teclee un número:" ))
numero1=float(input("teclee el siguiente número a valorar:"))
if(numero == numero1):
    print(("sus números"),(numero),("y"),(numero1),("son iguales"))
elif(numero > numero1):
    print(("su primer número"),(numero),("es mayor que"),(numero1))
elif(numero < numero1):
    print(("su primer número"),(numero),("es menor que"),(numero1))

