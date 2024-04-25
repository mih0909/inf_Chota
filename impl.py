print('A B C | F | G')
for A in 0,1:
	for B in 0, 1:
		for C in 0, 1:
			O = (A <= B) <= C
			G = A and not(B) or C
			print(A, B, C, "|", int(O), "|", int(G))