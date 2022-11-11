import re


def validate_phone(text):
    return re.match("^1[3-9]\d{9}$", text)


def validate_email(text):
    return re.match("^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+$", text)


def validate_input(text, role=None):
    while True:
        content = input(text).strip()
        if not content:
            print('请勿输入空值!')
            continue
        if role:
            content = role(content)
            if not content:
                print('检验错误!')
                continue
            content = content.group(0)
        return content
