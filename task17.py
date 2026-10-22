def sol17():
    total = 0
    count = 0
    first = True
    with open("numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            num = int(line.strip())
            total += num
            count += 1
            if first:
                minnum = num
                maxnum = num
                first = False

            minnum = min(minnum, num)
            maxnum = max(maxnum, num)
    if count > 0:
        print("сумма:", total)
        print("минимум:", minnum)
        print("максимум:", maxnum)
        print("количество чисел:", count)
        print("среднее:", total / count)
    else:
        print("в файле ниче нету")


sol17()
