outputBuffer = []
counter = 0
def readFile(fileIn):
    f = open(fileIn, "r")
    # for char in f:
    #     c = getChar(f)
    #     counter += 1
    #     if(c == "/"):
    #         while True:
    #             c2 = nextChar(f)
    #             if(c2 != " " and (nextChar(f)) != None):
    #                pass
    #     else:
    #         outputBuffer.append(c)

    # lines = f.readlines()
    # for lines in enumerate(lines):
    #     line = lines.readline()
    #     if lines[0] != "/":
    #         outputBuffer.append(line)
        

    
    for lines in f:
        line = f.readline()
        if line[0] != "/":
            outputBuffer.append(line)

    return(outputBuffer)

def getChar(f):
    char = f[counter]
    return(char)

def nextChar(f):
    char = f[counter + 1]
    return(char)