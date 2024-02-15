import sys
import os.path

fileMode = sys.argv[1]
fileName = sys.argv[2]

if len(fileMode) != 2 or fileMode[0] != "-" or len(fileMode[0]) > 2:
    print("Improper input format")
    print("The input format is as")
    sys.exit()          # This will exit the program as soon as we get improper input

if os.path.isfile("./" + fileName) is False:
    print("File not found")
    sys.exit()          # This will exit the program as soon as we get improper input


    



    