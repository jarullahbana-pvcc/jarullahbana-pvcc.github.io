import random

# Tuple of possible answers
magic_8_ball_responses = (
    "Yes, definitely!",
    "Absolutely not!",
    "I don't think so.",
    "Maybe, ask again later.",
    "My sources say no.",
    "Yes, but not right now.",
    "It is certain.",
    "Cannot predict now.",
    "My answer is unclear.",
    "Ask again, the answer will change."
)

def ask_question():
    print("Welcome to the Magic 8 Ball program by Farmandeh Bana!")
    question = input("Ask the Magic 8 Ball a YES or NO question: ")
    if question.strip()[-1] == '?':
        print("The Magic 8 Ball says: " + random.choice(magic_8_ball_responses))
    else:
        print("Please ask a YES or NO question ending with a '?'.")

# Running the program
ask_question()
