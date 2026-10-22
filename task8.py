def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("файла нету")
    except PermissionError:
        print("нет прав на чтение файла")
    except UnicodeDecodeError:
        print("не удалось прочитать текст файла")
    except OSError:
        print("ошибка операционной системы")
    return None


text = read_file("text.txt")
if text is not None:
    print(text)
