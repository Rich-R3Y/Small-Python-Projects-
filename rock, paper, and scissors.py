import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
possible_outcomes = [rock, paper, scissors]
computer_pick = random.choice(possible_outcomes)
user_pick = input('Pick "rock", "paper" or "scissors"\n')
if user_pick == "rock":
    user_pick = rock
    hand_power = 0
elif user_pick == "paper":
    user_pick = paper
    hand_power = 1
else:
    user_pick = scissors
    hand_power = 2
if computer_pick == user_pick:
    print(f' The computer picked: {computer_pick}\nYou picked: {possible_outcomes[hand_power]}\nIt\'s a tie!')
elif computer_pick == rock and user_pick == scissors:
    print(f'The computer picked: {computer_pick}\nYou picked: {possible_outcomes[hand_power]}\nThe computer wins!')
elif computer_pick == paper and user_pick == rock:
    print(f'The computer picked: {computer_pick}\nYou picked: {possible_outcomes[hand_power]}\nThe computer wins!')
elif computer_pick == scissors and user_pick == paper:
    print(f'The computer picked: {computer_pick}\nYou picked: {possible_outcomes[hand_power]}\nThe computer wins!')
else:
    print(f'The computer picked: {computer_pick}\nYou picked: {possible_outcomes[hand_power]}\nYou win!')
