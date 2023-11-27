from time import time
def fib_math(n):
	return int((((1+5**0.5)/2)**n - ((1-5**0.5)/2)**n) / 5**0.5)


def fib_cyc(n):
	fib1 = 1
	fib2 = 1
	for i in range(n-2):
		fib2 = fib1 + fib2
		fib1 = fib2 - fib1
	return fib2


for i in range(72, 85):
	cyc = fib_cyc(i)
	math = fib_math(i)
	d = abs(math - cyc)
	print(cyc)
	print(math)
	print(d)

