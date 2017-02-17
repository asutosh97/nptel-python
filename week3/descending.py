def descending(l):
	for i in range(0,len(l)):
		if i == 0:
			continue
		else:
			if l[i] > l[i-1]:
				return False
	return True

