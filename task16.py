import re


def sol16():
    stats = {"ИНФО": 0, "ПРЕДУПРЕЖДЕНИЕ": 0, "ОШИБКА": 0}
    error_users = []
    with open("logs.txt", "r", encoding="utf-8") as file:
        for line in file:
            match = re.search(r"\b(INFO|WARNING|ERROR)\b", line)
            if match:
                level = match.group(1)
                if level == "INFO":
                    stats["ИНФО"] += 1
                elif level == "WARNING":
                    stats["ПРЕДУПРЕЖДЕНИЕ"] += 1
                else:
                    stats["ОШИБКА"] += 1
            match = re.search(r"ERROR User (\d+)", line)
            if match:
                user = match.group(1)
                if user not in error_users:
                    error_users.append(user)

    for level in stats:
        print(f"{level}: {stats[level]}")
    print("Пользователи с ошибками:", error_users)


sol16()
