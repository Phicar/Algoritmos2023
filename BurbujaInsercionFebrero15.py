#Input: x lista de numeros enteros
# retornar la lista x ordenada
def insercion(x):
	print(x)
	phi = [0 for i in range(len(x))]
	for p in range(1,len(x)): #seleccionar el pivot
		piv = x[p] #pivot
		j = p-1 #el indice para moverme antes del pivot
		cont = 0
		while j>=0 and x[j]<piv: #mientras el pivot sea menor a x[j], echo para atras
			x[j+1]=x[j] #corriendo a la derecha los mayores
			cont+=1
			j-=1
		phi[piv-1] = cont #los mas grandes a la izquierda de piv
		#print(piv,x)
		x[j+1]=piv
		#print(piv,x,phi[piv-1])
	print("phi-->",phi)
	return x
#Input: X lista de numeros enteros.
#retornar la lista X ordenada.
def burbuja(x):
	print("OR: ",x)
	#Como entra n veces y n-1 cada i veces, entonces entra basicamente n^2 veces
	for i in range(len(x)): #voy a burbujear n veces
		for j in range(len(x)-1): #burbujear
			if x[j]>x[j+1]: #pregunto para intercambiar
				x[j],x[j+1]=x[j+1],x[j] #intercambia
		#print(x)
	return x
#para generar numeros enteros en un rango digamos [n].
A = [random.randint(1,100) for i in range(15)]
print(insercion([3,1,5,4,2]))
