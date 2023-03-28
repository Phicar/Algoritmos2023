ady = [[2,3],[3],[0],[0,1]]
vis = []
def dfs(x,y):

	if x==y:
		return True
	vis[x]=True
	print(x,y,vis)
	var = False
	for z in ady[x]:
		if not vis[z]:
			var = var or dfs(z,y)
	return var
vis = [False for i in range(len(ady))]
print(dfs(0,1))
