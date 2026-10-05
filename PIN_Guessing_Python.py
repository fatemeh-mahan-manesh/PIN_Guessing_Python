import random

selection = int(input("""Choose an option please :
1. You guess computer's 4-digit PIN
2. Computer guesses your 4-digit PIN
Enter 1 or 2 : """))

if selection == 1:
    temp = 1
    PIN = random.randint(1000, 9999)
    guess = int(input("Please enter your guess : "))
    while guess != PIN:
        if guess < PIN:
            guess = int(input("The PIN is more than your guess. Guess again. : "))
        elif guess > PIN:
            guess = int(input("The PIN is less than your guess. Guess again. : "))
        temp += 1
    if guess == PIN:
        print(f"correct! You guessed the PIN in {temp} attempt(s).")

elif selection == 2:
    lower_bound = 1000
    upper_bound = 9999
    temp = 1
    guess = random.randint(lower_bound, upper_bound)
    print(f"My guess is : {guess}")
    TorF = input("Is it True? Yes or No? : ")
    while TorF == "No":
        command = input("Should I go Upper or Lower? : ")
        if command == "Upper":
            lower_bound = guess + 1
        elif command == "Lower":
            upper_bound = guess - 1
        else:
            print("Invalid command. Please say Upper or Lower.")
            continue

        if lower_bound > upper_bound:
            print("Something is wrong! Your hints are inconsistent.")
            break

        guess = (lower_bound + upper_bound) // 2
        temp += 1
        print(f"My guess is : {guess}")
        TorF = input("Is it True? Yes or No? : ")

    if TorF == "Yes":
        print(f"Yay! I guessed the PIN in {temp} attempt(s).")
