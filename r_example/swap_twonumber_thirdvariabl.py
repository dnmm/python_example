# Python program to swap two variables

x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')
print('The value of x befor swapping',x)
print('The value of y befor swapping',y)
# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping',x)
print('The value of y after swapping',y)

# print('The value of x after swapping: {}'.format(x))
# print('The value of y after swapping: {}'.format(y))
