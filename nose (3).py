# A: lista
# n: n>=1 entero
def potencia(A,n):
	#caso base
	if n==1:
		AL = []
		for x in A:
			AL.append([x])
		return AL
	C =[]
	B = potencia(A,n-1)
	for x in A:
		for y in B:
			C.append([x]+y)
	return C

#x: lista
#y: permutacion (lista)
def primerPunto(x,y):
	z = [0 for i in range(len(x))]
	for i in range(len(x)):
		z[i]=x[y[i]-1]
	return z
def miguel(x,y):
	z =[]
	for i in range(len(x)):
		z.append(x[y[i]-1])
	return z
def a(x,y):
	return [x[y[i]-1] for i in range(len(y))]

print(primerPunto(["c","0","s","a"],[3,4,1,2]))
print(potencia([1,2,3],1))
