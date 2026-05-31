def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def greet(name):
    print(f"Hello {name}")

def get_user(users, id):
    for i, user in enumerate(users):
        if user["id"] == id:
            return user

x = 10
y = 2
print(divide(x, y))