lives = 10
def hard_mode(vidas):
    return vidas - 5
num_to_guess = random.randint(1, 100)
difficulty = input("Welcome to guessing number, please select the difficulty\n'Easy' 'Hard' ").lower()
not_game_over = True
guess_attempts = []
if difficulty == 'hard':
    lives = hard_mode(lives)
    print("You have selected 'hard mode'\nYou have 5 attempts.")
    print(f'Remaining lives: {lives}')
    print("I am thinking of a number between 1 and 100 ")
else:
    lives = 10
    print("You have selected 'easy mode'\nYou have 10 attempts.")
    print(f'Remaining lives: {lives}')
    print("I am thinking of a number between 1 and 100 ")
while not_game_over:
    if lives == 0:
        print("You lose!")
        not_game_over = False
    else:
        guess = int(input("Take a guess "))
        if guess in guess_attempts:
            print("you\'ve already guessed that number, pick another one!")
        elif guess == num_to_guess:
            print('You got the right number, You\'ve won! ')
            not_game_over = False
        elif guess != num_to_guess and guess > num_to_guess:
            print("Too high")
            guess_attempts.append(guess)
            lives -= 1
            print(lives)
        elif guess != num_to_guess and guess < num_to_guess:
            print("Too low")
            guess_attempts.append(guess)
            lives -= 1
            print(lives)
