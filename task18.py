import re
import json
import logging
from collections import Counter
logging.basicConfig(
    filename="processing.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

def sol18():
    requests = Counter()
    urls = Counter()
    errors = 0

    pattern = r"(\d+\.\d+\.\d+\.\d+) (\w+) (\S+) (\d{3})"
    try:
        with open("access.log", "r", encoding="utf-8") as file:
            for line in file:
                match = re.search(pattern, line)

                if not match:
                    logging.warning("Строчка журнала имеет неверный формат")
                    continue
                ip = match.group(1)
                method = match.group(2)
                url = match.group(3)
                code = int(match.group(4))
                requests[method] += 1
                urls[url] += 1

                if 400 <= code < 500:
                    errors += 1

        if urls:
            most_common_url = urls.most_common(1)[0][0]
        else:
            most_common_url = None

        result = {
            "всего запросов по методам": dict(requests),
            "всего ошибок 4xx": errors,
            "Самый популярный адрес": most_common_url
        }
        with open("stats.json", "w", encoding="utf-8") as file:
            json.dump(result, file, ensure_ascii=False, indent=4)

        logging.info("Обработка завершена")
        print("Результат сохранён в stats.json")

    except FileNotFoundError:
        logging.error("Файл access.log не найден")
        print("Файл access.log не найден")
    except PermissionError:
        logging.error("Нет прав на чтение access.log")
        print("Нет прав на чтение файла")
    except OSError as error:
        logging.error("Ошибка при работе с файлом: %s", error)
        print("Ошибка при работе с файлом")


sol18()
