import sys
import os.path

currentArgs = sys.argv[1:]
if len(currentArgs) != 2 or currentArgs[0][0] != "-" or len(currentArgs[0]) != 2:
    print("Improper input format")
    print("The input format is as")
    sys.exit()          # This will exit the program as soon as we get improper input

if os.path.isfile("./" + currentArgs[1]) is False:
    print("File not found")
    sys.exit()          # This will exit the program as soon as we get improper input


    



    