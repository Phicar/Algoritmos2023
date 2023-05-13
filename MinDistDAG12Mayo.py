vis = []
L = []
A = []
def dfs(x):
	global vis,L
	#print(x,len(vis ))
	vis[x]=0
	for y in range(len(A[x])):
		if A[x][y]>0 and vis[y]==-1:
			dfs(y)
	vis[x]=1
	L.append(x)
def ordTop(G):
	global L,A,vis
	A = G[:]
	L = []
	vis = [-1 for x in range(len(A))]
	for x in range(len(A)):
		entra = False
		for y in range(len(A)):
			if A[y][x]>0:
				entra = True
				break
		if not entra:
			#print(x,"no tiene entrada")
			dfs(x)
	L.reverse()
	return L
#print(ordTop([[0,1,1,0,0],[0,0,1,1,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0]]))
#print(ordTop([[0,0,5,0],[0,0,0,0],[0,0,0,0],[0,6,0,0]]))
def minDist(A,x):
	dist = [10**10 for i in range(len(A))]
	dist[x]=0
	T = ordTop(A)
	for i in range(len(A)):
		for z in range(len(A)):
			if A[T[i]][z]>0:
				alt = dist[T[i]]+A[T[i]][z]
				if dist[z]>alt:
					dist[z]=alt
	return dist
for x in range(5):
	print(x,minDist([[0,2,6,0,0],[0,0,3,3,0],[0,0,0,1,0],[0,0,0,0,5],[0,0,0,0,0]],x))
