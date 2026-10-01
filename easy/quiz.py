questions = [
    {
        "question": "What is the capital of france?",
        "options":["A. London","B. Paris","C. Rome","D. Madrid"],
        "answer":"B"
    },
    {
        "question": "How many legs does a spider have?",
        "options":["A. Six", "B. Eight", "C. Ten", "D. Twelve"],
        "answer":"C"
    },
    {
        "question": "Which planet do we live on?",
        "options":["A. Mars", "B. Venus", "C. Earth", "D. Jupiter"],
        "answer":"A"
    }
]

score = 0

for item in questions:
    print("\n" + item["question"])
    for option in item["options"]:
        print(option)

    answer = input("Your answer: ").upper()

    if answer == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong answer")

print("Your score:",score,"out of",len(questions))