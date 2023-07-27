import random
def guessing_game():
    print("Please type a number between 1 and 10")
    num_guess = input ("Guess: ")
    print(num_guess)
    # int_num_guess = int(num_guess)
    random_num = random.randint(1,10)
    # print(random_num)
    if num_guess.isnumeric() == False:
        print("Error value!")
    else:
        int_num_guess = int(num_guess)
        while 1<=int_num_guess <=10:
            if int_num_guess > random_num:
                print("This number is higher!")
                num_guess = input ("Guess: ")
                print(num_guess)
                int_num_guess = int(num_guess)
                # random_num = random.randint(1, 10)
                # print(random_num)
            elif int_num_guess < random_num:
                print("This number is lower!")
                num_guess = input ("Guess: ")
                print(num_guess)
                int_num_guess = int(num_guess)
                # random_num = random.randint(1, 10)
                # print(random_num)
            else:
                print("The number is correct!!")
                break



guessing_game()
