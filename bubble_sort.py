def bubble_sort(items):
	for i in range(1, len(items) - 1):
		j = i
		while j > 0 and items[j] > items[j + 1]:
			# swap elements
			temp = items[j]
			items[j] = items[j + 1]
			items[j + 1] = temp
			j = j-1
	return items

print(bubble_sort([1,2,1,6,4,7,4]))
