def matmult(m, n):
	result = [[0 for x in range(len(m))] for y in range(len(n[0]))]
	for i in range(len(m)):
		for j in range(len(n[0])):
			for k in range(len(n)):
				result[i][j] += m[i][k] * n[k][j]

	return result
