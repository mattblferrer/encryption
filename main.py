import math


# takes input of message and key from the user
def caesar_input():
    while True:
        try:
            message = input("Enter message: ")
            key = int(input("Enter key: "))

        except ValueError:  # if user entered a non-integer key
            print("Invalid input. Try again.")

        else:
            return message, key


# converts message to array of numbers based on letters' position in the alphabet
def message_to_num(message):
    numbers = []

    for char in message:
        if char.isalpha():  # convert message to uppercase and remove special characters
            ascii_equiv = ord(char.upper()) - 65  # ASCII offset, A = 65
            numbers.append(ascii_equiv)
    return numbers


# converts array of numbers back to message
def num_to_message(numbers):
    message = ""

    for number in numbers:
        message += chr(number + 65)  # ASCII offset, A = 65
    return message


# encrypts message using the Caesar cipher
def caesar_encrypt(message, key):
    numbers = message_to_num(message)
    cipher_nums = []  # shifted numbers

    # Caesar shift
    for number in numbers:
        number = (number + key) % 26  # get shift mod 26
        cipher_nums.append(number)

    # translate shifted numbers to message
    return num_to_message(cipher_nums)


# encrypts message using the Vigenere cipher
def vigenere_encrypt(message, key):
    # convert both message and key to uppercase
    message = message.upper()
    key = key.upper()

    # take number equivalent of message
    message_num = message_to_num(message)
    length = len(message_num)

    # extend key to length of message
    n = length / len(key)
    n = math.ceil(n)
    key_to_n = key * n

    if len(key_to_n) != length:
        key_to_n = key_to_n[:length]

    # vigenere shift
    key_num = message_to_num(key_to_n)
    sum_num = []
    for i in range(length):
        num = (message_num[i] + key_num[i]) % 26
        sum_num.append(num)

    # return message
    sum_num_message = num_to_message(sum_num)
    return sum_num_message


# decrypts message using the Vigenere cipher
def vigenere_decrypt(message, key):
    # invert key
    key_num = message_to_num(key)
    key_num_inverted = num_to_message([(26-i) for i in key_num])

    # pass inverted key to encryption function
    return vigenere_encrypt(message, key_num_inverted)


def main():
    # user main menu
    while True:
        try:
            print("1. Caesar cipher encrypt")
            print("2. Caesar cipher decrypt")
            print("3. Vigenere cipher encrypt")
            print("4. Vigenere cipher decrypt")

            selection = int(input("Select function. Enter number to continue. \n"))

        # invalid input
        except ValueError:
            print("Invalid input. Please try again.")

        # valid input
        else:
            # parse user's decision
            if selection == 1:
                # user_input
                user_input = caesar_input()
                message, key = user_input[0], user_input[1]

                output = caesar_encrypt(message, key)
                print("The coded message is {}".format(output))

            elif selection == 2:
                # user_input
                user_input = caesar_input()
                message, key = user_input[0], user_input[1]

                output = caesar_encrypt(message, -key)
                print("The original message is {}".format(output))

            elif selection == 3:
                # user_input
                message = input("Enter message: ")
                key = input("Enter key: ")

                output = vigenere_encrypt(message, key)
                print("Encrypted message: {}".format(output))

            elif selection == 4:
                # user_input
                message = input("Enter message: ")
                key = input("Enter key: ")

                output = vigenere_decrypt(message, key)
                print("Decrypted message: {}".format(output))

            else:
                print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
