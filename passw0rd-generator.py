#!/usr/bin/env python3
import sys, getopt

"""
Super secure password generator!

This python script generates passwords using the random python module to pick
from all alphanumeric characters. The user can determine the length of the
passwords as well as the number of passwords he wants to have generated. Ulti-
mately, the user has the option to save the passwords in a .csv file, line by
line.

Warning: The option to save the passwords to a .csv is implemented just for edu-
cational purposes. Never should you save passwords which you intend to use un-
protected on your machine.

The script can be used in two ways: Either by executing it with the keyword
arguments -c, -n and -s, denoting the number of characters for every password,
the number of passwords and the option whether to save them as csv. -c is manda-
tory, -n defaults to 1, -s defaults to 'n'.
Alternatively, the script prompts the user to input these values, when no key-
word arguments are provided.
"""

# FUNCTION DECLARING

# Get all alphanumeric characters except '\\'
all_chars = [chr(i) for i in range(33, 127)]
all_chars.remove("\\")

def generate_pw_w_random(no_of_chars):
    """
    Returns a string of randomly generated alphanumeric characters. The input
     string is checked if it is a digit, if not, a ValueError is raised.
    """

    # Test if no_of_chars is valid
    isdigit(no_of_chars)

    # Generate list of passwords with length of no_of_chars
    import random
    return ''.join([random.choice(all_chars) for i in range(int(no_of_chars))])

def isdigit(value):
        if not value.isdigit() :
            print( "Please enter a valid integer value > 0")
            raise ValueError('Input was a non valid integer! Try again.')

def save_to_csv(pw_list, filename):
    """
    Function that writes the list pw_list to a .csv file of the working
    directory, naming it with string provided in the imput argument <filename>.
    """
    import csv
    file = open(filename, 'w')
    with file:
        writer = csv.writer(file, delimiter='\n')
        print('pw_list', pw_list)
        writer.writerow(pw_list)
    print(f"Writing is done, saved as {filename}")

def is_choice_valid(choice):
    """
    Check, if the input argument <choice> is valid, which is 'Y', 'y', 'N' or
    'n'. Raise Value Error if not.
    """
    if not choice.lower() in ('y', 'n'):
        print("Invalid choice, please enter Y or y for Yes OR N or n for No.")
        raise ValueError('Invalid Choice Try again.')

def choice2boolean(choice):
    """
    Expects an input string of 'y' or 'n', returns True or False respectively.
    """
    choice_dct = {'y': True,
                  'n': False,
                 }
    return choice_dct[choice.lower()]

def handle_args(argv):
    """
    Handles the keyword arguments for the command line execution of the program
    when it is executed in keyword mode. Prints the correct function usage when
    key -h is used.
    Returns the number of characters, number of passwords and the coice if user
    wants to save as csv. Each return value is extracted from the keyword argu-
    ments and for each, the value None is provided, if the corresponding value
    is not in the keywords.
    """

    no_of_chars = '1'
    no_of_pwds = '1'
    choice = 'n'

    try:
        opts, args = getopt.getopt(argv,"hc:n:s:",["chars=","number=", "save="])
    except getopt.GetoptError:
        print('test.py -c <no_of_chars> -n <no_of_pwds> -s <savetocsv? y|n >')
        sys.exit(2)
    # Make sure, -c is provided
    if "-c" not in argv and "--charsize" not in argv:
        print("Providing -c or --charsize value is mandatory. Try again.")
        sys.exit()
    for opt, arg in opts:
        print(opt, arg)
        if opt == '-h':
            print("Usage: \n passw0rd_generator.py -c <no_of_chars> -n"\
                  " <no_of_pwds> -s <savetocsv>")
            sys.exit()
        elif opt in ("-n", "--numberofpwds"):
            no_of_pwds = arg
        elif opt in ("-s", "--savetocsv"):
            choice = arg
        else:
            no_of_chars = arg
    return no_of_chars, no_of_pwds, choice

def info_wrong_script_usage():
    print("Wrong usage. Usage: \n passw0rd_generator.py -c <no_of_chars>"\
          " -n <no_of_pwds> -s <savetocsv>\n type of <no_of_chars> : "\
          " int >= 0 \n type of <no_of_pwds> : int >=0\n type of <choice> "\
          ": str of ('Y'|'y'|'N'|'n') ")
    sys.exit()

# DECLARATION OF MAIN PROGRAMS

def main_cmdline_interact():
    """
    Main function which executes the script when no keywords are given. The
    user is here asked to enter the values successively.
    """
    while True:
        no_of_chars = input("How many characters do you want in your password?")
        try:
            # Check if above input is digit, if not catch Value Error and ask
            # again
            isdigit(no_of_chars)
        except ValueError:
            continue

        while True:
            no_of_pwds = input("And how many passwords do you want?")
            try:
                # Check if above input is digit, if not catch the Error and ask
                # again
                isdigit(no_of_pwds)
            except ValueError:
                continue

            # By now, all input values should be valid, so generate the
            # passwords
            pws =  [generate_pw_w_random(no_of_chars)
                    for n in range(int(no_of_pwds))]

            # Print passwords
            print("Here are your 'safe' passwords:\n")
            for pw in pws:
                print(f"{pw}\n")

            # Enable user to write passwords to csv-file
            while True:
                choice = input("Save them to .csv-file? (not recommended \
                               though ^^)\n\n (Y)es or (N)o")

                # Check if choice is valid, if not catch the Error and ask again
                try:
                    is_choice_valid(choice)
                except ValueError:
                    continue

                # Choice is valid, so write to csv if user chose to
                if choice2boolean(choice):
                    save_to_csv(pws, 'your_password_list.csv')
                break
            break
        break

def main(no_of_chars, no_of_pwds, choice):
    """
    Main function which is executed when keywords are provided.
    """
    try:
        isdigit(no_of_chars)
        isdigit(no_of_pwds)
        is_choice_valid(choice)
    except ValueError:
        info_wrong_script_usage()

    pws =  [generate_pw_w_random(no_of_chars) for n in range(int(no_of_pwds))]
    print("Here are your 'safe' passwords:\n")

    for pw in pws:
        print(f"{pw}\n")

    if choice2boolean(choice):
        save_to_csv(pws, 'your_password_list.csv')

# PROGAM EXECUTION

if __name__ == "__main__":
    # If user doesn't provide cmdline arguments, have it interact with program
    # via cmdline dialoge
    if len(sys.argv[1:]) == 0:
        main_cmdline_interact()

    # ... else use the cmdline arguments provided
    else:
        main(*handle_args(sys.argv[1:]))
