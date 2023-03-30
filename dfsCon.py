vis =[]
cic = False
def dfs1(act,ant):
	global vis,cic
	vis[act]=True
	for z in ady[act]:
		if not vis[z]:
			dfs1(z,act)
		else:
			if z!= ant and ant!=-1:
				print(ant,act,z)
				cic = True

def dfs(x):
	global vis
	#print(x+1)
	vis[x]=True
	for z in ady[x]:
		if not vis[z]:
			dfs(z)
ady = [[2,4,5],[],[0,4,6],[],[0,2,5],[0,4],[2,9],[8],[7],[6]]
def aciclico(ady):
	global vis,cic
	cic = False
	vis = [False for x in range(len(ady))]
	for x in range(len(vis)):
		if not vis[x]:
			dfs1(x,-1)
			if cic:
				return False
	return True
def compConex(ady):
	global vis
	vis = [False for x in range(len(ady))]
	print(vis)
	conex = 0
	for x in range(len(vis)):
		if not vis[x]:
			dfs(x)
			conex+=1
	return conex #print(conex)
print(aciclico(ady))