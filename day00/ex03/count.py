import sys
import string

def text_analyzer(argv=None):
    '''
    - Text_analyzer displays sums of upper characters, lower characters, punctuation characters and spaces in a given text.
    - Text_analylzer takes one parameter
    - If there is no text passed to the function, the user is prompted to give one.
    '''
    if argv is None:
        print("What is the text to analyse?")
        argv = input(">>")
    upper = sum(c.isupper() for c in argv)
    lower = sum(c.islower() for c in argv)
    punc = sum((c in string.punctuation) for c in argv)
    space = sum(c.isspace() for c in argv)

    print("The text contains {} characters:\n".format(len(argv)))
    print("- {} upper letters\n".format(upper))
    print("- {} lower letters\n".format(lower))
    print("- {} punctuation marks\n".format(punc))
    print("- {} spaces".format(space))
