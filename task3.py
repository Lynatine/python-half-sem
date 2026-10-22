import csv
def sol3():
    with open("students.csv", "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        grades = []
        group_gpa = {}
        
        for row in reader:
            name = row["name"]
            group = row["group"]
            grade = int(row["score"])
            grades.append((name, grade))

            if group not in group_gpa:
                group_gpa[group] = []
            group_gpa[group].append(grade)
    if grades:
        print("средний результат:", sum(grade for name, grade in grades) / len(grades))
        best_student = max(grades, key=lambda x: x[1])
        print("самый крутой студент:", best_student[0], best_student[1])
    for group in group_gpa:
        print("группа", group, "среднее:", sum(group_gpa[group]) / len(group_gpa[group]))


sol3()
