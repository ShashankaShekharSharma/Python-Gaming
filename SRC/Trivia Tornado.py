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
        random_questions = random.sample(self.questions, 10)
        timeout = time.time() + 100
        start_time = time.perf_counter()
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

            if time.time() >= timeout:
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
            print(f"You scored {self.score} out of {len(random_questions)*4}.")


# Easy Questions
easy_questions = [
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
        "text": "What is the capital of India?",
        "options": ["Delhi", "Guwahati", "Nagaland", "Manipur"],
        "answer": 1,
    },
    {
        "text": "When did India get independence?",
        "options": ["1989", "1947", "1969", "1500"],
        "answer": 2,
    },
    {
        "text": "Which mountain range separates Europe and Asia?",
        "options": ["The Rockies", "The Himalayas", "The Alps", "The Andes"],
        "answer": 2,
    },
    {
        "text": "What element is the main ingredient in chocolate?",
        "options": ["Magnesium", "Calcium", "Cocoa", "Zinc"],
        "answer": 3,
    },
    {
        "text": "What city is known as the 'Big Easy'?",
        "options": ["New York City", "Chicago", "New Orleans", "Las Vegas"],
        "answer": 3,
    },
    {
        "text": "What famous painting features a woman with a pearl earring?",
        "options": ["Girl with a Pearl Earring", "The Mona Lisa", "The Birth of Venus", "American Gothic"],
        "answer": 1,
    },
    {
        "text": "Who wrote the classic novel 'Pride and Prejudice'?",
        "options": ["Jane Austen", "Mary Shelley", "Charlotte Brontë", "George Eliot"],
        "answer": 1,
    },
    {
        "text": "What is the national animal of Canada?",
        "options": ["Moose", "Beaver", "Polar bear", "Grizzly bear"],
        "answer": 1,
    },
    {
        "text": "What is the largest planet in our solar system?",
        "options": ["Venus", "Jupiter", "Mars", "Saturn"],
        "answer": 2,
    },
    {
        "text": "Which ocean is the largest on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"],
        "answer": 4,
    },
    {
        "text": "In which year did the Titanic sink?",
        "options": ["1905", "1912", "1920", "1931"],
        "answer": 2,
    },
    {
        "text": "What is the capital of Japan?",
        "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"],
        "answer": 3,
    },
    {
        "text": "Who is known as the 'Father of Computers'?",
        "options": ["Charles Babbage", "Ada Lovelace", "Alan Turing", "Steve Jobs"],
        "answer": 1,
    },
    {
        "text": "Which country is known as the 'Land of the Rising Sun'?",
        "options": ["China", "Japan", "South Korea", "Vietnam"],
        "answer": 2,
    },
    {
        "text": "What is the currency of Australia?",
        "options": ["Dollar", "Euro", "Pound", "Yen"],
        "answer": 1,
    },
    {
        "text": "Which famous scientist developed the theory of relativity?",
        "options": ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Stephen Hawking"],
        "answer": 3,
    },
    {
        "text": "What is the largest mammal in the world?",
        "options": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "answer": 3,
    },
    {
        "text": "In what year did the Berlin Wall fall?",
        "options": ["1985", "1989", "1991", "1995"],
        "answer": 2,
    },
    {
        "text": "Which planet is known as the 'Morning Star' or 'Evening Star'?",
        "options": ["Mercury", "Venus", "Mars", "Jupiter"],
        "answer": 2,
    },
    {
        "text": "What is the largest desert in the world?",
        "options": ["Sahara Desert", "Gobi Desert", "Arabian Desert", "Antarctica"],
        "answer": 4,
    },
    {
        "text": "Who painted the famous 'Starry Night'?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "answer": 1,
    },
    {
        "text": "Which river is the longest in the world?",
        "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
        "answer": 1,
    },
    {
        "text": "What is the capital of Brazil?",
        "options": ["Sao Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
        "answer": 3,
    },
    {
        "text": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "J.K. Rowling", "George Orwell", "Ernest Hemingway"],
        "answer": 1,
    },
    {
        "text": "Which gas makes up the majority of Earth's atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": 3,
    },
    {
        "text": "What is the largest moon in our solar system?",
        "options": ["Titan", "Io", "Ganymede", "Enceladus"],
        "answer": 3,
    },
    {
        "text": "Who is known as the 'Queen of Pop'?",
        "options": ["Beyoncé", "Madonna", "Lady Gaga", "Taylor Swift"],
        "answer": 2,
    },
  ]
