print('#----- A N C H U R A -------#')

import json
with open('Conocimiento.json') as file:
	Conocimiento =json.load(file)

con =[]
g=[]
segundo = []
siguiente=[]

def priAnchura(Rama,Hoja):
	if Rama == Hoja:
		return Hoja
	if siguiente:
		contador = 0
		for X in siguiente:
			 contador += 1
		if contador > 1:
			print("Nodo")
			print("")
			print(siguiente[0])
			siguiente.pop(0)
	if segundo:
		del segundo[:]
	for i in Conocimiento:
		if i[0] == Rama:
			siguiente.append(i[1])
			segundo.append(i[0])
			if i[1] == Hoja:
				nodo = priAnchura(i[1],Hoja)
				return nodo
	con.append(list(set(segundo)))
	if con:
		print("Nodo Recorrido")
		print("")
		print(str(con))
		print(siguiente[0])
		g.append(siguiente[0])
		return priAnchura(siguiente[0],Hoja)

nodo = priAnchura("10","30")
print("Encontrado - Nodo principal: ")
print("")
print(nodo)
cam = []
if nodo:
	for c in g:
		if c not in cam:
			cam.append(c)
	print("Nodos Revi")
	print(cam)
else:
	print("No se encontro")
