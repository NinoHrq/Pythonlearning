import sys
args = sys.argv[1:]
if not args:
    exit()
text = " ".join(args)
reversed_text = text[::-1]
final_text = reversed_text.swapcase()
print(final_text)