#קריאה  לרנדום
import random

#סיפרה של ניקוד של המחשב ושל המשתמש
user_wins = 0
computer_wins = 0

#המערך של האפשריות שיכול המחשב לבחור ממנו
options = ["rock", "paper", "scissors"]

#תחילת המשחק אם אפשרות לבחור או לפרוש
while True:
    #הפיכה של התשובה של המשתמש לאותיות קטנות
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    #אם המשתמש בחר לצאת(q)יוצאים מהלולאת וניגמר המשחק
    if user_input == "q":
        break
    #אם המשתמש לא הכני אבן ניי או מספריים או q הלולא תמשיך לרוץ עש שהוא יכניס את התשובה הנכונה
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # אבן - 0 /נייר - 1 /מספריים - 2
    #האפשרויות של המחשב
    computer_pick = options[random_number]
    print(f'Computer picked {computer_pick} .')

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print(f'You won {user_wins} times.')
print(f'The computer won {computer_wins} times.')
print("Goodbye!")








