def factors(n):
	flist = []
	for i in range(1, n+1):
		if n % i == 0:
			flist = flist + [i]
	return flist

def isprime(n):
	if(factors(n) == [1, n]):
		return True
	else:
		return False

def sumprimes(l):
	sum = 0
	for i in l:
		if isprime(i):
			sum = sum + i
	return sum

sumprimes([3,3,1,13])
