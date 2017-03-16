'''
	Check if the there is an equal number of Xs and Os in a string
'''
def xo(s):
    ret = 0
    num_of_x = [ret for elem in s if elem.lower() == "x"]
    num_of_o = [ret for elem in s if elem.lower() == "o"]
    if len(num_of_x) == len(num_of_o):
        return True
    else:
        return False