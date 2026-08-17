class StudentProfile:
    def __init__(self,student_id,name,course,score=0.0,is_placed=False):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.is_placed = is_placed

    def __str__(self):
        placement_status = (
            "Placed" if self.is_placed 
            else "Not Placed"
        )

        return(
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score}\n"
            f"Placement Status: {placement_status}"
        )
    
student_one = StudentProfile(101, "Asha", "Python", 85.0, False)
student_two = StudentProfile(102, "Rahul", "Java")

print(student_one)
print(student_two)