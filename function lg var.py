value = 10  # global variable


def sample():
    value = 30
    value = value + 1
    print(value)


sample()
print(value)


def sam(name, age=20):
    print(name, age)


sam(name="hello")


def sa(num1, num2):
    sum = num1 + num2
    return sum


result=sa(10, 15)
print(result)