def intreverse(n):
	x = 0
	while n != 0:
		x = x * 10 + n % 10
		n = int(n / 10)
	return x

intreverse(783)