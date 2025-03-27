#usr/bin/env python3

import random

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    # Checks the divisibility from 2 to square root of n
    for i in range(2, int(n**0.5) + 1):
        # If n is divisible by any number, it's not prime
        if n % i == 0:
            return False
    return True

def guess_the_prime():
    # Generate a list of prime numbers between 1 and 100
    primes = [num for num in range(1, 101) if is_prime(num)]
    secret_prime = random.choice(primes)
    attempts_left = 5  
    
    print("Welcome to 'Guess the Prime Number'!")
    print("I'm thinking of a prime number between 1 and 100. Can you guess it in 5 tries?")
    
    while attempts_left > 0:
        print(f"\nAttempts left: {attempts_left}")
        guess_input = input("Your guess: ")
        
        # Check if the input is a valid number
        if not guess_input.isdigit():
            print("❌ Please enter a valid number.")
            continue
        
        guess = int(guess_input)
        # Check if the number is between 1 and 100
        if guess < 1 or guess > 100:
            print("⚠️ Please enter a number between 1 and 100.")
            continue
        
        if guess == secret_prime:
            print(f"🎉 Correct! The prime number was {secret_prime}. You win!")
            return
        elif not is_prime(guess):
            print("❌ The number you guessed is not prime! Try again")
        elif guess < secret_prime:
            print("⬆️ Your guess is too low. Try higher.")
        else:
            print("⬇️ Your guess is too high. Try lower.")
        
        attempts_left -= 1  
    
    print(f"\nGame over! The prime number was {secret_prime}. Better luck next time!")

# Start the game
guess_the_prime()