#Parametros: x: lista enteros positivos
#Idea: Voy a iterar sobre la lista y verificar la
#negacion de la proposicion.
def isSorted(x):
	for i in range(len(x)-1):
		if x[i]>x[i+1]:
			return False
	return True
#Parametros: x: lista de enteros positivos, n tamano de la permutacion.
#Idea: Verificar si los elementos estan en [n] y ver duplicados.
def isPermutation(x,n):
	if len(x)!= n:
		return False
	for i in range(len(x)):
		if x[i]>n or x[i]<1:
			return False
		for j in range(i+1,len(x)):
			if x[i]==x[j]:
				return False
	return True
#Misma idea que arriba pero usando un arreglo de booleanos como centinelas
#que me dicen cuando lo he visto
def isPermutation2(x,n):
	if len(x)!=n:
		return False
	visto = [False for i in range(n+1)]
	for i in range(len(x)):
		if (x[i]>n or x[i]<1) or visto[x[i]]:
			return False
		visto[x[i]]= True
	return True
print(isSorted([2,4,1,5,3]))
print(isSorted([1,3534,23534634,3463636346346]))
print(isPermutation([4,3,1,2],4),isPermutation2([4,3,1,2],4))
print(isPermutation([4,3,1,2],5),isPermutation2([4,3,1,2],5))
print(isPermutation([4,3,1,3],4),isPermutation2([4,3,1,3],4))
print(isPermutation([5,3,1,2],4),isPermutation2([5,3,1,2],4))
	
