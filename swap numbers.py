#using input function take two numbers and then swap the number

x = 10
y = 20

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

temp = x
x = y
y = temp

print("The value of x after swapping: {}".format(x))
print("The value of y after swapping: {}".format(y))

#output:
# Enter the value of x: 10
# Enter the value of y: 20
# The value of x after swapping: 20
# The value of y after swapping: 10

#output2:
# Enter the value of x: 15
# Enter the value of y: 30
# The value of x after swapping: 30
# The value of y after swapping: 15