import re

logs = [
    "2026-09-24 10:15:32 INFO Пользователь 123 вошёл в систему",
    "2026-09-24 10:16:04 ERROR Пользователь 456: ошибка проверки входа",
    "2026-09-24 10:17:21 INFO Пользователь 123 открыл страницу",
    "2026-09-24 10:18:45 WARNING Пользователь 789: слишком много запросов",
    "2026-09-24 10:19:02 ERROR Пользователь 123: ошибка подключения к базе данных",
]
pattern = r"(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>INFO|WARNING|ERROR) Пользователь (?P<user_id>\d+)[: ]+(?P<message>.+)"
for line in logs:
    match = re.search(pattern, line)

    if match:
        data = match.groupdict()
        print(data)
