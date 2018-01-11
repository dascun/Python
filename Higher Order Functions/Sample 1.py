#!/bin/python3

import sys
import os

#Write detecter implementation
def detecter(element):
    
    #Write isIn implementation    
    def isIn(sequence):
        return 'True' if element in sequence else 'False'
    
    return isIn

#Write closure function implementation for detect30 and detect45
detect30 = detecter(30)
detect45 = detecter(45)

print(detect30)
print(detect45)

if __name__ == "__main__":
	with open(os.environ['OUTPUT_PATH'], 'w') as fout:
		func_lst = [detect30, detect45]
		res_lst = list()
		lst = list(map(lambda x: int(x.strip()), input().split(',')))
		for func in func_lst:
			res_lst.append(func(lst))
		fout.write("{}\n{}".format(*res_lst))