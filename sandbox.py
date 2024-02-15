import sys
import os
print("Command Line Arguments", sys.argv)
currentArgs = sys.argv[1:]
if len(currentArgs) != 2 or currentArgs[0][0] != "-" or len(currentArgs[0]) != 2:
    print("Improper input format")
    print("The input format is as")
    sys.exit()
    


if os.path.isfile("./" + currentArgs[1]):
    print("File not found")
else:
    print("File Found")