from os import listdir

# Task 1
files = listdir("data/")

print(f"Content of data folder: {files}")

# Task 2

math_grades = []
physics_grades = []
statistics_grades = []
student_names = []

for file in files:
    with open(f"data/{file}", 'r') as f:
        if file == "student_names.txt":
            student_names = [line.strip() for line in f]
        elif file == "math.txt":
            math_grades = [int(line) for line in f]
        elif file == "physics.txt":
            physics_grades = [int(line) for line in f]
        elif file == "statistics.txt":
            statistics_grades = [int(line) for line in f]
        else:
            print(f"Unknown file: {file}")
        
grades = {student_names[i]: {"math": math_grades[i], "physics": physics_grades[i], "statistics": statistics_grades[i]} for i in range(len(student_names))}

print("\nDictionary: ")
for key, val in grades.items():
    print(f"\tstudent: {key}, \tgrades: {[i for i in val.values()]}")

# Task 3

# average grade
print("\nAverage grades:")
for key, val in grades.items():
    avg = sum([i for i in val.values()])/len(val)
    grades[key]["avg"] = avg
    print(f"\tstudent: {key}, \taverage: { avg:.2f}")

# top 3 by avg
top3_by_avg = sorted(grades.items(), key=lambda k_v: k_v[1]['avg'], reverse=True)[:3]
print("\nTop 3 by avg:")

for i in range(len(top3_by_avg)):
    print(f"\tstudent: {top3_by_avg[i][0]}, \taverage: { top3_by_avg[i][1]["avg"]:.2f}")
    
# Student number, avg by subject, min/max by subject
stud_number = len(grades.keys())
stats_by_subject = {
    "math": {"min": 101, "max": -1, "avg": 0.0},
    "physics": {"min": 101, "max": -1, "avg": 0.0},
    "statistics": {"min": 101, "max": -1, "avg": 0.0}
}

def helper_func(subject, val):
    stats_by_subject[subject]["avg"] += val[subject]

    if val[subject] > stats_by_subject[subject]["max"]:
        stats_by_subject[subject]["max"] = val[subject]
    
    if val[subject] < stats_by_subject[subject]["min"]:
        stats_by_subject[subject]["min"] = val[subject]

for key, val in grades.items():
    helper_func("math", val)
    helper_func("physics", val)
    helper_func("statistics", val)

stats_by_subject["math"]["avg"] = stats_by_subject["math"]["avg"] / stud_number
stats_by_subject["physics"]["avg"] = stats_by_subject["physics"]["avg"] / stud_number
stats_by_subject["statistics"]["avg"] = stats_by_subject["statistics"]["avg"] / stud_number

print("\nStats by subject: ")
for key, val in stats_by_subject.items():
    print(f"\tSubject: {key} \tmin: {val["min"]} \tmax: {val["max"]} \tavg: {val["avg"]}")

# Best student by subject
top_by_subject = []
top_by_subject.append( ["math", sorted(grades.items(), key=lambda k_v: k_v[1]['math'], reverse=True)[0]] )
top_by_subject.append( ["physics", sorted(grades.items(), key=lambda k_v: k_v[1]['physics'], reverse=True)[0]] )
top_by_subject.append( ["statistics", sorted(grades.items(), key=lambda k_v: k_v[1]['statistics'], reverse=True)[0]] )

print("\nHighest grade by subject:")
for i in range(len(top_by_subject)):
    print(f"\tsubject: {top_by_subject[i][0]} |\tstudent: {top_by_subject[i][1][0]}, \tgrade: { top_by_subject[i][1][1][top_by_subject[i][0]]:.2f}")

# Avg grade less than 50
not_pass_number = 0
not_pass_list = []
for key, val in grades.items():
    if val["avg"] < 50:
        not_pass_number += 1
        not_pass_list.append(key)

print("\nAvg less then 50:")
print(f"Number of students: {not_pass_number}")
for stud in not_pass_list:
    print(f"\t{stud}")