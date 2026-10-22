from contextlib import contextmanager


@contextmanager
def log_operation(path, operation):
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"НАЧАЛО: {operation}\n")

    try:
        yield
    except Exception:
        with open(path, "a", encoding="utf-8") as file:
            file.write(f"ОШИБКА: {operation}\n")
        raise
    else:
        with open(path, "a", encoding="utf-8") as file:
            file.write(f"КОНЕЦ: {operation}\n")


with log_operation("operation.log", "Обработка данных"):
    print("обрабатываем данные")
