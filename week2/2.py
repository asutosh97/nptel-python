def matched(s):
	Braces = 0
	for c in s:
		if c == '(':
			Braces = Braces + 1
		elif c == ')':
			if Braces > 0:
				Braces = Braces - 1
			else:
				return False
	
	if not Braces:
		return True
	else:
		return False

print matched("zb%78")
print matched("(7)(a")
print matched("a)*(?")
print matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
