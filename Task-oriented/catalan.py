#올바른 괄호란 (())나 ()와 같이 올바르게 모두 닫힌 괄호를 의미합니다. 
#)(나 ())() 와 같은 괄호는 올바르지 않은 괄호가 됩니다. 괄호를 이리저리 움직이며 올바른 괄호를 찾던 민호는 N개의 괄호쌍이 있을 때, 
#올바른 괄호를 만들 수 있는 경우의 수가 궁금해졌습니다. 괄호 쌍의 개수 N개가 주어졌을 때, 경우의 수를 반환하는 parenthesisCase 함수를 
#완성해 보세요. 예를 들어
#  - N = 1일 경우는 () 의 1가지만 존재하므로 1을 리턴하면 됩니다.
#  - 3일 경우에는 ((())), (())(), ()(()), ()()(), (()()) 의 5가지가 존재하므로 5를 리턴하면 됩니다.

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
