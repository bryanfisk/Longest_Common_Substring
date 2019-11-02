def LCS(v, w):	
	s = [[0 for x in range(len(v) + 1)] for y in range(len(w) + 1)]
	b = [[0 for x in range(len(v) + 1)] for y in range(len(w) + 1)]
	for i in range(1, len(w) + 1):
		for j in range(1, len(v) + 1):
			if v[j - 1] == w[i - 1]:
				s[i][j] = max([s[i - 1][j], s[i][j - 1], s[i - 1][j - 1] + 1])
			else:
				s[i][j] = max([s[i - 1][j], s[i][j - 1]])
			if s[i][j] == s[i - 1][j]:
				b[i][j] = 1
			elif s[i][j] == s[i][j - 1]:
				b[i][j] = 2
			else:
				b[i][j] = 3
	return b

def backtrack(b, w):
    output = ''
    column = len(w)
    row = len(v)
    while b[row][column] != 0:
        if b[row][column] == 1:
            row = row - 1
        elif b[row][column] == 2:
            column = column - 1
        elif b[row][column] == 3:
            column = column - 1
            row = row - 1
            output = output + w[column]
    return output[::-1]

with open('input.txt') as file:
    w = file.readline().strip()
    v = file.readline().strip()

b = LCS(w, v)
bt = backtrack(b, w)
print(bt)
output = open('output.txt', 'w')
output.write(bt)
output.close()



