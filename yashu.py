# 1. Variables and Data Types
project_name = "Python Demo"
version_number = 3.12
is_active = True
developer_tools = ["VS Code", "PyCharm", "Git"]

print(f"--- Welcome to the {project_name} (v{version_number}) ---")

# 2. Functions and Type Hinting
def calculate_experience(years: int) -> str:
    """Determines seniority level based on years of experience."""
    if years < 2:
        return "Junior Developer"
    elif 2 <= years <= 5:
        return "Mid-level Developer"
    else:
        return "Senior Developer"

# 3. Loops and Lists
print("\nRecommended Ecosystem Tools:")
for index, tool in enumerate(developer_tools, start=1):
    print(f"{index}. {tool}")

# 4. Dictionary and Data Extraction
user_profile = {
    "name": "Alex",
    "experience_years": 4,
    "skills": ["Python", "SQL", "Cloud"]
}

# Process the data
user_profile["role"] = calculate_experience(user_profile["experience_years"])

print("\n--- User Profile Summary ---")
print(f"Name: {user_profile['name']}")
print(f"Assigned Role: {user_profile['role']}")
print(f"Core Skills: {', '.join(user_profile['skills'])}")

# 5. Error Handling (Try-Except)
print("\nTesting Safe Division Mechanism:")
try:
    calculated_ratio = 100 / user_profile["experience_years"]
    print(f"Success! Experience Ratio: {calculated_ratio:.2f}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero experience.")
except KeyError as error:
    print(f"Error: Missing profile key {error}")
finally:
    print("Execution finalized successfully.")
