import re


def get_nickname(text):
    nickname = re.split(r'@', text)[0]
    return nickname


def get_domain(text):
    domain = re.split(r'@', text)[1]
    return domain
