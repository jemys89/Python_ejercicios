#Lee por teclado 5 números enteros positivos, y escribe cuál es el mayor de los números introducidos.  	
numeros = []
for elemento in ['primer', 'segundo','tercer','cuarto','quinto']:
    texto = u'Introduce el %s número: ' % (elemento)
    numeros.append(int(input(texto)))

# Ordenamos.
numeros.sort()

# Obtenemos máximo y mínimo.
minimo = numeros[0]
maximo = numeros[4]
print("El mayor de los números es:",maximo)