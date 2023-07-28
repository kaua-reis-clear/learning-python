from itertools import groupby

students = [
    {'name': 'Kauã', 'grade': 'A'},
    {'name': 'Cintia', 'grade': 'B'},
    {'name': 'André', 'grade': 'A'},
    {'name': 'Vitória', 'grade': 'C'},
    {'name': 'João Bosco', 'grade': 'D'},
    {'name': 'Miminha', 'grade': 'A'},
    {'name': 'Aline', 'grade': 'B'},
    {'name': 'Felipe', 'grade': 'A'},
    {'name': 'Mateus', 'grade': 'C'},
]


def order(student):
    return student['grade']


grouped_students = sorted(students, key=order)
groups = groupby(grouped_students, key=order)

for key, group in groups:
    print(key)
    for student in group:
        print(student)