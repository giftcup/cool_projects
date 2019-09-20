#Make a simple calculator to add, substract, multiply and divide two numbers
#This function adds two numbers
def add (x,y):
    return x + y
#This function subtracts two numbers
def substract (x,y):
    return x-y
#This function multiplies two numbers
def multiply (x,y):
    return x*y
#This function divides two numbers
def divide (x,y):
    return x/y
#This function finds the lcm of two numbers
def lcm (x,y) :
    return lcm
def greet_user():
    Print("Welcome to my space, I'll crunch the numbers for you!")

#Let user choose function
print ("Select operation")
print ('1.add')
print ('2.subtract')
print ('3.multiply')
print ('4.divide')


choice = input('Enter choice 1/2/3/4:')

x = int (input('Enter a number: '))
y = int (input('Enter another number: '))

if choice == '1':
    print(x, '+', y, '=', add(x,y))
elif choice == '2':
    print (x, '-', y, '=', subtract(x,y))
elif choice == '3':
    print(x, '*', y, '=', multiply(x,y))
elif choice == '4':
    print (x, '/', y, '=', divide(x,y))
else:
    print('Invalid input')
