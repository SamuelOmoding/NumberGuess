# NumberGuess
# Guess the Prime Number Game 🔢🎮

A simple Python game where you guessa randam prime number between 1-100 in 5 attempts. 


## 📜 Game Rules
- The computer selects a random prime number between 1 and 100.
- You have 5 attempts to guess the correct prime number.
- After each guess, you'll get a hint:  
  - ⬆️Too low! → Try a higher number.  
  - ⬇️Too high! → Try a lower number.  
- If you guess correctly within 5 tries, you win! 🎉  
- Otherwise, the game ends, and the correct number is revealed.  

## 🚀 How to Run the Game
1. Make sure you have Python 3 installed.  
2. Copy the code from [`guess_the_number.py`](#-code-overview) (or download the file).  
3. Run in terminal  
   ```bash
   python3 guess_the_prime.py

## Features
Simple, clean Python code
Error handling for invalid inputs
Clear feedback after each guess   

### Only 25 primes exist in 1-100 (Clever math+randomness)
Start with mid-range primes (like 37) to split possibilities.
Use the game's hints(⬆️/⬇️) to narrow down:
  If 37 is too low try higher primes (like 41,43,..).
  If too high try lower primes (like 31, 29,.)

Test case:
1. 50-17 -> 7
2. 37
3. 41-43->89
