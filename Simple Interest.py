# Write a python program to find Simple Interest on Rs.200 for 5 years at 5% per year

principal_amount = 200
time = 5
interest_rate = 5

total_interset = (principal_amount*time*interest_rate)/100

print("Total interset you have to pay:",total_interset)

# Output: Total interset you have to pay: 50.0


def simple_interest(amount,time,rate = 5):
    print(f"\nPrincipal Amount: Rs{amount}")
    print(f"Time Period: {time} years")
    print(f"Interest Rate: {rate}%")

    total_interest = (amount * time * rate) / 100

    print(f"Total Interest you have to pay is: Rs {total_interest}")

amt = int(input("How much amount you want: "))
time = int(input("For many years: "))

simple_interest(amt,time)

# Output:
# How much amount you want: 200
# For many years: 5
#
# Principal Amount: Rs200
# Time Period: 5 years
# Interest Rate: 5%
# Total Interest you have to pay is: Rs 50.0