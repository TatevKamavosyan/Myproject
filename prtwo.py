from random import *

goal_num = 0
win_nums = [7,11]
lose_nums = [2,3,12]
goal_nums = [4,5,6,8,9,10]
has_goal = False

rand_num1 = random.randint(1, 6)
rand_num2 = random.randint(1, 6)
rand_res = rand_num1 + rand_num2

print(f"The sum of dice is {rand_num1} + {rand_num2} = {rand_res}")

if rand_res in win_nums:
    print("You won")
elif rand_res in lose_nums:
    print("You lost the game")
elif rand_res in goal_nums:
    goal_num = rand_res
    print(f"Now your goal number is {goal_num}")
    has_goal = True


while has_goal:
    rand_num1 = random.randint(1, 6)
    rand_num2 = random.randint(1, 6)
    rand_res = rand_num1 + rand_num2
    print(f"The sum of dice is {rand_num1} + {rand_num2} = {rand_res}")
    if rand_res == goal_num:
        print("You won")
        has_goal = False
    elif rand_res == 7:
        print("You lost the game")
        has_goal = False