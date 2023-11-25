

def len_s(chislo, syst):
	c = 0
	while chislo > 0:
		chislo //= syst
		c += 1
	return c


def to(chislo, sys):
	chislo = abs(chislo)
	a = '0123456789ABCDEF'
	s = ''
	while chislo != 0:
		digit = chislo % sys
		chislo = chislo // sys
		s = a[digit] + s
	return s


def f33():
	mn = 10**4
	mx = 0
	for n in range(1000, 10000):
		if (n % 5 != 0) and (n % 7 != 0) and (n % 11 != 0) and (len_s(n, 3) == 8):
			mn = min(mn, n)
			mx = max(mx, n)
	print(mn, mx)


def f34():
	mn = 10 ** 4
	mx = 0
	for n in range(1000, 10000):
		if (n % 3 != 0) and (n % 17 != 0) and (n % 19 != 0) and (len_s(n, 4) == 6):
			mn = min(mn, n)
			mx = max(mx, n)
	print(mn, mx)


def f37():
	count = 0
	mn = 8000
	for n in range(3905, 7999):
		if (n % 100 // 10 != 0) and (n % 100 // 10 != 5) and (2 <= n % 1000 // 100 <= 6):
			count += 1
			mn = min(mn, n)
	print(count, mn)


def f41():
	mx = 0
	count = 0
	for n in range(2371, 9433):
		if (n % 64 // 8 == 1 and (n % 8 == 5 or n % 8 == 7)) and n % 5 != 0 and n % 3 != 0:
			count += 1
			mx = max(mx, n)
	print(count, mx)


def f43():
	count = 0
	mn = 8000
	for i in range(3721, 7753):
		n = i
		s = 0
		while n > 0:
			s += n % 10
			n //= 10
		if s % 3 == 0 and to(i, 2)[-3:] != '000':
			mn = min(mn, i)
			count += 1
	print(count, mn)


def f51():
	mx = 0
	count = 0
	for n in range(117649, 823542+1):
		if n % 3 == 2 and n % 8 != 3 and n % 12 != 5:
			count += 1
			mx = max(mx, n)
	print(count, mx)


def f52():
	count = 0
	mx = 0
	for n in range(1000, 70000):
		if len(to(n, 8)) == 5 and len(to(n, 5)) == 6 and (to(n, 16)[-2:] == 'FA'):
			count += 1
			mx = max(mx, n)
	print(count, mx)


f52()
