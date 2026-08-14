class StudentProfile:
    def __init__(self, student_id, name, course, score, is_placed):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.is_placed = is_placed

    def __str__(self):
        return "Placed" if self.is_placed else "Not Placed"


student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input().strip())
placement_input = input().strip()

# Convert placement_input into a Boolean value
if placement_input == "Yes":
    is_placed = True
elif placement_input == "No":
    is_placed = False
else:
    is_placed = False

# Create StudentProfile object
student = StudentProfile(
    student_id=student_id,
    name=name,
    course=course,
    score=score,
    is_placed=is_placed
)

print("STUDENT PROFILE")
print("Student ID:", student.student_id)
print("Name:", student.name)
print("Course:", student.course)
print("Score:", student.score)
print("Placement Status:", student)