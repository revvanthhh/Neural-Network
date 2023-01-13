marks = float(input("Enter the marks to get the grade: "))
if marks > 100 or marks < 0:
    print("Incorrect input")
elif marks >= 90:
    grade = "A"
elif marks >= 80 and marks <=89:
    grade = "B"    
elif marks >= 70 and marks <=79:
    grade = "C"
elif marks >= 60 and marks <=69:
    grade = "D"
elif marks >= 0 and marks <=60:
    grade = "F"  

if grade is not None:
    print("Grade is: "+grade) 
        


