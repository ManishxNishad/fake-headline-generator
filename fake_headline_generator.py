import random


subjects = [

    "Maths",

    "Physics",

    "Chemistry",

    "Python",

    "C Programming",

    "Data Science",

    "Artificial Intelligence",

    "Machine Learning",

    "Computer Science",

    "Biology",

    "English",

    "Statistics",

    "Web Development",

    "Data Structures",

    "Operating Systems"

]

exams = [

    "Midterm",

    "Final Exam",

    "Semester Exam",

    "Unit Test",

    "Internal Exam",

    "Practical Exam",

    "Quiz",

    "Mock Test",

    "Class Test",

    "Viva",

    "Entrance Exam",

    "Weekly Test",

    "Assessment",

    "Preliminary Exam",

    "Board Exam"

]

places = [
    "Library",
    "Classroom",
    "Laboratory",
    "Hostel",
    "Canteen",
    "Auditorium",
    "Computer Lab",
    "Study Room",
    "Campus",
    "Garden",
    "Lecture Hall",
    "Seminar Hall",
    "Cafeteria",
    "Reading Room",
    "Study Center"
]


while  True:
    subject = random.choice(subjects)
    exam = random.choice(exams)
    place = random.choice(places)
    
    headline = f"{subject} {exam} Scheduled in {place}"
    print("\n" + headline)
    user_input = input("Press Enter to generate another headline or type 'exit' to quit: ")
    if user_input.lower() == 'exit':
        break

print("Thank you for using the Fake Headline Generator!")
