dist = []
ant = []
INF = 10**10
#Matriz de adyacencia---> asigno 0 si dos nodos no se ven.
def camino(i,j): #retornar el camino mas corto de i a j. Si no hay, retorne []

def floyd(A):
	global dist,ant
	#Primero es el caso base->k=0
	dist = [[INF for j in range(len(A))] for i in range(len(A))]
	ant = [[-1 for j in range(len(A))] for i in range(len(A))]
	for i in range(len(A)):
		for j in range(len(A)):
			if i==j:
				dist[i][j]=0
				ant[i][i]=i
			elif A[i][j]!=0:
				dist[i][j]=A[i][j]
				ant[i][j]=i
	for k in range(0,len(A)):
		for i in range(len(A)):
			for j in range(len(A)):
				pos = dist[i][k]+dist[k][j]
				if pos<dist[i][j]:
					dist[i][j]=pos
					ant[i][j]=ant[k][j]
	#aca ya tengo en dist las distancias mas cortas.
floyd([[0,0,0,3],[0,0,0,2],[2,4,0,7],[0,0,0,0]])
print(dist)
