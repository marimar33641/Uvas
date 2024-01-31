from sys import stdin


def sol(i, _ans):
	global codes, letters, ans, cnt
	if i == len(ans) and cnt < 100:
		print(_ans)
		cnt += 1
	elif cnt < 100:
		for k in range(26):
			_min = chr(k+97)
			if _min in letters:
				ok, anscpy, j = True, '', i
				while j < len(ans) and ok and cnt < 100:
					anscpy += ans[j]
					if codes.get(int(anscpy)) != None and codes[int(anscpy)] == _min:
						sol(j+1, _ans+codes[int(anscpy)])
					j, ok = j+1, int(anscpy) <= 99



def main():
	global codes, letters, ans, cnt
	N, TC = int(stdin.readline().strip()),1
	while N:
		codes, letters = {}, set()
		for _ in range(N):
			l, n = map(str, stdin.readline().strip().split())
			codes[int(n)] = l
			letters.add(l)
		ans = stdin.readline().strip()
		cnt = 0
		print("Case #{0}".format(TC))
		sol(0,'')
		TC += 1
		N = int(stdin.readline().strip())
		print("")
        




main()