recu_students = []

with open('../studants.txt') as grades_file:
    for line in grades_file:
        student_grade = line
        student_grade = student_grade.split(" ")
        print(student_grade)
        if int(student_grade[1]) < 6:
          recu_students.append(student_grade[0])

print(recu_students)