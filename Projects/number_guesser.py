#קבלת מספרים רנדומלים
import random

#בקשה מהמשתמש להכניס מספר
top_of_range = input("Type a number: ")

#בדיקה שהמשתמש הכניס מספר ולא משהוא אחר
if top_of_range.isdigit():
    #המרה של המספר של המשתמש למספר במקום מחרוזת
    top_of_range = int(top_of_range)
    #בדיקב שהמשתמה הכניס מספר חיובי אם לא הוא מקבל הודע שיכניס  מספר גדול מ0 ויוצא
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:#אם המשתמש לא הכניס מספר הוא התוכנית ישר קוםצת לכאן ונותת הודע מתאימה
    print('Please type a number next time.')
    quit()

#טווח של המסםרים מ 0 עד המספר שהמשתמש הכניס כולל
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    #כמות מספר הנחושים
    guesses += 1
    user_guess = input("Make a guess: ")
    #עושים עוד פעם בידקה שהמשתמה הכניס מספר ולא משהוא אחר
    if user_guess.isdigit():
        #המרה למספר
        user_guess = int(user_guess)
    else:#אחרת תינתן הודע מתאימה והתוכנית תמשיך
        print('Please type a number next time.')
        continue#מחזיר את המשתמש לתחילת הלולאה בשיל שיתן מספר כול עוד לא הוכנס מספר התוכנית לא תמשיך

    #אם המשתמש ניחש נכון אתץ המספר הרנדומלי תינתן הודע מתאימה והתוכנית תפסיק
    if user_guess == random_number:
        print("You got it!")
        break
    #נותן הכוונה למשתמש לאז כיוון הוא צריך לנחש את המספר
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print(f'You got it in {guesses} guesses')