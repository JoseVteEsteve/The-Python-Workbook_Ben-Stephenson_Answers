"""In this exercise you will create a program that computes the average of a collection
of values entered by the user. The user will enter 0 as a sentinel value to indicate
that no further values will be provided. Your program should display an appropriate
error message if the first value entered by the user is 0."""

count = 0
total = 0
flag = True
while flag == True:
	number = int(input("Introduce a number: "))
	if number == 0:
		print("Error. Zero has been entered into the program")
		flag = False
	else:
		count = count + 1
		total = total + number

average = round(total/count,2)
print("The average is",average)
