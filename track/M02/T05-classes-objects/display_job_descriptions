class JobDescription:
    def __init__(self,job_id,company,role):
        self.job_id = job_id
        self.company = company
        self.role = role

    def __str__(self):
        return(
            f"Job ID: {self.job_id}\n"
            f"Company: {self.company}\n"
            f"Role: {self.role}"
        )

class PlacementManager:
    def __init__(self):
        self.job_descriptions = []

    def add_job_descriptions(self,job):
        self.job_descriptions.append(job)

    def display_job_descriptions(self):
        if len(self.job_descriptions) == 0:
            print("No job descriptions available")
        else:
            print("JOB DESCRIPTIONS")
            for job in self.job_descriptions:
                print(job.job_id, "-",job.company, "-",job.role)

manager = PlacementManager()
n = int(input())

for _ in range(n):
    job_id = int(input())
    company = input().strip()
    role = input().strip()

    job = JobDescription(job_id,company,role)
    manager.add_job_descriptions(job)

manager.display_job_descriptions()