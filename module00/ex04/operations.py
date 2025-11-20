import sys
args = sys.argv[1:]
if len(args) == 0 :
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")
    exit()
elif len(args) > 2 :
    print("AssertionError: too many arguments")
    exit()
elif len(args) == 1 :
    print("AssertionError: not enough arguments")
    exit()
try :
    A = int(args[0])
except ValueError:
    print("AssertionError: only integers")
    exit()
try :
    B = int(args[1])
except ValueError:
    print("AssertionError: only integers")
    exit()
s = A + B
diff = A - B
prod = A * B


print("Sum:", s)
print("Difference:", diff)
print("Product:", prod)

if B == 0:
    print("Quotient: ERROR (division by zero)")
    print("Remainder: ERROR (modulo by zero)")
else:
    print("Quotient:", A / B)
    print("Remainder:", A % B)
