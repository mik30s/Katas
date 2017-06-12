def insertion_sort(items):
	"""
	Sorts a list of items based on comparison using
	the insertion sort algorithm
	Worst case O(n^2), Best case O(n) 
	"""
	i = 1
	while i < len(items):
		j = i - 1
		for e in items[0:i]:
			if items[j + 1] < items[j]:
				temp = items[j]
				items[j] = items[j + 1]
				items[j + 1] = temp
			j -= 1
		i += 1
	return items

print insertion_sort([3,4,2,1])
