# encrypts message using the Caesar cipher
def caesar_encrypt(message, key):
    pass


# decrypts message using the Caesar cipher
def caesar_decrypt(message, key):
    pass


# encrypts message using the Vigenere cipher
def vigenere_encrypt(message, key):
    pass


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
                message = input("Enter message: ")
                key = input("Enter key: ")
                caesar_encrypt(message, key)

            elif selection == 2:
                message = input("Enter message: ")
                key = input("Enter key: ")
                caesar_decrypt(message, key)

            elif selection == 3:
                message = input("Enter message: ")
                key = input("Enter key: ")
                vigenere_encrypt(message, key)

            elif selection == 4:
                message = input("Enter message: ")
                key = input("Enter key: ")
                vigenere_decrypt(message, key)

            else:
                print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
