def sol2():
    nums = []
    with open("numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            try:
                num = int(line.strip())
                nums.append(num)
            except ValueError:
                pass
            
    with open("result.txt", "w", encoding="utf-8") as file2:
        if nums:
            file2.write(f"Min: {min(nums)}\n")
            file2.write(f"Max: {max(nums)}\n")
            file2.write(f"Average: {sum(nums) / len(nums)}")
        else:
            file2.write("No valid numbers")


sol2()
