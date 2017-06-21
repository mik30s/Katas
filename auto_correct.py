from collections import defaultdict

# build ditionary
def build_dict(filename):
	oxdict = defaultdict(list)
	with open(filename, encoding='utf-8') as file:
		for line in file: oxdict[line[0:1]].append(line.strip("\n"))
	return oxdict

# compute edit distance
def compute_distance(source, target):
	n, m = len(source), len(target)
	# print(n,m)
	matrix =  [[0]*(n+1) for i in range(m+1)]
	for i in range(n+1): matrix[0][i] = i
	for j in range(m+1): matrix[j][0] = j
	for i in list(range(1,m+1)):
		for j in list(range(1,n+1)):
			# print(i,j)
			cost = 0 if source[j-1] == target[i-1] else 1
			matrix[i][j] = min([matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + cost])
	return matrix[m][n]


word, word_dict = "", build_dict("words.txt")
while(word != "q"):
	word = input("your word: ")
	if word in word_dict[word[0:1]]: print(word)
	else: 
		#print("is not in")
		distances = {}
		correct = ""
		for w in word_dict[word[0:1]]: 
			distances[w] = compute_distance(w,word)
		correct = min(distances, key=distances.get)
		print("corrected: ", correct)