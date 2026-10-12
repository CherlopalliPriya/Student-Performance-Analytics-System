
import pandas as pd
import numpy as np

# Create student dataset
data = {
    "Student_ID": [501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515],
    "Name": [
        "Priya", "Priyanka", "Jyothika", "Vaishnavi",
        "Jaya Sree", "Prathibha", "Thejaswini", "Rajeswari",
        "Monika", "Monisha", "Arifa", "Zaara",
        "Shalini", "Nandhini", "Janu"
    ],
    "Python": [85,72,95,60,88,98,78,95,78,95,65,86,45,87,33],
    "SQL": [78,80,92,65,85,88,96,98,89,87,86,97,76,54,35],
    "HTML": [90,75,88,58,91,88,97,95,83,78,73,55,73,81,39],
    "CSS": [88,70,94,62,89,99,87,78,97,95,76,87,58,97,76],
    "JavaScript": [82,78,96,70,90,86,88,79,77,98,75,64,34,54,45],
    "Attendance": [92,85,98,75,94,88,96,85,74,86,56,77,83,71,59]
}

# Create and save a proper CSV file
pd.DataFrame(data).to_csv("student_data.csv", index=False)

# Read the CSV file
df = pd.read_csv("student_data.csv")

print("\nSTUDENT PERFORMANCE ANALYTICS SYSTEM")
print("\nSTUDENT DATA")
print(df.to_string(index=False))

subjects = ["Python", "SQL", "HTML", "CSS", "JavaScript"]

# Calculate total and average
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = np.round(df[subjects].mean(axis=1), 2)

# Calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    elif avg >= 40:
        return "E"
    else:
        return "F"

df["Grade"] = df["Average"].apply(calculate_grade)

# Calculate pass or fail
df["Result"] = df[subjects].min(axis=1).apply(
    lambda mark: "Pass" if mark >= 35 else "Fail"
)

# Display performance report
print("\nSTUDENT PERFORMANCE REPORT")
print(df[[
    "Student_ID", "Name", "Total",
    "Average", "Grade", "Result"
]].to_string(index=False))

# Class analysis
print("\nCLASS ANALYSIS")
print("Class Average:", round(df["Average"].mean(), 2))
print("Highest Average:", df["Average"].max())
print("Lowest Average:", df["Average"].min())
print("Students Passed:", (df["Result"] == "Pass").sum())
print("Students Failed:", (df["Result"] == "Fail").sum())

# Save final report
df.to_csv("student_performance.csv", index=False)

print("\nCSV files created successfully!")