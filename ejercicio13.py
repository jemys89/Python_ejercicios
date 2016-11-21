#Diseña	un programa que calcule el importe final de una venta considerando que sobre el valor bruto se hace un descuento según la siguiente tabla:
#Valores <=20 implican un descuento del 0%
#Valores >20 y <=100 implican un descuento descuento del 5%
#Valores >100 implican un descuento 10%


valor=float(input("Introduce un valor:"))
if valor >= 20 and valor <= 100 :
    print(valor * 0.95)
elif valor >= 100:
    print(valor * 0.90)
else:
     print("Su valor no tiene ningún descuento")
            
