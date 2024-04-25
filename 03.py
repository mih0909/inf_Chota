from random import randint
def a1(x):
	r = randint(0,1)
	if r:
		return x + 1
	return x - 1


def B(x):
	if x % 3 == 0:
		return b1(x)
	else:
		return b2(x)

def b1(x):
	r = randint(1, 100)
	if r < 11:
		return x + 1
	else:
		return x - 1

def b2(x):
	r = randint(1, 100)
	if r < 76:
		return x + 1
	else:
		return x - 1


c = 0
for j in range(10):
	for i in range(1000000):
		r = randint(1,1)
		if r:
			c = a1(c)
		else:
			c = B(c)
	# print([False, True][c >= 0])
	print(c)
	c = 0
