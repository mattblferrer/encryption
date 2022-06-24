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
# TODO: added selection parameter, update arguments hehe
def message_to_num(message, selection):
    numbers = []

    if selection == 1 or selection == 2:
        for char in message:
            if char.isalpha():  # convert message to uppercase and remove special characters
                ascii_equiv = ord(char.upper()) - 64  # ASCII offset, A = 65
                numbers.append(ascii_equiv)
        return numbers

    elif selection == 3 or selection == 4:
        for char in message:
            if char.isalpha():
                num = ord(char) - 97
                numbers.append(num)
        return numbers


# converts array of numbers back to message
# TODO: added selection parameter, update arguments hehe
def num_to_message(numbers, selection):
    message = ""

    if selection == 1 or selection == 2:
        for number in numbers:
            message += chr(number + 64)  # ASCII offset, A = 65
        return message

    elif selection == 3 or selection == 4:
        for number in numbers:
            message += chr(number + 97)
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
    message = message.lower()
    key = key.lower()
    message_num = message_to_num(message, 3)
    length = len(message_num)

    n = length / len(key)
    n = math.ceil(n)

    key_to_n = key * n

    if len(key_to_n) != length:
        key_to_n = key_to_n[:length]

    key_num = message_to_num(key_to_n, 3)
    sum_num = []
    for i in range(length):
        num = message_num[i] + key_num[i]
        if num > 25:
            num = num - 26
        sum_num.append(num)

    sum_num_message = num_to_message(sum_num, 3)
    print("Encrypted message: {}".format(sum_num_message))


# decrypts message using the Vigenere cipher
def vigenere_decrypt(message, key):
    pass


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

                vigenere_encrypt(message, key)

            elif selection == 4:
                # user_input
                message = input("Enter message: ")
                key = input("Enter key: ")

                vigenere_decrypt(message, key)

            else:
                print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
