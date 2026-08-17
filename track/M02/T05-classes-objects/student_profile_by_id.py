class Student:
    def __init__(self,student_id,name,course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return(f"{self.student_id} - {self.name} - {self.course}")

class PlacementManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student_by_id(self, student_id):
            for student in self.students:
                if student.student_id == student_id:
                    return student
            return None

manager = PlacementManager()
n = int(input())

for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()

    student = Student(student_id, name, course)
    manager.add_student(student)

required_id = int(input())
result = manager.find_student_by_id(required_id)

if result:
    print(result)
else:
    print(f"Student profile with ID {required_id} not found")