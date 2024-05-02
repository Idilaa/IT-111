def display_partial_solution(solution, guessed_letters):
    partial_solution = ''
    for letter in solution:
        if letter in guessed_letters:
            partial_solution += letter
        else:
            partial_solution += '_'
    return partial_solution

def main():
    solution = "succotash"
    guessed_letters = []
    attempts = 6

    print("Welcome to Wheel of Fortune!")
    print("Guess the letters in the word. You have {} attempts.".format(attempts))

    while attempts > 0:
        print("\nCurrent partial solution:", display_partial_solution(solution, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)
        if guess in solution:
            print("Yes, '{}' appears {} time(s) in the solution.".format(guess, solution.count(guess)))
        else:
            print("No, '{}' is not in the solution.".format(guess))
            attempts -= 1

        if '_' not in display_partial_solution(solution, guessed_letters):
            print("\nCongratulations! You've guessed the word:", solution)
            break

    if attempts == 0:
        print("\nSorry, you've run out of attempts. The word was:", solution)

if __name__ == "__main__":
    main()
