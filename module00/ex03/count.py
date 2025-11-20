import sys

def text_analyzer(text=None) :
    """Cette fonction compte le nombre de majuscules, minuscules, ponctuation et espaces dans un texte"""

    if text is None :
        print("What is the text to analyze?")
        text = input()
    if not isinstance(text, str) :
        print("AssertionError: argument is not a string")
        return
    upper = 0
    lower = 0
    punct = 0
    spaces = 0
    punctuation = ".,;:!?-_'\"()[]{}/\\"
    for c in text:
        if c.isupper() :
            upper += 1
        elif c.islower() :
            lower += 1
        elif c == " " :
            spaces += 1
        elif c in punctuation:
            punct += 1
    total = len(text)
    print("The text contains", total, "printable character(s):")
    print("-", upper, "upper letter(s)")
    print("-", lower, "lower letter(s)")
    print("-", punct, "punctuation mark(s)")
    print("-", spaces, "space(s)")

if __name__=="__main__":
    args = sys.argv[1:]
    if len(args) > 1 :
        print("AssertionError: more than one argument is provided")
    elif len(args) == 1 :
        text_analyzer(args[0])
    else :
        text_analyzer()