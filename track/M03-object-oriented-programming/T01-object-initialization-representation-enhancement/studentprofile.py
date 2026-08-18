class StudentProfile:
    def __init__(self, name, id, course, email, skills):
        self.student_name = name
        self.student_id = id
        self.student_course = course
        self.student_email = email
        self.student_skills = skills
st1 = StudentProfile("pujitha", 97, "DS", "pujitha123@gmail.com", ["Python", "Machine Learning"])
print(st1.student_course)
