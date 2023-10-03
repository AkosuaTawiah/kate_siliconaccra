correct_guess = 20
for correct in range(3):
    guess_number = int(input("Guess the number in my head: "))
if guess_number == correct_guess:
    print("you guessed the correct number")
    break
elif guess_number > correct_guess:
    print("your number is too high")
elif guess_number < correct_guess:
    print("your number is too low")
else:
    print("you guessed wrongly")
