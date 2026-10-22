from io import StringIO

def count_lines(stream):
    count = 0
    for line in stream:
        count += 1
    return count


with open("data.txt", "r", encoding="utf-8") as file:
    print("строк в файле:", count_lines(file))

text = StringIO("первая\nвторая\nтретья")
print("строк в строковом потоке:", count_lines(text))
