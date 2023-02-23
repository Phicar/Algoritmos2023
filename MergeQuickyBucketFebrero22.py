import random
#Input: Dos arreglos ordenados
#Output: El arreglo combinado ordenado
def Comb(A,B):
	i = 0 #puntero de A
	j = 0 #puntero de B
	C = [] #resultado
	while i<len(A) and j<len(B):
		if A[i]<=B[j]:
			C.append(A[i])
			i+=1
		else:
			C.append(B[j])
			j+=1
	#Al final puede que tenga un arreglo no vacio
	return C+A[i:]+B[j:]
def Merge(A):
	#Caso base
	if len(A)<=1:
		return A
	A1 = Merge(A[:len(A)//2])
	A2 = Merge(A[len(A)//2:])
	return Comb(A1,A2)
#######################################
#Input: Un arreglo
#Return: El arreglo ordenado
def quick1(A):
	if len(A)<=1:
		return A
	piv = len(A)-1
	piv = random.randint(0,len(A)-1)
	menores = []
	mayores = []
	for j in range(len(A)):
		if j==piv:
			continue
		if A[j]<=A[piv]:
			menores.append(A[j])
		else:
			mayores.append(A[j])
	return quick1(menores)+[A[piv]]+quick1(mayores)
##### QuickSort
def particion(A,iz,der):
	i = iz-1 #inicializo mi frontera a izquierda
	piv = A[der]
	for j in range(iz,der):
		if A[j]<=piv:
			i+=1 #frontera aumenta
			A[i],A[j]=A[j],A[i]
	i+=1
	A[der],A[i]=A[i],A[der]
	return i
#Input: Mi arreglo A, puntero a iz y un puntero a der
def quickSort(A,iz,der):
	if iz>=0 and der>=0 and iz<der:
		front = particion(A,iz,der)
		quickSort(A,iz,front-1)
		quickSort(A,front+1,der)
#########
#Input: Arreglo A. Mi colio es [n]
def bucketSort(A,n):
	C = [0 for i in range(n)]
	for x in A:
		C[x-1]+=1
	z = []
	for i in range(n): #itero el colio
		for j in range(C[i]):
			z.append(i+1)
	return z
A = [random.randint(1,5) for i in range(20)]
print(A)
print(bucketSort(A,5))
#quickSort(A,0,len(A)-1)
#print(A)

