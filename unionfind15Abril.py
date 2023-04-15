ady = [[2,4],[5],[0,4],[5],[0,2],[1,3,6],[5]]
pad = [x for x in range(len(ady))]
def find(x):
	if x==pad[x]:
		return x # ya es raiz
	return find(pad[x])
def union(x,y):
	global pad
	px = find(x)
	py = find(y)
	if px<py:
		pad[py]=px
	else:
		pad[px]=py
for x in range(len(ady)):
	for y in ady[x]:
		union(x,y) #uno a x y y por su arista
cc = 0 #comp. conexas
for i in range(len(ady)):
	if i==pad[i]:
		cc+=1
print(pad,cc)
		

