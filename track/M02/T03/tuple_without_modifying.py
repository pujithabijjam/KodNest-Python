course_name = input()
course_week = input()
course_status = input()
course_details = (course_name,course_week,course_status)
updated_week = input()
new_tuple = course_name,updated_week,course_status
course_details = new_tuple
print(course_details)