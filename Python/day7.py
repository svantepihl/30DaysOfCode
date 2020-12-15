n = int(input())

arr = list(map(int, input().rstrip().split()))

arr.reverse()

result = str()
for char in arr:
    result = result + str(char) + ' '
    
print(result)
    