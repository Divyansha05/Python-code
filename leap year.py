# Write Python program to check leap year

year = int(input("Enter the year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year.".format(year))

elif (year % 4 == 0) and (year % 100 == 0):
    print("{0} is a leap year.".format(year))

else:
    print("{0} is not a leap year.".format(year))

# Output:Enter the year: 2024
# 2024 is a leap year.

#Output:Enter the year: 2025
#2025 is not a leap year.

