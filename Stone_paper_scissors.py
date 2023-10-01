import random

print("Game Begins!!\nThe only inputs taken are 0,1,2\n 0 For Rock. \n 1 For Paper. \n 2 For Scissors. \n Good Luck!!")
user_point = 0
system_point = 0
while True:
    user_choice = int(input('Enter a number '))
    system_generate = (random.randrange(3))
    print(f"Lets say {system_generate}")
    if user_choice == 0:
        if system_generate == 0:
            print(f"That was a Tie! You got {user_point}, I got {system_point}")
        elif system_generate == 1:
            system_point += 1
            print(f"Hahha Gotcha. You got {user_point}, I got {system_point}")
        else:
            user_point += 1
            print(f"Oops. you got luck You got {user_point}, I got {system_point}")
    if user_choice == 1:
        if system_generate == 0:
            user_point += 1
            print(f"Oops. you got luck You got {user_point}, I got {system_point}")
        elif system_generate == 1:
            print(f"That was a Tie! You got {user_point}, I got {system_point}")
        else:
            system_point += 1
            print(f"Hahha Gotcha. You got {user_point}, I got {system_point}")
    if user_choice == 2:
        if system_generate == 0:
            system_point += 1
            print(f"Hahha Gotcha. You got {user_point}, I got {system_point}")
        elif system_generate == 1:
            user_point += 1
            print(f"Oops. you got luck You got {user_point}, I got {system_point}")
        else:
            print(f"That was a Tie! You got {user_point}, I got {system_point}")
    if user_point == 5 or system_point == 5:
        print("Game over!")
        if user_point > system_point:
            print("You win!")
        elif user_point < system_point:
            print("I win!")
        else:
            print("It's a tie!")
        break
