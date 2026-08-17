from student_profile_by_id import required_id
class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

n = int(input())
students = []
for i in range(n):
    student_id = int(input())
    name = input()
    course = input()
    student = StudentProfile(student_id,name,course)
    students.append(student)

required_course = input()
found = False
for student in students:
    if student.course.lower() == required_course.lower():
        print(student.student_id,"-",student.name,"-",student.course)
        found = True
if not found:
    print("No students found for course:", required_course)
    