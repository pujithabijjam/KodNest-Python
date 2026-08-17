class CandidateProfile:
    def __init__(self, name, email, score):
        self.name = name
        self.email = email
        self.score = score

    def get_email(self):
        self.get_email = self.email

    def get_score(self):
        self.get_score = self.score

name = input()
email = input()
score = float(input())

candidate = CandidateProfile(name, email, score)

print("CANDIDATE PROFILE")
print(f"Name: {name}")
print(f"Email: {email}")
print(f"Score: {score}")
        