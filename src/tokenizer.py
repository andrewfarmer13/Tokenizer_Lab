import re as RE


counter = 0
# def readFile(fileIn):
#     outputBuffer = []
#     f = open(fileIn, "r")

#     # for lines in enumerate(f):
#     #     line = f.readline()
#     #     #print("Read: " + str(lines) + " "+line)
#     #     if( line[0] != "/" and line[0] != "/*"):
#     #         outputBuffer.append(lines[1])
#     #         outputBuffer.append(line)
        
#     data = f.readlines()
#     for line in data:
#        word = line.split()
#        outputBuffer.

                
    # return(outputBuffer)

def getChar(input):
    char = input
    return(char)

def nextChar(input):
    char = input[counter + 1]
    return(char)

def lex(file):
    # buffer = []
    # for strings in arrIn:
    #     for words in strings:
    #        for letter in words:
    #         # if(words != " "):
    #         char = getChar(words)
    #         buffer.append(char)
    #         print(buffer)

    #     buffer = []
    f = open(file, "r")
    data = f.readlines()
    for line in data:
        word = line.split()
        for elements in word:
            # if elements[0] == "//" or elements[0] == "/*":
            #     pass
            # else:
            #     for x in elements:
            #         print(x)
            #         if x == "class" or x == "function" or x == "void" or x == "var" or x == "Array" or x == "int" or x == "let" or x == "while" or x == "Keyboard.readInt" or x == "do" or x == "Output.printString" or x == "Output.printInt" or x == "Output.println" or x == "return":
            #             print("\t" + "<keyword>" + x + "<\keyword>")
            print(elements)


