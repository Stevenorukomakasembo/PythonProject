import random

# Generate a random number between 5 and 25
secret_number = random.randint(5, 25)

def main():
    # Initialize the number of tries
    count = 0
    
    # Loop infinitely
    while(True):
        guessed_number  = int(input("Guess a number: "))

        # Increment the number of tries
        count += 1

        # Determine if guessed number is greater or less than the secret number
        if guessed_number > secret_number:
            print("Your guessed number is greater than the secret number.")
        elif guessed_number < secret_number:
            print("Your guessed_number is less than the secret number.")
        else:
            print(f"Number of tries: {count}")
            print("Your guessed number is correct!")
            break

        # Compare digits  
        assert_digits(guessed_number, secret_number)

        # Print the number of trials
        print(f"Number of tries: {count}")


def assert_digits(guessed_number, secret_number):
    """
    Determine how many digits have been guessed correctly in the correct 
    place and how many digits have been guessed correctly but in the wrong
    place.
    """
    # Convert guessed number and secret number to string 
    guessed_number = str(guessed_number)
    secret_number = str(secret_number)
    
    # Initialize correctly placed and wrongly placed digits
    wrong_place = 0
    correct_place = 0
    checked = []
    
    # Determine number with less number of digits
    if len(guessed_number) > len(secret_number):
        shortest_length = len(secret_number)
    elif len(guessed_number) < len(secret_number):
        shortest_length = len(guessed_number)
    else:
        shortest_length =  len(secret_number)
    
    # Determine digits guessed correctly in right place
    for i in range(shortest_length):
        if secret_number[i] == guessed_number[i]:
            correct_place += 1
            checked.append(guessed_number[i])
    
    # Determine digits gussed correctly in wrong place
    for digit1 in guessed_number:
        for digit2 in secret_number:
            if digit1 == digit2 and digit1 not in checked:
                wrong_place += 1
                checked.append(digit1)
    
    print(f"{correct_place} digits have been guessed correctly in the right place")
    print(f"{wrong_place} digits have been guessed correctly in the wrong place")


if __name__ == "__main__":
    main()
