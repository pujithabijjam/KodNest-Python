class StudentProfile:
    def __init__(self,student_id,name,course):
        pass

first_id = int(input())
first_name = input().strip()
first_course = input().strip()

second_id = int(input())
second_name = input().strip()
second_course = input().strip()

student1 = StudentProfile(first_id,first_name,first_course)
student2 = StudentProfile(second_id,second_name,second_course)

print("Student 1")
print(f"ID: {first_id}")
print(f"Name: {first_name}")
print(f"Course: {first_course}")

print("Student 2")
print(f"ID: {second_id}")
print(f"Name: {second_name}")
print(f"Course: {second_course}")