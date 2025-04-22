# Write Python program to Find the Largest Among Three Numbers

n1 = 10
n2 = 20
n3 = 15

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if (n1 >= n2) and (n1 >= n3):
    largest = n1
elif (n1 >= n1) and (n2 >= n3):
    largest = n2
else:
    largest = n3

print("The largest number is", largest)

# Output:
# Enter first number: 100
# Enter second number: 15
# Enter third number: 60
# The largest number is 100

# output:
# Enter first number: 10
# Enter second number: 20
# Enter third number: 15
# The largest number is 20