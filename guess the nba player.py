import random


liste = ["Kobe Bryant","Lebron James","Kevin Durant","Michael Jordan","Larry Bird","Stephen Curry",
"Tim Duncan", "Wilt Chamberlain","Bill Russel","Giannis Antetokounmpo","Kareem Abdul-Jabbar","Magic Johnson","Shaq"]

liste = [i.upper() for i in liste]





answer = random.choice(liste)

counter= 5

print("""
***************************
GUESS THE TOP 10 NBA PLAYER

Guess one of the top 10 NBA Players of all time. 
You have 5 guesses!

***************************
""")




while True:
    guess = (input("which top 10 nba player is this?"))
    
    if counter == 0:
       print("the answer is ", answer)
       break
    
    

    for i in range(len(guess)):
        guess = guess.upper()


    if guess == answer:
        print("congrats!")
        break
    elif guess != answer:
        counter -= 1
        print("Wrong! You have {} guesses left" .format(counter))















