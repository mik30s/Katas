from collections import defaultdict

def pair_sum(array, sum):
	"""
	Given a list of integers find all pairs of integers that
	add up to a given sum,
	"""
	pairs = []
	map = defaultdict(bool)
	for i,_ in enumerate(array):
		temp = sum - array[i]
		if temp >= 0 and map[temp] == True:
			pairs.append((array[i],temp))
		map[array[i]] = True
	return pairs

print(pair_sum([2,4,3,6],5))