medium_questions = [
    {
        "text": "What is the currency of Japan?",
        "options": ["Won", "Yuan", "Ringgit", "Yen"],
        "answer": 3,
    },
    {
        "text": "In which year did the Titanic sink?",
        "options": ["1912", "1905", "1923", "1931"],
        "answer": 1,
    },
    {
        "text": "Who is the author of 'To Kill a Mockingbird'?",
        "options": ["J.K. Rowling", "Harper Lee", "George Orwell", "Mark Twain"],
        "answer": 2,
    },
    {
        "text": "Which gas is most abundant in the Earth's atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Argon"],
        "answer": 3,
    },
    {
        "text": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": 2,
    },
    {
        "text": "Who painted 'Starry Night'?",
        "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
        "answer": 2,
    },
    {
        "text": "What is the capital of Brazil?",
        "options": ["Buenos Aires", "Lima", "Rio de Janeiro", "Brasília"],
        "answer": 4,
    },
    {
        "text": "In which year did the first manned moon landing occur?",
        "options": ["1969", "1972", "1981", "1990"],
        "answer": 1,
    },
    {
        "text": "In which year did World War II end?",
        "options": ["1943", "1945", "1947", "1950"],
        "answer": 2,
    },
    {
        "text": "Who played the character of Tony Stark in the Marvel Cinematic Universe?",
        "options": ["Chris Hemsworth", "Chris Evans", "Robert Downey Jr.", "Mark Ruffalo"],
        "answer": 3,
    },
    {
        "text": "What is the longest river in the world?",
        "options": ["Nile", "Amazon", "Yangtze", "Mississippi"],
        "answer": 2,
    },
    {
        "text": "Which country is known as the 'Land of the Rising Sun'?",
        "options": ["China", "Japan", "South Korea", "Thailand"],
        "answer": 2,
    },
    {
        "text": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Fe", "Cu"],
        "answer": 1,
    },
    {
        "text": "Which famous explorer is credited with circumnavigating the globe?",
        "options": ["Christopher Columbus", "Ferdinand Magellan", "Marco Polo", "Vasco da Gama"],
        "answer": 2,
    },
    {
        "text": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"],
        "answer": 4,
    },
    {
        "text": "In which year did the Berlin Wall fall?",
        "options": ["1985", "1989", "1991", "1995"],
        "answer": 2,
    },
    {
        "text": "Who was the first woman to win a Nobel Prize?",
        "options": ["Marie Curie", "Rosalind Franklin", "Dorothy Crowfoot Hodgkin", "Barbara McClintock"],
        "answer": 1,
    },
    {
        "text": "Which element is a noble gas?",
        "options": ["Oxygen", "Helium", "Nitrogen", "Hydrogen"],
        "answer": 2,
    },
    {
        "text": "What is the capital of South Africa?",
        "options": ["Nairobi", "Cape Town", "Johannesburg", "Pretoria"],
        "answer": 4,
    },
    {
        "text": "Who wrote the 'Harry Potter' book series?",
        "options": ["J.R.R. Tolkien", "J.K. Rowling", "C.S. Lewis", "George R.R. Martin"],
        "answer": 2,
    },
    {
        "text": "What is the largest desert in the world?",
        "options": ["Gobi Desert", "Sahara Desert", "Arabian Desert", "Karakum Desert"],
        "answer": 2,
    },
    {
        "text": "Which famous scientist formulated the laws of motion and universal gravitation?",
        "options": ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Nikola Tesla"],
        "answer": 1,
    },
    {
        "text": "In which year did the United States declare its independence?",
        "options": ["1765", "1776", "1789", "1799"],
        "answer": 2,
    },
    {
        "text": "What is the largest planet in our solar system?",
        "options": ["Mars", "Jupiter", "Saturn", "Neptune"],
        "answer": 2,
    },
    {
        "text": "Who wrote '1984', a dystopian novel depicting a totalitarian regime?",
        "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Margaret Atwood"],
        "answer": 1,
    },
    {
        "text": "Which country is known as the 'Land of the Pharaohs'?",
        "options": ["Greece", "Egypt", "Italy", "Turkey"],
        "answer": 2,
    },
    {
        "text": "What is the largest mammal on land?",
        "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
        "answer": 1,
    },
    {
        "text": "Who painted the famous artwork 'The Persistence of Memory' featuring melting clocks?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Salvador Dalí", "Claude Monet"],
        "answer": 3,
    },
    {
        "text": "What is the capital of Australia?",
        "options": ["Melbourne", "Sydney", "Canberra", "Brisbane"],
        "answer": 3,
    },
    {
        "text": "In which year did the first manned moon landing occur?",
        "options": ["1961", "1969", "1975", "1981"],
        "answer": 2,
    },
]
hard_questions = [
    {
        "text": "In which year did World War I begin?",
        "options": ["1912", "1914", "1916", "1918"],
        "answer": 2,
    },
    {
        "text": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Saturn", "Neptune"],
        "answer": 1,
    },
    {
        "text": "Who developed the theory of relativity?",
        "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Niels Bohr"],
        "answer": 2,
    },
    {
        "text": "Which chemical element has the symbol 'Au'?",
        "options": ["Silver", "Gold", "Platinum", "Copper"],
        "answer": 2,
    },
    {
        "text": "In what year did the Chernobyl disaster occur?",
        "options": ["1984", "1986", "1990", "1994"],
        "answer": 2,
    },
    {
        "text": "Who painted 'Starry Night'?",
        "options": ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Claude Monet"],
        "answer": 2,
    },
    {
        "text": "Which philosopher is known for his work on the social contract theory?",
        "options": ["John Locke", "Jean-Jacques Rousseau", "Thomas Hobbes", "Karl Marx"],
        "answer": 2,
    },
    {
        "text": "What is the speed of light in a vacuum?",
        "options": ["299,792 kilometers per second", "150,000 kilometers per second", "450,000 kilometers per second",
                    "600,000 kilometers per second"],
        "answer": 1,
    },
    {
        "text": "In which year did the Industrial Revolution begin?",
        "options": ["1700", "1750", "1800", "1850"],
        "answer": 2,
    },
    {
        "text": "Which novel opens with the line, 'Call me Ishmael'?",
        "options": ["Moby-Dick", "The Great Gatsby", "1984", "Pride and Prejudice"],
        "answer": 1,
    },
    {
        "text": "What is the world's longest river?",
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
        "answer": 1,
    },
    {
        "text": "Who is known as the 'Father of Modern Physics'?",
        "options": ["Max Planck", "Erwin Schrödinger", "Niels Bohr", "Albert Einstein"],
        "answer": 4,
    },
    {
        "text": "Which African country was formerly known as Abyssinia?",
        "options": ["Ethiopia", "Kenya", "Nigeria", "Ghana"],
        "answer": 1,
    },
    {
        "text": "Who wrote 'The Wealth of Nations'?",
        "options": ["Karl Marx", "John Locke", "Adam Smith", "David Ricardo"],
        "answer": 3,
    },
    {
        "text": "In what year did the Titanic sink?",
        "options": ["1908", "1912", "1916", "1920"],
        "answer": 2,
    },
    {
        "text": "Which hormone is known as the 'love hormone'?",
        "options": ["Insulin", "Oxytocin", "Serotonin", "Adrenaline"],
        "answer": 2,
    },
    {
        "text": "Who discovered penicillin?",
        "options": ["Alexander Fleming", "Louis Pasteur", "Marie Curie", "Joseph Lister"],
        "answer": 1,
    },
    {
        "text": "What is the capital of Australia?",
        "options": ["Sydney", "Canberra", "Melbourne", "Brisbane"],
        "answer": 2,
    },
    {
        "text": "Which element has the chemical symbol 'Fe'?",
        "options": ["Iron", "Gold", "Silver", "Copper"],
        "answer": 1,
    },
    {
        "text": "In what year was the Berlin Wall demolished?",
        "options": ["1985", "1989", "1995", "2000"],
        "answer": 2,
    },
    {
        "text": "Who is the author of 'The Catcher in the Rye'?",
        "options": ["J.D. Salinger", "F. Scott Fitzgerald", "Ernest Hemingway", "Ray Bradbury"],
        "answer": 1,
    },
    {
        "text": "What is the largest desert in the world?",
        "options": ["Gobi Desert", "Sahara Desert", "Antarctica", "Arabian Desert"],
        "answer": 3,
    },
    {
        "text": "Who developed the first successful polio vaccine?",
        "options": ["Jonas Salk", "Albert Sabin", "Edward Jenner", "Louis Pasteur"],
        "answer": 1,
    },
    {
        "text": "In what year did the American Civil War begin?",
        "options": ["1850", "1861", "1875", "1889"],
        "answer": 2,
    },
    {
        "text": "Which element is a noble gas and often used in balloons for lifting?",
        "options": ["Helium", "Neon", "Krypton", "Argon"],
        "answer": 1,
    },
    {
        "text": "Who won the Nobel Prize in Physics for the discovery of the neutron?",
        "options": ["Marie Curie", "Niels Bohr", "Ernest Rutherford", "James Chadwick"],
        "answer": 4,
    },
    {
        "text": "What is the currency of Japan?",
        "options": ["Won", "Yuan", "Yen", "Ringgit"],
        "answer": 3,
    },
    {
        "text": "Which ocean is the largest by area?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"],
        "answer": 4,
    },
    {
        "text": "Who wrote 'The Art of War'?",
        "options": ["Sun Tzu", "Machiavelli", "Homer", "Plato"],
        "answer": 1,
    },
    {
        "text": "In what year was the Magna Carta signed?",
        "options": ["1215", "1300", "1400", "1500"],
        "answer": 1,
    },
]
mixed_questions = [
    {
        "text": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"],
        "answer": 4,
    },
    {
        "text": "Which planet is known as the 'Blue Planet'?",
        "options": ["Mars", "Earth", "Venus", "Jupiter"],
        "answer": 2,
    },
    {
        "text": "Who is the author of 'To Kill a Mockingbird'?",
        "options": ["J.K. Rowling", "Harper Lee", "Ernest Hemingway", "Jane Austen"],
        "answer": 2,
    },
    {
        "text": "What is the currency of Japan?",
        "options": ["Yuan", "Yen", "Ringgit", "Won"],
        "answer": 2,
    },
    {
        "text": "Which country is known as the 'Land of the Rising Sun'?",
        "options": ["China", "Japan", "South Korea", "Vietnam"],
        "answer": 2,
    },
    {
        "text": "Who painted the 'Starry Night'?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "answer": 1,
    },
    {
        "text": "In which year did the Titanic sink?",
        "options": ["1912", "1920", "1931", "1945"],
        "answer": 1,
    },
    {
        "text": "What is the capital of Australia?",
        "options": ["Sydney", "Canberra", "Melbourne", "Brisbane"],
        "answer": 2,
    },
    {
        "text": "Who is known as the 'Father of Computers'?",
        "options": ["Alan Turing", "Charles Babbage", "Ada Lovelace", "Steve Jobs"],
        "answer": 2,
    },
    {
        "text": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": 2,
    },
    {
        "text": "Which country is famous for its tulips and windmills?",
        "options": ["Switzerland", "Netherlands", "Denmark", "Norway"],
        "answer": 2,
    },
    {
        "text": "What is the capital of Brazil?",
        "options": ["Sao Paulo", "Brasilia", "Rio de Janeiro", "Buenos Aires"],
        "answer": 2,
    },
    {
        "text": "Who wrote 'The Great Gatsby'?",
        "options": ["F. Scott Fitzgerald", "Herman Melville", "George Orwell", "Mark Twain"],
        "answer": 1,
    },
    {
        "text": "What is the main ingredient in guacamole?",
        "options": ["Avocado", "Tomato", "Onion", "Lime"],
        "answer": 1,
    },
    {
        "text": "What is the capital city of South Korea?",
        "options": ["Seoul", "Tokyo", "Beijing", "Bangkok"],
        "answer": 1,
    },
    {
        "text": "Who is the author of 'The Catcher in the Rye'?",
        "options": ["J.D. Salinger", "Ernest Hemingway", "F. Scott Fitzgerald", "George Orwell"],
        "answer": 1,
    },
    {
        "text": "What is the currency of South Africa?",
        "options": ["Rand", "Dollar", "Euro", "Peso"],
        "answer": 1,
    },
    {
        "text": "Which mountain is the highest in the world?",
        "options": ["Mount Kilimanjaro", "Mount Everest", "Mount McKinley", "Mount Fuji"],
        "answer": 2,
    },
    {
        "text": "Who is known as the 'Queen of Pop'?",
        "options": ["Madonna", "Beyoncé", "Lady Gaga", "Rihanna"],
        "answer": 1,
    },
    {
        "text": "In which year did World War II end?",
        "options": ["1943", "1945", "1950", "1960"],
        "answer": 2,
    },
    {
        "text": "What is the capital of Canada?",
        "options": ["Vancouver", "Ottawa", "Toronto", "Montreal"],
        "answer": 2,
    },
    {
        "text": "Which famous scientist developed the theory of relativity?",
        "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
        "answer": 2,
    },
    {
        "text": "What is the largest desert in the world?",
        "options": ["Sahara Desert", "Arabian Desert", "Antarctica", "Gobi Desert"],
        "answer": 3,
    },
    {
        "text": "Who painted the 'Mona Lisa'?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "answer": 3,
    },
    {
        "text": "Which country is known as the 'Land of the Rising Sun'?",
        "options": ["China", "Japan", "South Korea", "Vietnam"],
        "answer": 2,
    },
    {
        "text": "What is the capital of Mexico?",
        "options": ["Madrid", "Buenos Aires", "Mexico City", "Lima"],
        "answer": 3,
    },
    {
        "text": "In which year did the Berlin Wall fall?",
        "options": ["1985", "1989", "1991", "1995"],
        "answer": 2,
    },
    {
        "text": "Who is known as the 'Bard of Avon'?",
        "options": ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain"],
        "answer": 3,
    },
    {
        "text": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": 3,
    },
    {
        "text": "Which gas makes up the majority of Earth's atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": 3,
    },
]
    # Create a Quiz object and run the quiz
print("Welcome to Quiz Competetion.\n")
print("Instructions:")
print("1. For every correct answer you get 4 marks and for every wrong answer you get -1. Type 'leave' if you want to skip the question")
print("2. Write the option number. For eg. if second option is correct, your input should be 2")
print("3. You have only 100 seconds to answer 10 questions\n")
print("Choose your question level")
while True:
    print("1. Easy Level\n2. Medium Level\n3. Hard Level\n4. Mixed Questions\n5. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        my_quiz = Quiz(easy_questions)
        my_quiz.run_quiz()
        break
    elif choice == '2':
        my_quiz = Quiz(medium_questions)
        my_quiz.run_quiz()
        break
    elif choice == '3':
        my_quiz = Quiz(hard_questions)
        my_quiz.run_quiz()
        break
    elif choice == '4':
        my_quiz = Quiz(mixed_questions)
        my_quiz.run_quiz()
        break
    elif choice == "5":
        print("Exiting Quiz. Gooodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

