FILE = "dictionary.txt"
# my test file that only has a few  words
TESTFILE = "dictionary.txt"

'''
is_in_file: brute force search for word within given file
'''
def is_in_file(fileobject, word):
    for line in fileobject:
        if (line.strip() == word):
            return True
    return False

'''
check_substring: check if there is a real word within the given word
'''
def check_substring(fileobject, word):
    for line in fileobject:
        line = line.strip()
        if (len(line) > 3) and (line in word):
            print("--> Found this substring: " , line)
            return True
    return False

def main():
    # Opens a file. You can now look at each line in the file individually with a statement like "for line in f:"
    f = open(FILE,"r")
    # f = open(TESTFILE,"r")

    # turn the words in the dictionary into a list
    word_list = f.read().strip().split('\n')

    print("Can your password survive a dictionary attack?")

    invalid = True
    while (invalid):
        test_password = input("Type in a trial password: ")
        test_password = test_password.strip()

        if (is_in_file(word_list, test_password)):
            print("That is a very weak password. It is an actual word.")
            invalid = True
        elif (check_substring(word_list, test_password)):
            print("That is a weak password. There is a real word within it and it may not be very safe.")
            invalid = False

            if (input("Try again? (Y/N) ").upper() == "Y"):
                invalid = True
        else:
            invalid = False

    # exited while loop
    print("\nGood job making a password!")

if __name__ == '__main__':
    main()
