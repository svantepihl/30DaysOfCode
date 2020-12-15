#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    def get_max_hourglass(matrix):
        max_hourglass = -64
        for i in range(len(matrix)-2):
            for j in range(len(matrix[i])-2):
                current_hourglass = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]
                if current_hourglass > max_hourglass:
                    max_hourglass = current_hourglass
        return max_hourglass
            
    print(get_max_hourglass(arr))
