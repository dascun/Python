#!/bin/python3

import sys
import os

# Add the factory function implementation here
def factory(n=0):
    def current():
        return n
    def counter():
        return n+1
    return current,counter

f_current, f_counter = factory(int(input()))

if __name__ == "__main__":
	with open(os.environ['OUTPUT_PATH'], 'w') as fout:
		func_lst = [f_current, f_counter]
		res_lst = list()
		for func in func_lst:
			res_lst.append(func())
		fout.write("{}\n".format(*res_lst))