def add(a, b):
    return a + b

def divide(a, b):
    return a / b  # bug: no check for division by zero

def greet(name):
    print("Hello " + name)  # should use f-string

def get_user(users, id):
    for i in range(len(users)):  # bad practice: should use enumerate
        if users[i]["id"] == id:
            return users[i]

x = 10
y = 0
print(divide(x, y))  # this will crash!