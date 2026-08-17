class JobDescription:
    def __init__(self, job_id, company, role, location="Remote", is_active=True):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.is_active = is_active
    
    def __str__(self):
        status = "Active" if self.is_active else "Closed"
        return(
            f"Job ID: {self.job_id}\n"
            f"Company: {self.company}\n"
            f"Role: {self.role}\n"
            f"Location: {self.location}\n"
            f"Status: {status}"
        )

job_one = JobDescription(501, "TechNova", "Python Developer", "Bengaluru", True)
job_two = JobDescription(502, "CodeWorker", "Java Developer", "Hyderabad", True)
job_three = JobDescription(503, "CloudNine", "Support Engineer", "Remote", False)

job_descriptions = [job_one, job_two, job_three]

for i in job_descriptions:
    print(i)