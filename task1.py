def sol1(path):
    
    linect = 0
    wordct = 0
    symbolct = 0
    longestline = 0
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip("\n")
            linect += 1
            wordct += len(line.split())
            symbolct += len(line)
            longestline = max(longestline, len(line))
    print(f"строчек:{linect}")
    print(f"слов:{wordct}")
    print(f"символов:{symbolct}")
    print(f"максимальная строка:{longestline}")


sol1("text.txt")
