# Write a python Program to transport company charges the fare

num = int(input("enter the km distance: "))
if 0 < num < 51:
    res = num * 8
    print("charge on your distance is", res)

elif 50 < num < 101:
    res = num * 10
    print("charge on your distance is", res)
elif num > 100:
    res = num * 12
    print("charge on your distance is", res)

# Output:
# enter the km distance: 51
# charge on your distance is 510

# enter the km distance: 90
# charge on your distance is 900

# enter the km distance: 200
# charge on your distance is 2400