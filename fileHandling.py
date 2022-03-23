import sys

argCount = len(sys.argv)
args = sys.argv
filename = ""
arraySize = -1

if argCount == 2:
    filename = args[1]
elif argCount == 3:
    filename = args[2]
    arraySize = args[1]
else:
    print("This program should be invoked from the command-line as:")
    print("python3 <name of python script file> <command-file>")
    print("or")
    print("python3 <name of python script file> <array size> <command-file>")
    exit(0)

with open(filename, "r") as ifile:
    lines = ifile.readlines()

for line in lines:
    print(line)

if argCount == 3:
    print(f"array size is: {args[1]}")
else:
    print("default array size is used")
    

