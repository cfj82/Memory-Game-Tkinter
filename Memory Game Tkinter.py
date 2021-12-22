# memory game with tkinter

import tkinter as tk
import random

root = tk.Tk()
root.title("Memory Game")
root.geometry("470x550")
root.configure(background='black')

# list of matches behind cards
matches = [1,1,2,2,3,3,4,4,5,5,6,6]
random.shuffle(matches)

# keep track of what clicked
answer_list = []
answer_dict = {}
count = 0
correct = 0


def reset():
    global correct, matches
    correct = 0
    matches = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
    random.shuffle(matches)
    status_lbl.config(text="")

    button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    for button in button_list:
        button.config(text=" ", state="normal", bg="#5DADE2")


def win():
    status_lbl.config(text="You Win!")
    # change color of buttons
    button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    for button in button_list:
        button.config(bg="gray", )


def button_click(b, number):
    global count, correct, answer_list, answer_dict
    if b["text"] == " " and count < 2:  # if b[text] = nothing/blank
        # show number when matched
        b["text"] = matches[number]
        # add match to answer list
        answer_list.append(number)
        # set button as dict key
        answer_dict[b] = matches[number]
        count = count + 1

    # determine if correct
    elif len(answer_list) == 2:  # if two answers in answer_list
        if matches[answer_list[0]] == matches[answer_list[1]]:
            status_lbl.config(text='Match!')
            # disable button
            for key in answer_dict:  # key is from dict key match
                key["state"] = "disabled"
            count = 0  # reset count
            answer_dict = {}
            answer_list = []
            correct +=1
            if correct == 6:
                win()
        # wrong match
        else:
            count = 0
            answer_list = []
            for key in answer_dict:
                key["text"] = " "
            answer_dict = {}



# frames
f0 = tk.Frame(root, bg="#000000")  # for buttons
f0.pack(pady=10)
f1 = tk.Frame(root, bg="#000000")  # for label
f1.pack(pady=10)
f2 = tk.Frame(root, bg="#000000")  # for label
f2.pack(pady=8)

# buttons
b0 = tk.Button(f0, text=' ', font=("Helvetica", 20), border=5,
                 bg="#5DADE2", height=3, width=6, relief='groove', command=lambda: button_click(b0,0))
b1 = tk.Button(f0, text=' ', font=("Helvetica", 20), border=5,
                 bg="#5DADE2", height=3, width=6, relief='groove', command=lambda: button_click(b1,1))
b2 = tk.Button(f0, text=' ', font=("Helvetica", 20), border=5,
                 bg="#5DADE2", height=3, width=6, relief='groove', command=lambda: button_click(b2,2))
b3 = tk.Button(f0, text=' ', font=("Helvetica", 20), border=5,
                 bg="#5DADE2", height=3, width=6, relief='groove', command=lambda: button_click(b3,3))


b4 = tk.Button(f0, text=' ', font=("Helvetica", 20), border=5,
                 bg="#5DADE2", height=3, width=6, relief='groove', command=lambda: button_click(b4,4))
b5 = tk.Button(f0, text=' ', font=("Helvetica", 20), border=5,
                 bg="#5DADE2", height=3, width=6, relief='groove', command=lambda: button_click(b5,5))
b6 = tk.Button(f0, text=' ', font=("Helvetica", 20), border=5,
                 bg="#5DADE2", height=3, width=6, relief='groove', command=lambda: button_click(b6,6))
b7 = tk.Button(f0, text=' ', font=("Helvetica", 20), border=5,
                 bg="#5DADE2", height=3, width=6, relief='groove', command=lambda: button_click(b7,7))


b8 = tk.Button(f0, text=' ', font=("Helvetica", 20), border=5,
                 bg="#5DADE2", height=3, width=6, relief='groove', command=lambda: button_click(b8,8))
b9 = tk.Button(f0, text=' ', font=("Helvetica", 20), border=5,
                 bg="#5DADE2", height=3, width=6, relief='groove', command=lambda: button_click(b9,9))
b10 = tk.Button(f0, text=' ', font=("Helvetica", 20), border=5,
                 bg="#5DADE2", height=3, width=6, relief='groove', command=lambda: button_click(b10,10))
b11 = tk.Button(f0, text=' ', font=("Helvetica", 20), border=5,
                 bg="#5DADE2", height=3, width=6, relief='groove', command=lambda: button_click(b11,11))


b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

# status label
status_lbl = tk.Label(f1, font=("verdana", 20), anchor="center", relief='flat', border=15,
            bg="#5DADE2", width=20, text="")
status_lbl.pack(side='top')

start_button = tk.Button(f2, text='Start', font=("Helvetica", 12), border=5,
                 bg="#5DADE2", height=2, width=18, relief='groove', command=lambda: reset())
start_button.pack(side='bottom')


# create menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)
# create dropdown
option_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu = option_menu)  # create function for menu
option_menu.add_command(label = "Reset", command = reset)

option_menu.add_separator()        # adds line to separate

option_menu.add_command(label = "Quit", command = root.quit)


root.mainloop()
