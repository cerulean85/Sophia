# 괄호 쌍 경우의수, 카탈란 수

# Bottom-Up
# def binomial(bin, n, k):
# 	for i in range(0, n + 1):
# 		for j in range(0, k + 1):
# 			if j > i: break;
# 			if bin[i][j] > 0 : continue
# 			if j == 0 or i == j: bin[i][j] = 1
# 			else: bin[i][j] = int(bin[i - 1][j] + bin[i - 1][j - 1])
# 	return bin[n][k]

#Top-Down
def binomial(bin, n, k):
	if n==k or k==0 : return 1
	elif bin[n][k] > 0 : return bin[n][k]
	else :
		bin[n][k] = binomial(bin, n-1, k) + binomial(bin, n-1, k-1)
		return bin[n][k]


def cataln(n) :
	bin = [[0 for col in range(2*n + 1)] for row in range(2*n + 1)]
	return binomial(bin, 2*n, n) - binomial(bin, 2*n, n+1)

print(cataln(5))