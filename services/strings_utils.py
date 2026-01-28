from email.utils import parseaddr

def count_char(s, char):
    if s is None:
        return 0
    return s.count(char)

def is_empty(s):
     return s is None or s.strip() == ""

def has_min_length(s, min_len):
    if s is None:
        return False
    return len(s) >= min_len

def is_valid_email(email):
    name, addr = parseaddr(email)
    return '@' in addr and '.' in addr.split('@')[-1]

print(is_valid_email("test@example.com"))  # True
print(is_valid_email("not an email"))