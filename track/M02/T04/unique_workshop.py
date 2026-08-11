n = int(input())

registrations = set()

for i in range(n):
    student_id = input()
    registrations.add(student_id)

unique_count = len(registrations)
duplicate_count = n - unique_count

print("Unique registrations:", unique_count)
print("Duplicate entries:", duplicate_count)

search_id = input()

if search_id in registrations:
    print("Registered")
else:
    print("Not Registered")