import re as RE


counter = 0
def readFile(fileIn):
    outputBuffer = []
    f = open(fileIn, "r")

    for lines in enumerate(f):
        line = f.readline()
        #print("Read: " + str(lines) + " "+line)
        if( line[0] != "/" and line[0] != "/*"):
            outputBuffer.append(lines[1])
            outputBuffer.append(line)
        

    
    # for lines in f:
    #     for word in lines.split():
            
    #         if word != "//":
    #             if word == str(range_char("a", "z")):
    #                 print("<Identifier>", word, "</Identifier>")
    #             elif word == '0-9':
    #                 print("<Digit>", word, "</Digit>")

                
    return(outputBuffer)

def getChar(input):
    char = input
    return(char)

def nextChar(input):
    char = input[counter + 1]
    return(char)

def lex(arrIn):
    buffer = []
    for strings in arrIn:
        for words in strings:
           for letter in words:
            if(words != " "):
                char = getChar(words)
                buffer.append(char)
                #print(buffer)
            for item in buffer:
                if(item == "=" or item == ";"):
                    print(" <symbol>" + item + "</symbol>")
        buffer = []
