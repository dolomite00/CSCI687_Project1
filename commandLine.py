import sys

argCount = len(sys.argv)
args = sys.argv

if argCount == 2:
    print(f"filename is {args[1]}")
elif argCount == 3:
    print(f"array size is {args[1]}")
    print(f"filename is {args[2]}")
else:
    print("This program should be invoked from the command-line as:")
    print("python3 <name of python script file> <command-file>")
    print("or")
    print("python3 <name of python script file> <array size> <command-file>")
    exit(0)

# use these two variables
inputfilename = args[1]
arraysize = args[2]


