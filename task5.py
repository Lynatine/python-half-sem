import json

def sol5():
    with open("students.json", "r", encoding="utf-8") as file:
        students = json.load(file)
    best_student = max(students, key=lambda x: x["score"])
    for student in students:
        student["passed"] = student["score"] >= 60
    print("лучший студент:", best_student["name"], best_student["score"])
    with open("students_result.json", "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)


sol5()
