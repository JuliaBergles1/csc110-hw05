"""
Name: Julia Bergles
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """ Ask for a valid uppercase letter: A, B, or C """
    # remove the default return and add your code
    while True:
        letter = input("Give an single uppercase letter: ") # ask the user to enter a letter
        if len(letter) != 1: # check that the input contains exactly one character
            print("Error: it needs to be a single character.")
            continue
        if letter != "A" and letter != "B" and letter != "C": # make sure the letter is one of the allowed options
            print("Error: You provided the wrong character.")
            continue
        return letter  # return the valid letter
        
        
        
        

def get_digit():
    """ Ask for a valid digit: 1, 2, or 3 """
    while True: # ask the user to enter a digit
        digit = input("Give an single number character: ")
        if not digit.isdigit(): # check that the input contains only digits
            print("Error: your input should be only digits.")
            continue
        if digit != "1" and digit != "2" and digit != "3":  # make sure the digit is 1, 2, or 3
            print("Error: a single digit needs to be in [1,3].")
            continue
        return digit # return the valid digit



def check_pattern(letter, digit, lst):
    """ Print each word containing the letter before the digit """
    print("Strings with the pattern:")
    for word in lst: # check each word in the list
        found = False
        #find a position containing the requested letter
        for i in range(len(word)):
            if word[i] == letter:
                #only check positions after the letter
                for j in range(i + 1, len(word)):
                    if word[j] == digit:
                        found = True  # stop searching once the pattern is found
                        break
            if found:
                break

        # print each matching word only once
        if found:
            print(word, end=" ")

    print()


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-digit pair and checks a list for strings where the letter appears before the digit"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    while True: # repeat the program until the user chooses to stop
        letter = get_letter() 
        digit = get_digit()

        check_pattern(letter, digit, st_list) # find and print all words matching the pattern

        again = input("Try Again? (y/n): ") # ask whether the user wants to try another pattern
        if again != "y":
            break 

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()