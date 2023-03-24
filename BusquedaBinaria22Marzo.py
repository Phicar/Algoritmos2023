import random
#retornar solo un indice
def Busqueda(A,x):
	mini = 0 #posicion a izq.
	maxi = len(A)-1 #posicion a der.
	ult = -1
	while mini<=maxi:
		#print(x,A,mini,maxi)
		med = (mini+maxi)//2
		if x<A[med]:
			maxi = med-1
		else:
			mini = med+1
			if x==A[med]:
				ult = med

	return ult
A = [2,2,2,2,2,2,2,2,2]#[random.randint(1,100) for i in range(100)]
A.sort()
print(Busqueda(A,2))
