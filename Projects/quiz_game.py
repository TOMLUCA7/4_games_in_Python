
print("Welcome to my computer quiz!")
#שואל את המשתמש אם הור רוצ הלשחק
playing = input("Do you want to play? ")

#אם המשתמש רושם כול דבר חוץ מה כן הוא לא ממשיך לשחק
#המרת המילה כן לאותיות קטנות שיהיה התאמה בין הצשובות
if playing.lower() != "yes":
    quit()

#אם המשתמש רשם כן הוא מקבל את ההמודע הבא ומתחיל את הניקוד שלו מה 0
print("Okay! Let's play :)")
score = 0

#שאלה ראשונה למשתמש אם ענה נכון הוא מקבל נקודה אם ענה לא נכון מקבל הודע שהוא טעה
#ככה במשך 4 שאלות
#המרת התשובה לאותיות קטנות שיהיה התאמה בין תשובות
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

#התפסת הניקות שהמשתמש קיבל (בתור מחרוזת)
print("You got " + str(score) + " questions correct!")
print("our grade is " + str((score / 4) * 100) + "%.")

