#Bellman-Ford: Parte de la tarea
INF = 10**10
def dijkstra(A,x):
        d = [INF for i in range(len(A))] #inicializo en INF
        d[x]=0
        #Visitados Jonathan.
        q = [True for i in range(len(A))] #q[x] is verd. sii x en q.
        while True:
                u = -1
                mini = INF
                for z in range(len(q)): #computa el argmin
                        if q[z] and d[z]<=mini:
                                u = z
                                mini = d[z]
                if u==-1: #no encontre a nadie en q, termine
                        break
                q[u]=False #saco a u de q
                for y in range(len(A[u])): #itero sobre vecinos que estan en q
                        if A[u][y]==0 or not q[y]:
                                continue
                        alt = d[u]+A[u][y]
                        if alt<d[y]: #actualizo distancia
                                d[y]=alt
        return d
A = [[0,5,10,0,0],[0,0,3,9,2],[0,2,0,1,0],[0,0,0,0,4],[7,0,0,6,0]]
print(dijkstra(A,0))
