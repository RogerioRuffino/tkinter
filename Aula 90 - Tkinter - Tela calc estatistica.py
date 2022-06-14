def select(value):
    if value == "Space":
        entry1.insert(tkinter.END, ' ')
    elif value == "Backspace":
        entry1.delete(len(entry1.get())-1,tkinter.END)
    else:
        entry1.insert(tkinter.END, value)

    root = Tk()
    root.configure(background = "cornflowerblue")
    root.wm_attributes("-alpha", 0.7)

    alphabets = ['`','1','2','3','4','5','6','7','8','9','0','-','=','<- 
       Backspace',
            'Tab','q','w','e','r','t','y','u','i','o','p','[',']',"\\",
            'Caps Lock','a','s','d','f','g','h','j','k','l',';',"'",'Enter',
            'Shift','z','x','c','v','b','n','m',',','.','/','Shift',
             'Space']
    Row = 2
    Column = 0

    for alphabet in alphabets:
    command = lambda x=alphabet: select(x)
    if alphabet != 'Space':
        Button(root, text = alphabet,
               command = command,width = 5, padx=3, pady=3,bd=12,bg = "black", fg="white").grid(row = Row, column = Column)
    if alphabet == 'Enter':
        Button(root, text = alphabet,
               command = command, width = 15, padx=3, pady=3,bd=12,bg = "black", fg="white").grid(row = Row, column = Column, columnspan = 2)
    if alphabet == 'Shift':
        Button(root, text = alphabet,
               command = command, width = 15, padx=3, pady=3,bd=12,bg = "black", fg="white").grid(row = Row, column = Column, columnspan = 2)    
    if alphabet == 'Space':
        Button(root, text = alphabet,
               command = command, width = 130, padx=3, pady=3,bd=12,bg = "black", fg="white").grid(row = 6, columnspan = 16)

    Column +=1
    if Column > 13 and Row == 1:
        Column = 0
        Row += 1
    if Column > 13 and Row == 2:
        Column = 0
        Row +=1
    if Column > 13 and Row == 3:
        Column = 0
        Row +=1
    if Column > 12 and Row == 4:
        Column = 0
        Row +=1
