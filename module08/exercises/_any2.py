# recruit_developer.py
def schedule_interview(applicant):
    print(f"Scheduled interview with {applicant['name']}")

applicants = [
    {
        "name": "Devon Smith",
        "programming_languages": ["c++", "ada"],
        "years_of_experience": 1,
        "has_degree": False,
        "email_address": "devon@email.com",
    },
    {
        "name": "Susan Jones",
        "programming_languages": ["python", "javascript"],
        "years_of_experience": 2,
        "has_degree": False,
        "email_address": "susan@email.com",
    },
    {
        "name": "Sam Hughes",
        "programming_languages": ["java"],
        "years_of_experience": 4,
        "has_degree": True,
        "email_address": "sam@email.com",
    },
]
# any: each candidate only needed to meet at least one criterion.
# all: candidate needs to fit all of the reqs


for applicant in applicants:
    knows_python = "python" in applicant["programming_languages"]
    experienced_dev = applicant["years_of_experience"] >= 5

    credentials = (
        knows_python,
        experienced_dev,
        applicant["has_degree"],
    )
    if knows_python or experienced_dev or applicant["has_degree"]:
        schedule_interview(applicant)
    # if any(credentials):
    #     schedule_interview(applicant)
