FILE = "dictionary.txt"

'''
is_in_file: brute force search for word within given file
'''
def is_in_file(fileobject, word):
    for line in fileobject:
        if (line.strip() == word):
            return True
    return False

def main():
    # Opens a file. You can now look at each line in the file individually with a statement like "for line in f:"
    f = open(FILE,"r")

    print("Can your password survive a dictionary attack?")

    # Take input from the keyboard, storing in the variable test_password
    # NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
    test_password = input("Type in a trial password: ")
    test_password = test_password.strip()

    # Write logic to see if the password is in the dictionary file below here:
    invalid = is_in_file(f, test_password)
    while (invalid):
        print("That is a weak password. It is an actual word.")
        test_password = input("Try another password: ")
        test_password = test_password.strip()
        invalid = is_in_file(f, test_password)

    print("\nGood job making a password!")

if __name__ == '__main__':
    main()
