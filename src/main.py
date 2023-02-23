import tokenizer as tk

if __name__ == "__main__":
    file = input("What file would you like to read: ")
    if(file == "SquareGame.jack"):
       f = tk.readFile(file)
       print(f)
    elif(file == "Main.jack"):
      #  f = tk.readFile(file)
      #  print("<tokens>")
      #  tk.lex(f)
      #  print("</tokens>")
      # print(f)
      print("<Tokens>")
      tk.lex(file)
      print("</Tokens>")
    else:
        print("File does not exist, shutting down now!")