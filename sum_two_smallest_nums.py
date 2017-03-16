'''
Find the smallest of two numbers and return their sum
'''
def sum_two_smallest_numbers(numbers):
    newArray = sorted(numbers)
    return sum(newArray[0:2])