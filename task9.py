def parse_number(value):
    return float(value)

value = input("введите число: ")

try:
    num = parse_number(value)
    print("числа:", num)
except ValueError:
    print("некорректное число")
