#!/usr/bin/env python3
"""
This program has a user enter in a password and runs a series of checks
"""
from __future__ import print_function


def is_valid_password(password):
    """
    Checks to see if the new password is valid
    :param: password
    """
    print("Please re-enter your password: ")
    password_two = input()
    while(password != password_two):
        print("That password didn't have the required properties. # password did not match")
        main()
    # The password must be at least 8 char long
    length = len(password)
    if length <= 8:
        print ("That password didn't have the required properties. # password length")
        main()
    # The password must have one upper case
    elif password.islower is False:
        print ("That password didn't have the required properties. # No upper case letter")
        main()
    #The password must have one digit
    elif password.isalpha is True:
        print("That password didn't have the required properties.   # No digit")
        main()
    else:
        print("That pair of passwords will work")

def main():
    """
    Test your module
    """
    print("Enter your password: ")
    password = input()
    is_valid_password(password)


if __name__ == "__main__":
    main()
    exit(0)
