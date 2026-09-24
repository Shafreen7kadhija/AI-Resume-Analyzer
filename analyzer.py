import re

def skill_exists(text, skill):

    if skill == "c++":

        return bool(re.search(r"(?<!\w)c\+\+(?!\w)", text))

    if skill == "c":

        return bool(re.search(r"(?<!\w)c(?!\w|\+\+)", text))

    if skill == "javascript":

        return bool(
            re.search(r"(?<!\w)(javascript|js)(?!\w)", text)
        )

    if skill == "data structures":

        return bool(
            re.search(
                r"(?<!\w)(data structures|dsa)(?!\w)",
                text
            )
        )

    pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

    return bool(re.search(pattern, text))

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

        if skill_exists(job_text, skill):

            required_skills.append(skill)

            if skill_exists(resume_text, skill):

                matching_skills.append(skill)

            else:

                missing_skills.append(skill)

    return required_skills, matching_skills, missing_skills