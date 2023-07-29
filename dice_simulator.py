import random
print("""Welcome the the dice game. Please input the number of the time you would like to roll your dice, 
        then press enter. If you want to exit the game, please input 'exit'.
      """)
user_input = (input("How many dice would you like to roll? "))
while user_input.isnumeric() == True:
    num_user_input = int(user_input)
    start = 1
    end = 100

    result = random.sample(range(start, end + 1), num_user_input)
    print(*result, sep=", ")
    total = sum(result)
    print(f"The total of the numbers is {total}")
    user_input = (input("How many dice would you like to roll? "))
else:
    print("Thank you for playing with us!")
    quit()

