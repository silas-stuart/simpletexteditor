import tkinter as tk
import tkinter.filedialog

root = tk.Tk()
root.title("Text Editor")

text = tk.Text(root)
text.pack(fill="both", expand=True)

def saveas():
    global text
    t = text.get("1.0", "end-1c")  # Get text content
    savelocation = tkinter.filedialog.asksaveasfilename()  # Open save dialog
    if savelocation:  # Check if user selected a file
        file1 = open(savelocation, "w+")
        file1.write(t)
        file1.close()

button = tk.Button(root, text="Save", command=saveas)
button.pack()

root.mainloop()

#This is the font editor
def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

font= tk.Menubutton(root, text="Font")
font.grid()
font.menu=tk.Menu(font, tearoff=0)