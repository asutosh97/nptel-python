def alternating(l):
	n = len(l)

	if n == 0 or n == 1:
		return True

	elif n == 2:
		diff = l[0] - l[1]
		if diff:
			return True
		else:
			return False

	else:
		flag = False
		prev = l[1] - l[0]
		for i in range(1,n-1):
			diff = l[i+1] - l[i]
			if (diff > 0 and prev > 0) or (diff < 0 and prev < 0) or (prev == 0) or (diff == 0):
				flag = True
				break
			prev = diff

		if flag == True:
			return False
		else:
			return True