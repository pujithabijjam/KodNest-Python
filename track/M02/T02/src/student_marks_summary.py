student_count = int(input())
total_marks = 0
passed_count = 0
faild_count = 0
for i in range(1,student_count+1):
    mark = int(input())
    total_marks += mark
    if mark >= 40:
        passed_count += 1
    else:
        failed_count += 1
print(f"Total marks: {total_marks}")
print(f"Passed Students: {passed_count}")
print(f"Failed Students: {faild_count}")

if failed_count == 0:
    print("Batch Result: All Passed")
else:
    print("Batch Result: Needs Improvement")
