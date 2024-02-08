def es_palindromo(palabra:str):
	invertido = palabra[::-1]

	if invertido == palabra:
		return True
	else:
		return False

jujuy = 'jujuy'
nadan = 'nadan'

print(es_palindromo(nadan))
print(es_palindromo(jujuy))
