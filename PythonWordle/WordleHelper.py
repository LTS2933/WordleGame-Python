import random

class WordleHelper:
    ANSI_GREEN = "\u001B[32m"
    ANSI_YELLOW = "\u001B[33m"
    ANSI_DEFAULT = "\u001B[0m"

    @staticmethod
    def random_words_to_array(file_name):
        random_words = []
        try:
            with open(file_name, "r") as file:
                random_words = file.readlines()
        except IOError as e:
            print(e)
        
        random_words_array = [word.strip() for word in random_words]
        return random_words_array

    @staticmethod
    def generate_answer(random_words_array):
        answer = random.choice(random_words_array).upper()
        return answer

    @staticmethod
    def is_valid_word(word, random_words_array):
        return word.upper() in random_words_array

    @staticmethod
    def char_count(word, c):
        count = 0
        for char in word:
            if char == c:
                count += 1
        return count

    @staticmethod
    def game_play():
        correct_answer = False
        random_words_array = WordleHelper.random_words_to_array("randomWords.txt")
        answer = WordleHelper.generate_answer(random_words_array)
        for _ in range(6):
            print(f"Guess {_ + 1} of 6")
            guess = input("Enter your 5-letter guess: ").upper()

            while (
                guess is None 
                or not guess.isalpha() 
                or len(guess) != 5 
                or not WordleHelper.is_valid_word(guess, random_words_array)

            ):
                if len(guess) != 5:
                    print("Your guess must be 5 letters!")
                else:
                    print("Your guess must be a valid word!")
                guess = input("Enter your 5-letter guess: ").upper()

            colored_result = []
            for guess_index, guess_char in enumerate(guess):
                if guess_char == answer[guess_index]:
                    colored_result.append(WordleHelper.ANSI_GREEN + guess_char + WordleHelper.ANSI_DEFAULT)
                elif guess_char in answer:
                    if WordleHelper.char_count(answer, guess_char) < WordleHelper.char_count(guess, guess_char):
                        colored_result.append(guess_char)
                    else:
                        colored_result.append(WordleHelper.ANSI_YELLOW + guess_char + WordleHelper.ANSI_DEFAULT)
                else:
                    colored_result.append(guess_char)

            print("".join(colored_result))
            
            if guess == answer:
                print("Congratulations! You guessed correctly.")
                correct_answer = True
                break

        if not correct_answer:
            print(f"Sorry, you did not answer correctly.\nThe correct answer was {answer}")

        response = input("Would you like to play again? Enter 'Y' or 'Yes': ")
        if response.upper() in ["Y", "YES"]:
            WordleHelper.game_play()
        else:
            print(f"You entered '{response}' thanks for playing!")

if __name__ == "__main__":
    WordleHelper.game_play()
