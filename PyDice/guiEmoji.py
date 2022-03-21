import tkinter as tk, time as t, random as r

root = tk.Tk()

root.title('Roll Dice')
root.geometry('200x100')
root.eval('tk::PlaceWindow . center')

def getDice():
    t.sleep(1.5)
    b["text"]=r.choice(["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"])
    
b = tk.Button(root, text=root.title(), command=getDice)
b.pack(expand=True)

root.mainloop()
