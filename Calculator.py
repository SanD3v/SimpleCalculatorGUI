from tkinter import *

root = Tk()
root.title('Calculator')

for i in range(1):
    root.columnconfigure(i, weight=1, minsize=75)
root.rowconfigure(i, weight=1, minsize=75)
ROW = 0
COLUMN = 0
INDEX = 0
NUM1 = 0
NUM2 = 0
OP = None
entryField = Entry(root, text='Enter Input', bg='#505050', fg='black', width=32, borderwidth=10)
entryField.grid(row=3, column=0, columnspan=3)
frm = Frame(root)


def createButtton(k):
    global ROW
    global COLUMN
    Button(frm, text=k, fg='black', bg='#505050', padx=30, pady=25,font='bold', borderwidth=10, command=lambda: buttonClick(k)).grid(
        row=ROW,
        column=COLUMN)
    COLUMN += 1
    if COLUMN == 3:
        COLUMN = 0
        ROW += 1


def buttonClick(k):
    global NUM1
    global NUM2
    global OP
    if k == '+':
        OP = 0
        NUM1 = int(entryField.get())
        entryField.delete(0, 10)
    elif k == '-':
        OP = 1
        NUM1 = int(entryField.get())
        entryField.delete(0, 10)
    elif k == 'x':
        OP = 2
        NUM1 = int(entryField.get())
        entryField.delete(0, 10)
    elif k == '/':
        OP = 3
        NUM1 = int(entryField.get())
        entryField.delete(0, 10)
    elif k == '%':
        OP = 4
        NUM1 = int(entryField.get())
        entryField.delete(0, 10)

    elif k == '=':
        NUM2 = int(entryField.get())
        entryField.delete(0, 10)
        if OP == 0:
            entryField.insert(0, str(NUM1 + NUM2))
        elif OP == 1:
            entryField.insert(0, str(NUM1 - NUM2))
        elif OP == 2:
            entryField.insert(0, str(NUM1 * NUM2))
        elif OP == 3:
            entryField.insert(0, str(NUM1 / NUM2))
        elif OP == 4:
            entryField.insert(0, str(NUM1 % NUM2))
    elif k == 'C':
        entryField.delete(0, 10)
    elif k == 'E':
        exit()

    else:
        global INDEX
        entryField.insert(INDEX, k)
        INDEX += 1


buttonList = list(range(10)) + ['+', '-', '=', 'C', 'x', '/', '%', 'E']
for i in buttonList:
    createButtton(str(i))
frm.grid(row=0, column=0, columnspan=3)

mainloop()
