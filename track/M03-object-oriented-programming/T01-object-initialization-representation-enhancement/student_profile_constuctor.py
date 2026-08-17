class StudentProfile:
    def __init__(self, student_id, name, course, experience, skills):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills

student_id = int(input())
name = input().strip()
course = input().strip()
experience = int(input())
skills = input().replace(" ",", ")

print(f"Student ID: {student_id}")
print(f"Name: {name}")
print(f"Course: {course}")
print(f"Experience in years: {experience}")
print(f"Skills: {skills}")