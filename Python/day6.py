def even_odd(string):
    even = str()
    odd = str()
    for i in range(len(string)):
        if i % 2 == 0:
            even = even + string[i]
        else:
            odd = odd + string[i]
    print(even + ' ' + odd)

n = int(input())

for i in range(n):
    even_odd(input())
            