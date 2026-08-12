def student_eligibility(marks, attendence, project_completed):
    if marks >= 60 and attendence >= 75 and project_completed == True:
        return "Eligible"
    else:
        return "Not Eligible"
marks = int(input())
attendence = int(input())
project_completed = input().strip().lower()
result = student_eligibility(marks, attendence, project_completed)
print(result)