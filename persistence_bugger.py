'''
    Find which digits in a number produce a single
    digit number when multiplied with each other
'''
def persistence(num):
    iters = 0
    while len(str(num)) > 1:
        prod = get_product(num)
        iters = iters + 1
        num = prod
    return iters
        
# Return product of digits in a number   
def get_product(num):
    prod = 1
    for d in str(num):
        prod = prod * int(d)
    return prod
    