'''
My version of the Guess the Hidden Word game
'''

secret = "spotify"
blanks = [" _ "]*len(secret)
TRIES = len(secret) * 2
guesses = ""

is_correct = False
is_correct_guess = False
cur_try = 0

while (not is_correct) and (cur_try < TRIES):
    is_correct_guess = False
    # print blanks
    for b in blanks:
        print(b, end=" ")

    # print number of tries -- NOTE: do this on a new line! Thus "\n"
    print("\nTries left: ", TRIES - cur_try)
    
    guess = input("Guess a letter: ")

    #print(len(guess)) # NOTE: debugging my "or" problem

    # check if 1 letter was input -- NOTE: accidentally used an "or" here!
    if (len(guess) != 1) and (len(guess) != len(secret)):
        print("ERROR. Either enter one character or guess entire word.")
    else:
        # guess is 1 char or entire word
        cur_try += 1
        if (len(guess) == 1):
            # tried to guess one letter
            # have they tried to guess this already
            if guess in guesses:
                print("INVALID GUESS. Already guessed this letter.")
            else:
                guesses += guess
                # loop through and find if the letter is correct
                for i in range(len(secret)):
                    if (secret[i] == guess):
                        # found a correct letter!
                        blanks[i] = guess
                        is_correct_guess = True
                if (is_correct_guess):
                    print("Good guess!")
        else:
            # tried to guess entire word
            if guess == secret:
                is_correct = True
            else:
                is_correct = False
                print("That is not the secret word.")
                
    # check if we've filled in all the blanks
    if (" _ " not in blanks):
        is_correct = True

# done!
if (is_correct):
    print("\nCongrats! You won!")
else:
    print("\nGood try!")
