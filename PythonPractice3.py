#This script determines whether or not the word entered has an
#even or odd amount of letters
def even_or_odd(word):
    if len(word) % 2 == 0:
        print "Even"
    else:
        print "Odd"

word = raw_input("Please enter a word:")
even_or_odd(word)
