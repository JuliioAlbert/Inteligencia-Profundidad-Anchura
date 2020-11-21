print('#----- P R O F U N D I D A D-------#')

import json
with open('Conocimiento.json') as file:
	Conocimiento =json.load(file)
arr=[]

def profundidad(comienzo,busqueda):
	
	if comienzo == busqueda:
		return busqueda
	for j in Conocimiento:
		if j[0] == comienzo:
			arr.append(comienzo)
			print(j[0])
			resultado=profundidad(j[1],busqueda)
			if resultado:
				return resultado
	arr.pop()
	
resultado=profundidad("10","30")
if resultado:
	print ("Encontrado")
	print(arr)
else:
	print("No encontrado")


#JULIO ALBERTO GONZALEZ DE JESUS
