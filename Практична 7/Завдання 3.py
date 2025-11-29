students = {
    "Анна": 92,
    "Богдан": 85,
    "Віктор": 98,
    "Галина": 79,
    "Дмитро": 90
}

grades = students.values()

total_score = sum(grades)
num_students = len(students)
average_score = total_score / num_students

print(f"Словник студентів: {students}")
print(f"Загальна сума балів: {total_score}")
print(f"Кількість студентів: {num_students}")

print(f"Середній бал: {average_score:.2f}")