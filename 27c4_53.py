
n = int(input())
t = int(input())
t_b = t_a = 0 
for i in range(n):
	a, b = map(int, input().split())
	t_a += a
	t_b += b
	if t_b > t_a:	
		t_b = t_a
print(t_b + t)
"""
3
20
320 150
300 230
2000 440