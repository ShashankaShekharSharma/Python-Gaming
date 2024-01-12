import random
import time
import msvcrt

class TypingTest:
    def __init__(self, word_count):
        self.word_count = word_count
        self.words_list = [
            "the", "be", "of", "and", "a", "to", "in", "he", "have", "it", "that", "for", "they", "with", "as", "not",
            "on", "she", "at", "by", "this", "we", "you", "do", "but", "from", "or", "which", "one", "would", "all",
            "will", "there", "say", "who", "make", "when", "can", "more", "if", "no", "man", "out", "other", "so",
            "what", "time", "up", "go", "about", "than", "into", "could", "state", "only", "new", "year", "some", "take",
            "come", "these", "know", "see", "use", "get", "like", "then", "first", "any", "work", "now", "may", "such",
            "give", "over", "think", "most", "even", "find", "day", "also", "after", "way", "many", "must", "look",
            "before", "great", "back", "through", "long", "where", "much"
        ]

    def generate_random_sentence(self):
        sentence = " ".join(random.choice(self.words_list) for _ in range(self.word_count))
        return sentence

    def typing_test(self):
        print(f"Welcome to the Typing Test!")

        sentence_to_type = self.generate_random_sentence()

        print(f"\nType this sentence:\n\n{sentence_to_type}")

        start_time = None
        while True:
            if msvcrt.kbhit():
                start_time = time.time()
                break

        user_input = input("Your input:\n").strip()

        correct_words = sum(1 for word1, word2 in zip(sentence_to_type.split(), user_input.split()) if word1 == word2)
        accuracy = (correct_words / self.word_count) * 100

        print("\nGame Over!")
        end_time = time.time()
        time_taken = end_time - start_time

        print(f"Time : {time_taken:.2f} seconds")
        print(f"Speed : {(correct_words / time_taken) * 60:.2f} WPM")
        print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    print("Choose the number of words to type:")
    print("1. 30 words")
    print("2. 50 words")
    print("3. 100 words")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        test = TypingTest(30)
    elif choice == '2':
        test = TypingTest(50)
    elif choice == '3':
        test = TypingTest(100)
    else:
        print("Invalid choice. Please run the script again.")

    test.typing_test()

