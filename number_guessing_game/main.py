import random

def main():
    print("Welcome to the number guessing game!")
    computer_choice = random.randint(1, 100)


    while True:
        try:
            guess = int(input("Please enter any number from (1 to 100):  "))

            if guess < computer_choice:
                print("Too low!")
            elif guess > computer_choice:
                print("Too high!")
            else:
                print("Congratulations! You guessed it")
                break

        except ValueError:
            print("Please select a integer value only")
            
if __name__ == "__main__":
    main()