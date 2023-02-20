import tokenizer as tk

if __name__ == "__main__":
    file = input("What file would you like to read: ")
    if(file == "SquareGame.jack"):
       f = tk.readFile(file)
       print(f)
    elif(file == "Main.jack"):
       f = tk.readFile(file)
       tk.lex(f)

    else:
        print("File does not exist, shutting down now!")