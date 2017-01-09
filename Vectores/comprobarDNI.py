#Verificar si una cadena de texto leída por teclado es un  DNI correcto o no.
# Suponer que los DNI tienen 8 dígitos y a continuación una letra mayúscula.


	
dni = input("Introduce tú DNI\n > ")
assert len(dni) == 9, "El DNI debe tener 9 caracteres"
	

def comprobarNumerosDni(dni):
	letrasValidas = "TRWAGMYFPDXBNJZSQVHLCKE"
	numeros = "0123456789"
	letraMayuscula = dni[8].upper()
	
	for n in dni[:8]:
		

		if n in numeros:
			pass
		else:
			print("Los 8 primeros caracteres  de '{}' no son números".format(dni))

	if letraMayuscula in letrasValidas:
		pass
	else:
		print("La letra no coincide con las validadas para el DNI")

	return print("DNI OK")




	
	
comprobarNumerosDni(dni)
		

#CASOS TESTS
#43125269Q Ok
#q25413417 Peta
# 234  ERR7 Peta
# 11111111A Ok
# []  Peta
# 22222222Q Ok