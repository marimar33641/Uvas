from sys import stdin
def phi(p, n, x, a, mem):
	ans = None
	if (n,x) in mem: ans = mem[(n,x)]
	else:
		if(x > 5000): ans = (a * 100) / x
		elif(x <= 5000 and n == 0): ans = 0
		else:
			ans = max(phi(p, n - 1, x, a, mem), phi(p, n - 1, x + p[n - 1], a, mem))
		mem[(n,x)] = ans
	return ans

def main():
	n, x = map(int, stdin.readline().split())
	while(n != 0 and x != 0):
		p = list()
		for j in range( n ):
			p.append(float(stdin.readline().strip())*100)
		i = p.pop(x-1)
		ans = phi(p, n - 1, i, i, {})
		print("%.2f" % ans)
		n, x = map(int, stdin.readline().split())

main()
