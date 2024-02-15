import sys
import os

fileMode = sys.argv[1]
fileName = sys.argv[2]

if len(fileMode) > 2 or fileMode[0] != "-":
    print("Improper input format")
    print("The input format is as Hello")
    sys.exit()          # This will exit the program as soon as we get improper input

if os.path.isfile("./" + fileName) is False:
    print("File not found")
    sys.exit()          # This will exit the program as soon as we get improper input

if len(fileMode) > 1 and fileMode[1] not in ("c","l","w","m"):
    print("Invalid command \nUse -c for number of bytes, -l for number of lines, -w for  number of words")
elif len(fileMode) == 1 and fileMode != "-":
    print("Invalid command \nUse -c for number of bytes, -l for number of lines, -w for  number of words")

# -c Output the number of bytes in file
if fileMode == "-c":
    print(str(os.path.getsize("./" + fileName)) + "  " + fileName)

print(len(fileMode),fileMode[1])   
print("ALL SET")