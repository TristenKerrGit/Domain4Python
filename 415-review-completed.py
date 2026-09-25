"""It tells the players what position they are in and the life they are in the game"""


game_state = True
game_lives = 1
while game_lives <= 3:
    for i in range(1,11):
        print("You have reached position", i, "in game life", game_lives)
    if game_state == True:
        game_lives +=1
print("Thank you for playing.")

print(__doc__)