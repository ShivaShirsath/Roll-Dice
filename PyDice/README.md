<h1 align=center>Roll Dice</h1>

> Console
```python
import random as r

while True:
    if 'x' in input("Roll Dice ( x for eXit) ? : "):
        exit(0)
    print((" ● "*r.randint(1, 6)).center(20)) # r.choice(["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]).center(28)
```
---
> Graphic
```python
import tkinter as tk, time as t, random as r

root = tk.Tk()

root.title('Roll Dice')
root.geometry('200x100')
root.eval('tk::PlaceWindow . center')

def getDice():
    t.sleep(1.5)
    b["text"]=(" ● "*r.randint(1, 6)).center(12) # r.choice(["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"])
    
b = tk.Button(root, text=root.title(), command=getDice)

b.pack(expand=True)

root.mainloop()
```
