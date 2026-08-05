marks = int(input())
attendence = int(input())
project_completion_status = input()
if marks >= 60 and attendence >= 75:
    if project_completion_status == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")