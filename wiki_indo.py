import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import messagebox

wikipedia.set_lang("id")
win = Tk()
win.title("Wiki Search")
win.configure(background="skyblue")

# Function
def clear():
    parts_list.delete("1.0", END)

def search_wiki(Event=None) :
    search = entry.get()
    if entry.get()=="":
        messagebox.showerror("Required Fields", "Harap di Isi")
        return
    answer = wikipedia.summary(search)
    # showinfo("Wikipedia Answer",answer)
    parts_list.insert("1.0","\n" + answer)

# Creating Label
label_name = Label(win, text="Created By\nFaishal Setiawan", fg="white",bg="#FF5939")
label_name.grid(row=0,column=0)


label = Label(win, text="Wikipedia Search: ", font=(10), bg="skyblue")
label.grid(row=0,column=0,columnspan=5,pady=(10,0))

# Creating Entry
entry = Entry(win,font=("italic",20))

entry.grid(row=1, column=0, columnspan=4, padx=10)

# Creating Button
button = Button(win, text="Search", command=search_wiki,font=(20), bg="#FF8017")
button.grid(row=1, column=3, padx=(0,10),pady=10)

button_clear = Button(win, text="Clear", command=clear,font=(20), bg="#FF4333", fg="white", padx=50)
button_clear.grid(row=8, column=0, columnspan=5)

#List
# Part list(List box)
parts_list = Text(win, height=20, width=61, border=0,padx=30,pady=30,font=15)
parts_list.grid(row=2, column=0, columnspan=4, rowspan=6, pady=10,padx=(35,0))
# Create Scrollbar
scrollbar = Scrollbar(win)
scrollbar.grid(row=2, column=4, rowspan=6)

# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# Run

win.geometry("810x690")
win.attributes("-alpha", 0.95)
win.resizable(False, False)
win.bind("<Return>", search_wiki)
win.mainloop()
