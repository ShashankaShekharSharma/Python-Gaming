import random
import time

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question["text"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")
        user_answer = input("Your answer (enter the option number): ")
        return user_answer

    def run_quiz(self):
        # Select 10 random questions from the quiz questions
        random_questions = random.sample(self.questions, 10)

        # Set a timer for 60 seconds
        timeout = time.time() + 60

        # Initialize the start time
        start_time = time.perf_counter()

        # Iterate through the selected questions
        for question in random_questions:

            # Calculate the elapsed time
            elapsed_time = time.perf_counter() - start_time

            # Display the elapsed time
            print(f"Elapsed time: {elapsed_time:.2f} seconds")

            # Check if the time is up
            if time.time() > timeout:
                print("Time's up! Your score is:", self.score)
                break

            user_answer = self.display_question(question)
            correct_answer = str(question["answer"])
            
            if time.time()>timeout:
                self.score += 0
            elif user_answer == 'leave':
                print("Question Skipped")
                self.score += 0
            elif user_answer == correct_answer:
                print("Correct!\n")
                self.score += 4
            else:
                print(f"Wrong! The correct answer is {correct_answer}.\n")
                self.score -= 1

        # Display the score
        if time.time() <= timeout:
            print(f"You scored {self.score} out of {len(random_questions)}.")

# Sample quiz questions
quiz_questions = [
    {
        "text": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": 3,
    },
    {
        "text": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": 1,
    },
    {
        "text": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain"],
        "answer": 3,
    },
    {
        "text":"What is the capital of India?",
        "options":["Delhi","Guwahati","Nagaland","Manipur"],
        "answer":1,
    },
    {
        "text":"When did India get independence?",
        "options":["1989","1947","1969","1500"],
        "answer":2,
    },
    {
        "text":"When did India get independence?",
        "options":["1989","1947","1969","1500"],
        "answer":2,
    },
        {
        "text":"When did India get independence?",
        "options":["1989","1947","1969","1500"],
        "answer":2,
    },
        {
        "text":"When did India get independence?",
        "options":["1989","1947","1969","1500"],
        "answer":2,
    },
        {
        "text":"When did India get independence?",
        "options":["1989","1947","1969","1500"],
        "answer":2,
    },
        {
        "text":"When did India get independence?",
        "options":["1989","1947","1969","1500"],
        "answer":2,
    },
]

# Create a Quiz object and run the quiz
print("Welcome to Quiz Competetion.")
print("Instructions:")
print("For every correct answer you get 4 marks and for every wrong answer you get -1. Type 'leave' if you want to skip the question")
my_quiz = Quiz(quiz_questions)
my_quiz.run_quiz()
