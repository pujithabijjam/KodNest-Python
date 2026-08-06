limit = int(input())
number = 1
total = 0
while number <= limit:
    if number % 2 == 0:
        total += number
    number += 1
print(f"Even Sum: {total}")