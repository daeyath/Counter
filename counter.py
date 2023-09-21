from tkinter import Tk, Label, Button, font

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title_label = Label(self, text="Counter", font=("Arial",15))
        self.title_label.pack()
        self.label_font=font.Font(size="24")
        self.label = Label(self, text="0", font=("Arial",50))
        self.label.pack(pady=100)
        self.button = Button(self, text="Next", command=self.count, height=6, width=15, font=("Arial",12))
        self.button.pack(pady=100)
        self.resetbtn=Button(self, text="Reset", command=self.reset)
        self.resetbtn.pack()
        
    def count(self):
    	data=int(self.label["text"])
    	data+=1
    	self.label["text"]=str(data)
    	
    def reset(self):
    	self.label["text"]="0"

root = Root()
root.mainloop()