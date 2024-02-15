import sys
print("Command Line Arguments", sys.argv)
currentArgs = sys.argv[1:]
if len(currentArgs) != 2 or currentArgs[0][0] != "-":
    print("Improper input format")