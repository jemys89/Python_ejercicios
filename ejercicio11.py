#Ejercicio11 de programación
#Jamal
#Progrma que informa si los 2 primeros números sumados, son del mismo valor que el tercer número.


print ("Teclee tres números enteros:")
n1= int(input("teclee un número entero:"))
n2= int(input("teclee el siguiente número:"))
n3= int(input("teclee el último número:"))
if (n1 + n2 == n3):
        print ((("Se cumple que"),(n1),("+"),(n2),("="),(n3)))
elif (n1 + n3 == n2):
         print ((("Se cumple que"),(n1),("+"),(n3),("="),(n2)))
elif (n2 + n3 == n1):
         print ((("Se cumple que"),(n2),("+"),(n3),("="),(n1)))
else:
             print ("No hay 2 números que sumen lo mismo que 1")
             
