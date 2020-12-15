#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    binary = format(n, "b")
    
    max_ones = 0
    current_ones = 0
    for char in binary:
        if char == '1':
            current_ones += 1
            if current_ones > max_ones:
                max_ones = current_ones
        elif current_ones > 0:
            current_ones = 0
                
    print(max_ones)
                
