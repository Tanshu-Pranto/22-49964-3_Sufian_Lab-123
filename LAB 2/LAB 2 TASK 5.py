

#convert a student’s marks of a course into a grade    

marks = float(input("Enter marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 85:
    grade = "A"
elif marks >= 80:
    grade = "B+"
elif marks >= 75:
    grade = "B"
elif marks >= 70:
    grade = "C+"
elif marks >= 65:
    grade = "C"
elif marks >= 60:
    grade = "D+"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)