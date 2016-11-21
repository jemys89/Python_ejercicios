#Escribe un programa que pida por teclado tres valores de tipo entero, y que calcule si se cumple
# que la suma de dos de ellos es igual al tercero. La salida del programa tiene que tener el formato:
#		Números introducidos: N1	N2 N3 (tabulador)
#Y una de las cuatro líneas de salida siguientes:
#Se cumple que N1 = N2 + N3
#Se cumple que N2 = N1 + N3
#Se cumple que N3 = N1 + N2
#Los números no cumplen la condición

#Jamal

print ("Teclee tres números enteros:")
n1= int(input("teclee el primer número entero:"))
n2= int(input("teclee el siguiente número:"))
n3= int(input("teclee el último número:"))
if n1 + n2 == n3:
        print ("Se cumple que",n1,"+",n2,"=",n3)
elif n1 + n3 == n2:
         print ("Se cumple que",n1,"+",n3,"=",n2)
elif n2 + n3 == n1:
         print ("Se cumple que",n2,"+",n3,"=",n1)
else:
             print ("Los números no cumplen la condición")
