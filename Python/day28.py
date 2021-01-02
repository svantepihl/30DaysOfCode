#!/bin/python3

import re

GMAIL_PATTERN = re.compile('^[\w.+\-]+@gmail\.com$')

if __name__ == '__main__':
    result = list()
    N = int(input())
    
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]
        
        emailID = firstNameEmailID[1]
        
        if GMAIL_PATTERN.match(emailID):
            result.append(firstName)
    for name in sorted(result):
        print(name)
