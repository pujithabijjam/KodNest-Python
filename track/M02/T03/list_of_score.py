n = int(input())
scores = []
for i in range(n):
    score = int(input())
    scores.append(score)
search_score = int(input())
highest = max(scores)
lowest = min(scores)
total = sum(scores)
if search_score in scores:
    result = "Found"
else:
    result = "Not Found"
print(f"Result: {result}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Search Result: {result}")