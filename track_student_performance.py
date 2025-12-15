class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks) / len(self.marks)

students = [
    Student("John", [85, 78, 92]),
    Student("Alice", [88, 79, 95]),
    Student("Bob", [70, 75, 80])
]

top_student = ""
highest_avg = 0
averages = {}

for s in students:
    avg = round(s.average(), 2)
    averages[s.name] = avg

    if avg > highest_avg:
        highest_avg = avg
        top_student = s.name

print("Average Marks:", averages)
print("Top Performer:", top_student)
