def hey(name, age):
    print("My name is " + name + "age:" + str(age))


def hello():
    print("hello")


value = "Argentina "
hey(value, 23)

hello()


def hai(*val):
    print("first:" + val[0] + " second:" + val[1])


hai("ijas", "Hello", 3)
