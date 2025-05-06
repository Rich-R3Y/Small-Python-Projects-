import random, art, game_data
print(art.logo)

def higher(a, b):
    if a > b:
        return "a"
    else:
        return "b"

def valid_answer(second_answer):
    incorrect = True
    while incorrect:
        second_answer = input("You have to pick either 'a' or 'b' as your answer.").lower()
        if second_answer == 'a' or second_answer == 'b':
            incorrect = False
    return second_answer

def same_or_not(a, b):
    while a == b:
        b = random.choice(game_data.data)
    return b

first_option = random.choice(game_data.data)
followers_a = first_option["follower_count"]
score = 0
not_game_over = True
while not_game_over:
    print(f'Your current score is: {score}')
    print(f'Compare A: {first_option["name"]}, {first_option["description"]}, from {first_option["country"]}.')
    print(art.vs)
    second_option = random.choice(game_data.data)
    same_or_not(first_option, second_option)
    print(f'Against B: {second_option["name"]}, {second_option["description"]}, from {second_option["country"]}.')
    followers_b = second_option["follower_count"]
    answer = higher(followers_a, followers_b)
    print(answer)
    guess = input('''Who has more followers on Instagram? "A" or "B" ''').lower()
    if guess != 'a' and guess != 'b':
        guess = valid_answer(guess)
    if guess != answer:
        not_game_over = False
    else:
        score += 1
        first_option = second_option
        followers_a = followers_b
