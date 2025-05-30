import csv
def grade(AverageMarks):
        if AverageMarks >= 90:
            return 'A'
        elif 80 <= AverageMarks < 90:
             return 'B'
        elif 70 <= AverageMarks < 80:

            return 'C'
        elif 60 <= AverageMarks < 70:

            return 'D'
        else:
            return 'F'

students_data = []


def MarksSheet():
    while True:
        name = input("Name of the Student: ")
        RollNumber = input("Roll No.: ")
        PhysicsMarks = int(input("Marks in Physics: "))
        ChemistryMarks = int(input("Marks in Chemistry: "))
        MathematicsMarks = int(input("Marks in Mathematics: "))
        EnglishMarks = int(input("Marks in English: "))

        print(name, RollNumber, PhysicsMarks, ChemistryMarks, MathematicsMarks)

        AverageMarks = round((PhysicsMarks + ChemistryMarks +
                             MathematicsMarks + EnglishMarks) / 4, 2)
        print(
            f"Average Marks of {name} are {AverageMarks} and has scored grade {grade(AverageMarks)}")

        info = {
         "Name": name,
         "Roll no. ": RollNumber,
         "Physics Marks": PhysicsMarks,
         "Chemistry Marks": ChemistryMarks,
         "Mathematics Marks": MathematicsMarks,
         "English Marks": EnglishMarks,
         "Average Marks": AverageMarks,
         "Grade": grade(round(AverageMarks, 2))
         }

        students_data.append(info)
        print("\n------ Student Record Saved ------")
        print("Name:", name)
        print("Roll No.:", RollNumber)
        print("Average Marks:", round(AverageMarks, 2))
        print(f"{name} has scored grade '{grade(AverageMarks)}'.")

        more = input("\nDo you want to add another student? (y/n): ")
        if more.lower() == 'n':
            break
        save_to_csv(students_data)



def save_to_csv(data, filename="student_marks.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Roll no. ", "Physics Marks",
                                "Chemistry Marks", "Mathematics Marks", "English Marks", "Average Marks", "Grade"])
        writer.writeheader()
        writer.writerows(data)


save_to_csv(students_data)
MarksSheet()

print("---------------------Here is the final report---------------------")
print("{:<20} {:<20} {:<20} {:<20}".format("Name", "Roll no. ", "Average Marks", "Grade"))

for info in students_data:
     print("{:<20} {:<20} {:<20} {:<20}".format(
         info["Name"], info["Roll no. "], info["Average Marks"], info["Grade"]))


highest_avg = max(info["Average Marks"] for info in students_data)
toppers = [info for info in students_data if info["Average Marks"] == highest_avg]

print("\n🏆 TOPPER(S) OF THE CLASS")
print("-" * 80)

for topper in toppers:
        print(f"{topper['Name']} (Roll No: {topper['Roll no. ']}) with Average Marks: {topper['Average Marks']} and Grade: {topper['Grade']}")
        print("\n✅ All data has been saved to 'student_marks.csv'")
import os
print("\nCSV file saved at:", os.path.abspath("student_marks.csv"))
