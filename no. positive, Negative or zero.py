# Write Python program to check if a Number is Positive,Negative or Zero

num = int(input("Enter a number: "))
print(num)
if num > 0:
    print("positive number.")
elif num == 0:
    print("Zero number.")
else:
    print("Negative number.")

# Output:Enter a number: 10
# 10
# positive number.

# Enter a number: -4
# -4
# Negative number.

# Enter a number: 0
# 0
# Zero number.