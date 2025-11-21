score = float(input("Enter a score: "))

grade = ""

if score >=90 and score <= 100:
    grade = "A" 
elif score >= 80 and score <=90:
    grade = "B"
elif score >= 70 and score <=80:
    grade = "C"
elif score >= 60 and score <=70:
    grade = "D"
elif score >= 50 and score <=60:
    grade = "E"
elif score >= 0 and score <=50:
    grade = "F"
else:
    grade = ""

match grade:
    case "A" | "E":
        print("You got an", grade , "for the test")
    case "B" | "C" | "D" | "F":
        print("You got a" , grade , "for the test")
    case "":
        print("")