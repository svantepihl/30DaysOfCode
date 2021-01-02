import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here


def swap(i, j, values):
    temp = values[j]
    values[j] = values[i]
    values[i] = temp


def bubble_sort(values):
    sorted = False
    length = len(values)
    swap_count = 0
    while not sorted:
        sorted = True
        for i in range(length-1):
            if values[i] > values[i+1]:
                swap(i, i+1, values)
                sorted = False
                swap_count += 1
    return swap_count


print('Array is sorted in ' + str(bubble_sort(a)) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[len(a)-1]))
