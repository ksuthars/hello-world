from tkinter import *
import GUI_Test
import lift_test

def call_gui1():
    win1 = tk.Tk() 
    gui1= GUI_Test.GUI(win1)
    gui1.pack(fill="both",expand=true)
    
    
def call_gui2():
    win2 = tk.Toplevel(win1)
    gui2=lift_test.GUI(win2)
    gui2.pack(fill="both",expand=true)

if  __name__== '__main__':
     root = Tk()
     root.title('Caller Gui')
     root.minsize(720,600)
     button_1 = Button(root, text ='call gui1', width='20', height = '20', command =call_gui1)
     button_1.pack()
     button_2 = Button(root, text ='call gui2', width='20', height = '20', command =call_gui2)
     button_2.pack()
     root.mainloop()
     
    