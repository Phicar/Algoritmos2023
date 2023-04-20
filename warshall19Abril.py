n=3
ady =[[False,True,False],[False,False,True],[False,False,False]]
adyc =[[False for i in range(n)] for j in range(n)]
def W(x,y,k):
	print(x,y)
	if k==0:
		return ady[x][y]
	return W(x,y,k-1) or (W(x,k,k-1) and W(k,y,k-1))

for x in range(n):
	for y in range(n):
		adyc[x][y]=W(x,y,n-1)
print(adyc)

