from sys import stdin
entries = int(input())

phonebook = dict()

for i in range(entries):
    name, number = input().split()
    phonebook[name] = number
    
for line in stdin:
    key = line.strip()
    if key in phonebook:
        print(key + '=' + phonebook[key])
    else:
        print('Not found')