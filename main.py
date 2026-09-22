from analyzer import analyze_skills


print("===================================")
print("       AI RESUME ANALYZER")
print("===================================")

print("\nEnter your resume details:")

resume = input("Resume text: ")

print("\nEnter the job description:")

job_description = input("Job description: ")

required_skills, matching_skills, missing_skills = analyze_skills(
    resume,
    job_description
)
if required_skills:

    match_percentage = (
        len(matching_skills) / len(required_skills)
    ) * 100

else:

    match_percentage = 0

print("\n===================================")
print("          ANALYSIS RESULT")
print("===================================")
print(f"\nMatch Percentage: {match_percentage:.2f}%")

print("\nMatching Skills:")

if matching_skills:
    for skill in matching_skills:
        print("✓", skill)
else:
    print("No matching skills found.")

print("\nMissing Skills:")

if missing_skills:
    for skill in missing_skills:
        print("✗", skill)
else:
    print("No missing skills found.")

print("\nAnalysis completed!")

print("\n===================================")
print("       IMPROVEMENT SUGGESTIONS")
print("===================================")

if missing_skills:

    print("\nConsider improving these skills:")

    for skill in missing_skills:
        print("•", skill)

    print("\nTip: Add relevant projects or experience")
    print("that demonstrate these skills.")

else:

    print("\nYour resume covers all detected job skills!")
    print("Continue highlighting your relevant experience.")