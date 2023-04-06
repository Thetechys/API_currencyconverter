import tkinter as tk


dimension = xwidth, yheight = 800,400


root = tk.Tk()
root.geometry(f"{int(xwidth)}x{int(yheight)}")
# frame = tk.Frame(root)
# frame.pack()


var = tk.StringVar()
var2 = tk.StringVar()
choices = ['SGD','MYR','USD']
#choices2 = ['JPY','BAHT','WON']

def selected_from_curr(*args):
    print(f"FROM currency: {var.get()}")


def selected_to_curr(*args):
    print(f"TO currency: {var2.get()}")

def reset():
    var.set('')
    var2.set('')

var.trace("w",selected_from_curr)
var2.trace("w",selected_to_curr)

## 800 x 400 (xwidth x yheight)

dropdown_menu = tk.OptionMenu(root,var,*choices)
dropdown_menu.config(width=5)
dropdown_menu.grid(row=2,column=1)

dropdown_menu2 = tk.OptionMenu(root,var2,*choices)
dropdown_menu2.config(width=5)
dropdown_menu2.grid(row=2,column=3)

text_entry = tk.Entry(root,width=15)
text_entry.grid(row=2,column=2)


reset_button = tk.Button(root, text='Reset',command=reset)
reset_button.grid(row=3,column=2)

out_label = tk.Label(root,text='output')
# out_label.config(width=5)
out_label.grid(row=0,column=0)









root.mainloop()