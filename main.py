import pandas as pd
print ("="*50)
print ("student report analyzer")
print ("="*50)
data = {

"Name": ["Aarav", "Priya", "Rohan", "Sneha", "Kiran",

"Meera", "Arjun", "Divya", "Rahul", "Ananya",

"Vikram", "Pooja", "Siddharth", "Riya", "Aditya",

"Nisha", "Kabir", "Tanya", "Ishaan", "Simran"],

"Math": [87,45,72,91,38,65,88,54,76,93,42,79,85,61,70,55,88,47,82,95],

"Science": [78,52,68,88,41,71,82,49,80,89,39,74,90,58,65,60,85,50,77,91],

"English": [82,61,74,85,55,68,79,62,71,87,48,80,83,70,73,63,76,58,69,92],

"History": [75,58,65,80,42,72,77,55,68,84,44,76,88,63,67,59,80,52,72,88],

"CS": [91,48,80,94,35,63,95,57,85,96,40,82,92,67,78,61,90,44,88,97]

}
df = pd.DataFrame(data)
subjects = ["Math", "Science", "English", "History", "CS"]
df["Total"] = df[subjects].sum(axis=1)
df["average"] = df["Total"]/5
def grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
df["Grade"] = df["average"].apply(grade)
df["passed_all"] = df[subjects].min(axis=1) >= 40
df["status"] = df["passed_all"].map({True: "Pass", False: "Fail"})
print("full class report:")
print(df[["Name"]+subjects+["Total", "average", "Grade", "status"]].to_string(index=False))
passed=df[df["passed_all"]]
print("\nStudents who passed all subjects:", len(passed),"/", len(df))
print("grade distribution:")
for j, i in df["Grade"].value_counts().items():
    print(f"Grade {j}: {i} students")