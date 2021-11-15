#A SIMPLE FACTORIAL CALCULATOR

#asking for a number
factorial = int(input("Give a number you want to know the factorial of: "))
output = 1
#a loop to calculate the factorial
for i in range(2, factorial + 1):
    output *= i
#print the result
print(output)
input("press enter to exit")