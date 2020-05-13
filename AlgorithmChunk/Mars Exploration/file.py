"""Sample Input 0

SOSSPSSQSSOR

Sample Output 0

3"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    listofExplore = ["S","O","S"]
    count =0
    intcount = 0
    for i in s:
        if listofExplore[intcount] != i:
            count+=1
        intcount+=1
        if intcount > (len(listofExplore)-1):
            intcount = 0
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
