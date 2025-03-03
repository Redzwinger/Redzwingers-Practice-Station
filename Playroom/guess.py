# Text-Based Number Guessing Game
import random

def generate_hint(secret_number, guess_count):
    """Generates hints based on the current guess round."""
    if guess_count == 1:
        return f"The number is greater than {secret_number - random.randint(1, 10)}."
    elif guess_count == 2:
        return f"The number is {'even' if secret_number % 2 == 0 else 'odd'}."
    elif guess_count == 3:
        hints = [
            f"The number squared is greater than {secret_number ** 2 - random.randint(1, 50)}.",
            f"The number cubed is less than {secret_number ** 3 + random.randint(1, 100)}.",
            f"The number is a multiple of 3." if secret_number % 3 == 0 else "The number is not a multiple of 3.",
            f"The number is a prime number." if all(secret_number % i != 0 for i in range(2, int(secret_number ** 0.5) + 1)) else "The number is not a prime number.",
            f"The number is divisible by 5." if secret_number % 5 == 0 else "The number is not divisible by 5.",
            f"The sum of the digits is {sum(int(digit) for digit in str(secret_number))}.",
            f"The number minus 10 is {secret_number - 10}.",
            f"The product of its digits is {eval('*'.join(str(secret_number)))}.",
            f"The number when divided by 4 gives a remainder of {secret_number % 4}.",
            f"The number is a perfect square." if (int(secret_number ** 0.5)) ** 2 == secret_number else "The number is not a perfect square."
        ]
        return random.choice(hints)
    elif guess_count == 4:
        lower_bound = max(1, secret_number - 5)
        upper_bound = min(100, secret_number + 5)
        hints = [
            f"The number is between {lower_bound} and {upper_bound}.",
            f"The number is closer to {lower_bound + (upper_bound - lower_bound) // 2} than to 1 or 100.",
            f"The number has {len(str(secret_number))} digits.",
            f"The number is higher than {lower_bound + random.randint(1, 3)}.",
            f"The number is lower than {upper_bound - random.randint(1, 3)}."
        ]
        return random.choice(hints)
    elif guess_count == 5:
        hints = [
            f"The number is within 3 units of {secret_number + random.randint(-3, 3)}.",
            f"The tens digit is {str(secret_number)[0]}.",
            f"The number ends with {str(secret_number)[-1]}.",
            f"The number is a palindrome." if str(secret_number) == str(secret_number)[::-1] else "The number is not a palindrome.",
            f"The number is divisible by 2 and 3." if secret_number % 6 == 0 else "The number is not divisible by 2 and 3."
        ]
        return random.choice(hints)
    else:
        return "No more hints available."

def play_round():
    secret_number = random.randint(1, 100)
    print("\nNew round! You have 5 guesses to find the number.")

    for guess_count in range(1, 6):
        guess = int(input(f"Guess {guess_count}: Enter your guess (1-100): "))
        
        if guess == secret_number:
            print("Congratulations! You guessed the number correctly.")
            return True
        else:
            print("Incorrect.")
            hint = generate_hint(secret_number, guess_count)
            print(f"Hint {guess_count}: {hint}")

    print(f"Sorry, you've used all your guesses. The correct number was {secret_number}.")
    return False

def main():
    play_again = True
    while play_again:
        play_round()
        play_again = input("Do you want to play another round? (yes/no): ").lower() == 'yes'
    print("Thanks for playing!")

if __name__ == "__main__":
    main()


