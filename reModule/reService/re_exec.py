import re


def get_nickname(text):
    nickname = re.split(r'@', text)[0]
    return nickname


def get_domain(text):
    domain = re.split(r'@', text)[1]
    return domain


print(get_nickname("user@example.com"))
print(get_domain("user@example.com"))
