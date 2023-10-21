import random

questions = [
    "1. Who created Python?",
    "2. When was Python created?",
    "3. Which of these Python data types is indexed and immutable?",
    "4. Which of these Programming Languages was first released?",
    "5. What for an animal a Python is?"
]

options = [
    "a) James Gosling\nb) Brandon Eich\nc) Guido van Rossum\nd) Bjarne Stroustrup",
    "a) 1986\nb) 1991\nc) 1996\nd) 2001",
    "a) List\nb) Dictionary\nc) Set\nd) Tuple",
    "a) JavaScript\nb) Python\nc) Java\nd) C#",
    "a) Spider\nb) Tiger\nc) Snake\nd) Fox"
]

answers = ["c", "b", "d", "b", "c"]

while True:

    print("\nLet's play a Python Quiz! There will be 5 questions, for each only one option is correct.\n")

    user_answers = []

    for question, option in zip(questions, options):
        print(f"\n{question}\n")
        print(option)

        letters = "abcd"
        answer = " "

        while answer not in letters:
            answer = input("\nAnswer: ").strip().lower()
            if answer not in letters:
                print("\n* Please type in either 'a', 'b', 'c' or 'd'.")

        user_answers.append(answer)

    score = 0
    for user_answer, answer in zip(user_answers, answers):
        if user_answer == answer:
            score += 20

    print(f"\nYour Answers: {user_answers}")
    print(f"Correct Answers: {answers}")

    if score >= 80:
        message = "Congratulations! :)"
    elif score >= 60:
        message = "Good job. :)"
    else:
        message = "Don't worry, at least you've learned something new. :)"

    print(f"\nYou scored {score}%. {message}\n")

    replay = input("Wanna play again? ([Y]es/[N]o): ").strip().lower()
    if replay != "y" and replay != "yes":
        break

print("\nThanks for playing! :)")

