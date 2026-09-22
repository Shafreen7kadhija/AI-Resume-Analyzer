import re


def analyze_skills(resume, job_description):

    skills = [
        "java",
        "python",
        "c",
        "c++",
        "javascript",
        "sql",
        "html",
        "css",
        "react",
        "git",
        "data structures",
        "machine learning",
        "flask",
        "spring boot"
    ]

    resume_text = resume.lower()
    job_text = job_description.lower()

    required_skills = []
    matching_skills = []
    missing_skills = []

    for skill in skills:

        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, job_text):

            required_skills.append(skill)

            if re.search(pattern, resume_text):
                matching_skills.append(skill)
            else:
                missing_skills.append(skill)

    return required_skills, matching_skills, missing_skills

