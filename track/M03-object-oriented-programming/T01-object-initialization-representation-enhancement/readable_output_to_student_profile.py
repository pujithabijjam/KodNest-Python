class StudentProfile:
    def __init__(self,student_id, name, course, experience, skills):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills

    def __str__(self):
        return self.student_id
        return self.name
        return self.course
        return self.experience
        return self.skills

student_id = int(input())
name = input()
course = input()
experience = int(input())
skills = input().split(",")

student = StudentProfile(student_id,name,course,experience,skills)
print("STUDENT PROFILE")
print(f"Student ID: {student_id}")
print(f"Name: {name}")
print(f"Course: {course}")
print(f"Experience in years: {experience}")
print(f"Skills: {', '.join(skills)}")