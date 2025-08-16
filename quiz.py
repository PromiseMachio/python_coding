def run_quiz():
    score = 0
    questions = [
        {
            "question": "Where did you hear the Rf Economical branch?",
            "options": ["A) Social media", "B) Friends", "C) Web surfing", "D) TV adverts"],
            "answer": "A"
        },
        {
            "question": "Where is the Rf E branch HQ located?",
            "options": ["A) S America, Mexico", "B) Africa, Kenya", "C) N America, Washington", "D) Europe, Spain"],
            "answer": "B"
        },
        {
            "question": "Which of these is NOT practiced by the Rf E branch in societal development and art creation according to the 1997 documentation?",
            "options": ["A) Schools construction", "B) Hospital and church support", "C) Refugee migration assistance", "D) Politicians' campaign forums"],
            "answer": "A"
        } ]
   

    print("Welcome to the Rf E branch test on partnership program.\n")

    # Display questions and get user input
    for index, q in enumerate(questions, 1):
        print(f"Question {index}: {q['question']}")
        for option in q["options"]:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"You got {score} out of {len(questions)} correct!")

# Run the quiz
run_quiz()
