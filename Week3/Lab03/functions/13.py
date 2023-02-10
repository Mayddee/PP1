print('Hello! What is your name?')
name = input()
print("Well,", name, ", I am thinking of a number between 1 and 20.")
print("Take a guess.")
x = int(input())
n = 19
for i in range(20):
    if x == n:
        break
    print("Your guess is too low.")
    print("Take a guess.")
    x = int(input())
    print(" ")
print("Good job,", name, "! You guessed my number in", i + 1, "guesses!")