'''
Count the number of vowels in a string
'''
def getCount(inputStr):
    vowels = []
    return len([vowels for v in inputStr if v in ['a', 'e', 'o', 'i', 'u']])
    
  