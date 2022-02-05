from tkinter import *

root = Tk()
root.geometry("300x300")
root.configure(bg="#141414")

def button_animation(x,y,fcolor,bcolor,cmd,text):

    def on_entry(e):
        test_button['background']=bcolor
        test_button['foreground']=fcolor

    def out_entry(e):
        test_button['background']=fcolor
        test_button['foreground']=bcolor

    test_button = Button(root,width=42,height=2,text=text,
                        fg=bcolor,
                        bg=fcolor,
                        border=0,
                        activeforeground=fcolor,
                        activebackground=bcolor,
                        command=None
                        )

    test_button.bind('<Enter>', on_entry)
    test_button.bind('<Leave>', out_entry)
    test_button.place(x=x,y=y)

button_animation(0,0,"#141414","pink",None,"Button")
root.mainloop()