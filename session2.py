#Homework: Session 2
#Additional resources:
#● Input ★ https://realpython.com/python-input-output/
#● turtle module documentation ★ https://docs.python.org/3/library/turtle.html ● for loops ★ https://realpython.com/python-for-loop/
#● functions ★ https://www.datacamp.com/community/tutorials/functions-python-tutorial
#Question 1
#Explain what this program does
for number in range(100):
    output = 'o' * number
    print(output)

#A loop that consider value from 0 to 100 not inclusive, the value 0 to 99 is rapresented by 'number'. 
#The program execute the value 'o' times number for 100 times.

#Question 2
#Your boss really likes calculating VAT on their purchases. It is their favourite hobby. They've written this code to calculate VAT and need your help to fix it.
def calculate_vat(amount):
    return amount * 1.2

total = calculate_vat(100)
print(total)
#When your boss runs the program they get the following output:
#None
#Your boss expects the program to output the value 120. What is wrong? How do you fix it?

  #The following is a function with a parameter. Inside the function there a program to be execute.
  #In order to execute and stop the program return keyword is  needed to bring out the value
  #and assign the result to a variable outside the local scope

