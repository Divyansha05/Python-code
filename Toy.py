# Write a python program that reads the product code and the order amt and prints out the net amt that the customer is reguired to pay after the discount

print("1.Battery toy\n2.Key based \n3.Electrical based")
num=int(input("enter the number of toy:"))
amount=int(input("enter the amount:"))
if num==1:
    total=amount
    dis=0
    if amount>1000:
        dis=(amount*10)/100
        total=amount-dis
    print("discount",dis)
    print("total amount is:",total)
if num==2:
    total=amount
    dis=0
    if amount>100:
        dis=(amount*5)/100
        total=amount-dis
    print("discount",dis)
    print("total amount is:",total)
if num==3:
    total=amount
    dis=0
    if amount>500:
        dis=(amount*10)/100
        total=amount-dis
    print("discount",dis)
    print("total amount is:",total)

# Output:
# 1.Battery toy
# 2.Key based
# 3.Electrical based
# enter the number of toy:2
# enter the amount:600
# discount 30.0
# total amount is: 570.0

# 1.Battery toy
# 2.Key based
# 3.Electrical based
# enter the number of toy:1
# enter the amount:1200
# discount 120.0
# total amount is: 1080.0

# 1.Battery toy
# 2.Key based
# 3.Electrical based
# enter the number of toy:3
# enter the amount:700
# discount 70.0
# total amount is: 630.0