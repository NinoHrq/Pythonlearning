import sys
args = sys.argv[1:]
if len(args) == 0 :
    exit()
if len(args) > 1 :
    print("AssertionError: more than one argument is provided")
    exit()
try :
    n = int(args[0])
except ValueError:
    print("AssertionError: argument is not an integer")
    exit()
if (n == 0) :
    print("I'm Zero.")
elif (n % 2 == 0) :
    print("I'm Even.")
else :
    print("I'm Odd.")