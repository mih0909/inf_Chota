def to(chislo, sys):
	chislo = abs(chislo)
	A = '0123456789ABCDEF'
	s = ''
	while chislo != 0:
		digit = chislo % sys
		chislo = chislo // sys
		s = A[digit] + s
	return s

def frm(chislo, sys):
	D = {'0':0, '1':1, '2':2, '3':3,
	    '4':4, '5':5, '6':6, '7':7,
	    '8':8, '9':9, 'A': 10, 'B':11,
	    'C':12, 'D':13, 'E':14, 'F':15}
	l = len(chislo)
	n = 0
	p = 1
	while l != 0:
		digit = chislo[l-1]
		if D.get(digit) > sys:
			return -1234567890
		n += D.get(digit) * p
		l -= 1
		p *= sys
	return n
a, b = map(int, input('to \n').split())
d, c = input('frm \n').split()
print(to(a, b))
print(frm(d, int(c)))
