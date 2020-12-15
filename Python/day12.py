class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber,scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        grade = ''
        mean = sum(self.scores)/len(self.scores)
        if mean >= 90 and mean <= 100:
            grade = 'O'
        if mean >= 80 and mean < 90:
            grade = 'E'
        if mean >= 70 and mean < 80:
            grade = 'A'
        if mean >= 55 and mean < 70:
            grade = 'P'
        if mean >= 40 and mean < 55:
            grade = 'D'
        elif mean < 40:
            grade = 'T'
        return grade


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())