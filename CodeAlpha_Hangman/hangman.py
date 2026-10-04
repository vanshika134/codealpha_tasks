import random

words = ["python", "java", "html", "coding", "laptop"]

word = random.choice(words)

guessed_word = ["_"] * len(word)

wrong_guesses = 0
max_wrong_guesses = 6

guessed_letters = []
correct_letters = []
wrong_letters = []

print("=" * 30)
print("       HANGMAN GAME")
print("=" * 30)

while wrong_guesses < max_wrong_guesses and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)
    print("Remaining attempts:", max_wrong_guesses - wrong_guesses)
    print("Correct letters:", ", ".join(correct_letters))
    print("Wrong letters:", ", ".join(wrong_letters))

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        correct_letters.append(guess)

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        print("Wrong!")
        wrong_letters.append(guess)
        wrong_guesses += 1


if "_" not in guessed_word:
    print("\n🎉 You won!")
    print("The word was:", word)
else:
    print("\n❌ Game over!")
    print("The word was:", word)