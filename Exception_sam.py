b=0
try:
    a=10/b
    print(a)
    print('try completed')
except ZeroDivisionError:
    print("can't divided by zero")

print("Program completed")