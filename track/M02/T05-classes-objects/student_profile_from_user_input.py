class StudentProfile:
    def __init__(self,student_id,name,course,score,is_placed=False):
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
            "STUDENT PROFILE\n"
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score}\n"
            f"Placement Status: {placement_status}"
        )
    
student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
placement_input = input().strip()

is_placed = placement_input.upper() == "YES"

student = StudentProfile(student_id,name,course,score,is_placed)

print(student)