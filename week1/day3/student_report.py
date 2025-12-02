import csv

with open("student_report.csv","r") as f:
    reader = csv.DictReader(f)
    students = list(reader)

# Calculate averages
for s in students:
    marks = [float(s["math"]), float(s["science"]), float(s["english"])]
    avg = sum(marks) / len(marks)
    print(s["name"], "Average:", avg)

# Class summary
all_marks = []
for s in students:
    all_marks.extend([
        float(s["math"]),
        float(s["science"]),
        float(s["english"])
    ])

print("Class Average:", sum(all_marks) / len(all_marks))
print("Highest:", max(all_marks))
print("Lowest:", min(all_marks))
