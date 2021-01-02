# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import datetime


class Date:
    def __init__(self,string):
        day,month,year = string.split()
        
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
    def is_earlier(self,other):
        if self.year < other.year:
            return True
        elif self.year == other.year and self.month < other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day < other.day:
            return True
        else:
            return False

returned_date = Date(input())
due_date = Date(input())


if returned_date.is_earlier(due_date):
    print(0)
elif returned_date.month == due_date.month and returned_date.year == due_date.year:
    days = returned_date.day - due_date.day
    print(days*15)
elif returned_date.month != due_date.month and returned_date.year == due_date.year:
    months = returned_date.month - due_date.month
    print(months*500)
elif returned_date.year > due_date.year:
    print(10000)