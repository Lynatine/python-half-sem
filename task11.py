import re

def sol11():
    with open("logs.txt", "r", encoding="utf-8") as file:
        text = file.read()
    users = re.findall(r"User (\d+)", text)
    errors = re.findall(r".*ERROR.*", text)
    error_users = re.findall(r"ERROR User (\d+)", text)
    print("все пользователи:", users)
    print("строчек с ошибками:")
    for line in errors:
        print(line)
    print("польхователи с ошибками:", error_users)


sol11()
