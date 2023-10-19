import random

print("\nLet's play Rock, Paper Scissors! The first one to reach 3 points wins.\n")

restart = True
while restart:

    user_score = computer_score = 0

    while user_score < 3 and computer_score < 3:

        options = ("Rock", "Paper", "Scissors")

        valid_user_choice = False
        while not valid_user_choice:
            user_choice = input("\nType in [R]ock, [P]aper or [S]cissors: ").strip().lower()

            match user_choice:
                case "r" | "rock":
                    user_choice = options[0]
                    valid_user_choice = True
                case "p" | "paper":
                    user_choice = options[1]
                    valid_user_choice = True
                case "s" | "scissors":
                    user_choice = options[2]
                    valid_user_choice = True
                case _:
                    print("\n* Please enter either [R], [P] or [S].")

        computer_choice = options[random.randint(0, 2)]

        print(f"\nYou: {user_choice}")
        print(f"Computer: {computer_choice}\n")

        if (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
            user_score += 1

        elif user_choice != computer_choice:
            computer_score += 1

        print(f"Score: {user_score} (You) x {computer_score} (Computer)")

    print("\n*******************")
    print(f"{"You" if user_score == 3 else "The Computer"} won {":)" if user_score == 3 else ":("}")
    print("*******************\n")

    valid_restart = False
    while not valid_restart:
        restart = input("Play again? [Y]es/[N]o: ").strip().lower()

        match restart:
            case "y" | "yes":
                restart = True
                valid_restart = True
                print("\nGreat! Let's start again. The first one to reach 3 points wins.")
            case "n" | "no":
                restart = False
                valid_restart = True
                print("\nThanks for playing, see you soon!")
            case _:
                print("\n* Please enter either [Y] or [N].\n")
