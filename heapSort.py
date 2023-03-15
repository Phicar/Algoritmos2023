#A es arreglo
#retorno A arreglado
def heapSort(A):
	h = []
	for i in range(len(A)):
		h.append(A[i])
		ind = len(h)
		while ind>1:
			pad = ind//2
			if h[ind-1]>h[pad-1]:
				h[ind-1],h[pad-1]=h[pad-1],h[ind-1]
				ind = pad
			else:
				break
	############ Ya tengo mi heap
	sor = []
	while len(h)>0: #mientras tenga heap, hagale
		h[0],h[-1]=h[-1],h[0] # los intercambio
		r = h.pop() #longitud de h disminuye en 1
		sor.append(r)
		ind = 1
		while True:
			print(h)
			iz = 2*ind
			der= 2*ind+1
			maxi = -1 #el maximo de los hijos de ind
			maxiInd = -1 #el indice del maximo
			if iz<=len(h) and h[ind-1]<h[iz-1]:
				maxi = h[iz-1]
				maxiInd = iz
			if der<=len(h) and h[ind-1]<h[der-1]:
				if maxi< h[der-1]:
					maxi = h[der-1]
					maxiInd = der
			if maxi == -1:
				break
			h[ind-1],h[maxiInd-1]=h[maxiInd-1],h[ind-1]
			ind = maxiInd
	return sor
print("-->",heapSort([4,3,5,7,1]))
			
		
