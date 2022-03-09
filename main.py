#Simple 2-way caesar cipher with GUI
from tkinter import *

root = Tk()
root.title("CCipher")
root.geometry("340x80")
root.resizable(False, False)

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
newstring = ''

def encodeString(string, key):
    global newstring
    print("Encoding..." + string + " with key of " + key)

    #Encoding logic
    for letter in string.upper(): 
        if letter in letters: 
            num = int(letters.find(letter)) + int(key) 

            if num >= len(letters):
                num = num - len(letters)
            elif num < 0:
                num = num + len(letters)

            newstring = newstring + letters[num]
        else:
            newstring = newstring + letter

    output.insert(0, newstring)
    newstring = ''
    num = 0

def decodeString(string, key):
    global newstring
    print("Decoding..." + string + " with key of " + key)

    #Decoding logic
    for letter in string.upper():
        if letter in letters:
            num = int(letters.find(letter)) - int(key)

            if num >= len(letters):
                num = num - len(letters)
            elif num < 0:
                num = num + len(letters)

            newstring = newstring + letters[num]
        else:
            newstring = newstring + letter

    output.insert(0, newstring)
    newstring = ''
    num = 0

def clearOutput():
    output.delete(0, END)

#GUI
lblText = Label(root, text="String")
lblText.grid(row=0, column=0)
entryText = Entry(root, width=30)
entryText.grid(row=0, column=1)
lblKey = Label(root, text="Key")
lblKey.grid(row=1, column=0)
entryKey = Entry(root, width=30)
entryKey.grid(row=1, column=1)
entryKey.insert(0, "0")
btnEncode = Button(root, text="Encode", command=lambda:[clearOutput(), encodeString(entryText.get(), entryKey.get())])
btnEncode.grid(row=0, column=2)
btnDecode = Button(root, text="Decode", command=lambda:[clearOutput(), decodeString(entryText.get(), entryKey.get())])
btnDecode.grid(row=0, column=3)
lblOutput = Label(root, text="Result")
lblOutput.grid(row=2, column=0)
output = Entry(root, width=30)
output.grid(row=2, column=1)


root.mainloop()