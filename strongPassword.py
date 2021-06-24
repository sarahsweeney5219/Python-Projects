#strongPassword.py
#uses regular expressions to make sure the user's password is "strong"
#this means it is at least eight characters long, contains both uppercase and lowercase characters,
#and has at least one digit

import re

#checks to see if there is at least one uppercase letter, at least one lowercase letter, at least
#one number, at least one special symbol, and that the password is at least 8 characters long.

def checkPassword(text):
    checkLength = re.compile(r'(\w{8,})')
    checkForNum = re.compile(r'([0-9]+)')
    checkForUpper = re.compile(r'([A-Z]+)') #checks for uppercase letter
    checkForLower = re.compile(r'([a-z]+)') #checks for lowercase letter
    checkForSymbol = re.compile(r'[@%+\/!$#?.(){}~\-]')
    if (checkLength.findall(text) == []):
        print('Your password is too short.')
        tryAgain()
    elif(checkForNum.findall(text) == []):
        print('Your password is missing a number.')
        tryAgain()
    elif(checkForUpper.findall(text) == []):
        print('Your password is missing an uppercase letter.')
        tryAgain()
    elif(checkForLower.findall(text) == []):
        print('Your password is missing a lowercase letter.')
        tryAgain()
    elif(checkForSymbol.findall(text) == []):
        print('Your password is missing a special symbol.')
        tryAgain()
    else:
        print('Your password ' + text + " is a strong password")

def tryAgain():
    attempt = input('Try again:')
    checkPassword(attempt)

pswrd = input('Hello. Please enter a password you would like to test.\n')
checkPassword(pswrd)

