import sys
import os.path

fileMode = sys.argv[1]
fileName = sys.argv[2]

# Check is fileMode is correct or not
if len(fileMode) > 2 or fileMode[0] != "-":
    print("Improper input format")
    print("The input format is as Hello")
    sys.exit()          # This will exit the program as soon as we get improper input


if len(fileMode) > 1 and fileMode[1] not in ("c","l","w","m"):
    print("Invalid command \nUse -c for number of bytes, -l for number of lines, -w for  number of words")
elif len(fileMode) == 1 and fileMode != "-":
    print("Invalid command \nUse -c for number of bytes, -l for number of lines, -w for  number of words, - for all of these")

# Check if the fileName is correct or not
if os.path.isfile("./" + fileName) is False:
    print("File not found")
    sys.exit()          # This will exit the program as soon as we get improper input

# -c Output the number of bytes in file
if fileMode == "-c":
    print(str(os.path.getsize("./" + fileName)) + "  " + fileName)

# -l Output the number of lines in file
elif fileMode == "-l":
    with open("./" + fileName,"r") as fp:
        print(str(len(fp.readlines())) + "  " + fileName)
    fp.close()
    
# -w Output the number of words in file
elif fileMode == "-w":
    with open("./" + fileName,"r") as fp:
        content = fp.read()
        wordCount = len(content.split())
        print(str(wordCount) + "  " + fileName)
    fp.close()  

# -m Output the number of characters in file
elif fileMode == "-m":
    with open("./" + fileName,"r") as fp:
        content = fp.read()        
        print(str(len(content)) + "  " + fileName)

    
# - Output the number of characters in file
elif fileMode == "-":
    with open("./" + fileName,"r") as fp:
        lines = len(fp.readlines())
        fileSize = os.path.getsize("./" + fileName)        
    fp.close()
    
    
    with open("./" + fileName,"r") as fp:
        words = len(fp.read().split())      
        print(str(fileSize) + "  "  + str(lines) + "  "  + str(words) + " " + fileName)
    fp.close()
