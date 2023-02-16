import tokenizer as tk

if __name__ == "__main__":
    file = input("What file would you like to read: ")
    if(file == "SquareGame.jack"):
        tk.readFile(file)
    else:
        print("File does not exist, shutting down now!")