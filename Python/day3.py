def weird_or_not(number):
    if (number % 2) == 0:
        if number >= 2 and number <= 5:
            print("Not Weird")
        elif number >= 6 and number <= 20:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")
    

if __name__ == '__main__':
    n = int(input().strip())
    weird_or_not(n)