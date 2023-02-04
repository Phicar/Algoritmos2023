tmp = []
vis=[]
#El i es en que posicion estoy asignando la permutacion.
def permUnica(i):
    global tmp,vis #Me deja modificar variables de afuera
    if i==len(tmp):
        #ACA YA TENGO MI PERMUTACION.
        print(tmp,vis)
        return
    for j in range(len(tmp)-1,-1,-1): #Loop de adentro.
        if not vis[j]:
            tmp[i]=j+1
            vis[j]=True
            permUnica(i+1)
            vis[j]=False
def permutaciones(n):
    global tmp,vis
    tmp = [0 for i in range(n)]
    vis = [False for i in range(n)]
    permUnica(0)
    # vis va a volver a ser False

#X: lista
#Algoritmo para ordenar prueba Prop1.
def sort(X):
	if len(X)<2:
		return X
	a = X[-1]
	XS = []
	XT = []
	for i in range(len(X)-1):
		if X[i]<a:
			XS.append(X[i])
		else:
			XT.append(X[i])
	XSOrd = sort(XS)
	XTOrd = sort(XT)
	return XSOrd+[a]+XTOrd
#Generar perm. usando A_n = A_{n-1}x[n]
#n: entero positivo
def Perm(n):
	if n==1: #Caso base
		return [[1]]
	B = Perm(n-1) #ESTA ES LA RECURSION..A_{n-1}
	C = []
	for x in B:
		for i in range(n):
			#Tengo una pareja ordenada (i,x)
			#Aplicar la funcion phi.
			y = x[0:i]+[n]+x[i:]
			C.append(y)
	return C
permutaciones(3)
