from email.utils import parseaddr

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_valid_email(email):
    name, addr = parseaddr(email)
    return '@' in addr and '.' in addr.split('@')[-1]

print(is_valid_email("test@example.com"))  # True
print(is_valid_email("not an email"))
