from tkinter import *

class Test(Frame):

    def __init__(self,window):
        super().__init__(window)
        self.grid()
        self.__init_widgets()

    def __init_widgets(self):
        self.__lb1 = Label(self, text = "1)Скільки буде 2+2*2? Відповідь дайте типом float")
        self.__lb1.grid(row=0, column=0, columnspan=4, sticky=W)

        self.__btn11 = Button(self, text="   6   ", command = self.__false1)
        self.__btn11.grid(row=1, column=0, sticky=W)

        self.__btn12 = Button(self, text="  6.0 ", command = self.__true1)
        self.__btn12.grid(row=1, column=1, sticky=W)

        self.__btn13 = Button(self, text="   8   ", command = self.__false1)
        self.__btn13.grid(row=1, column=2, sticky=W)

        self.__btn14 = Button(self, text="  8.0 ", command = self.__false1)
        self.__btn14.grid(row=1, column=3, sticky=W)

        self.__l1=Label(self, text=" ")
        self.__l1.grid(row=2, column=0, columnspan=4,sticky=W)

        self.__lbl2 = Label(self, text = " ")
        self.__lbl2.grid(row=3, column=0, columnspan=4, sticky=W)

        self.__lb2 = Label(self, text = "1)Скільки буде 2+2*2? Відповідь дайте типом float")
        self.__lb2.grid(row=4, column=0, columnspan=4, sticky=W)

        self.__btn21 = Button(self, text="   6   ", command = self.__false2)
        self.__btn21.grid(row=5, column=0, sticky=W)

        self.__btn22 = Button(self, text="  6.0 ",command = self.__true2)
        self.__btn22.grid(row=5, column=1, sticky=W)

        self.__btn23 = Button(self, text="   8   ", command = self.__false2)
        self.__btn23.grid(row=5, column=2, sticky=W)

        self.__btn24 = Button(self, text="  8.0 ", command = self.__false2)
        self.__btn24.grid(row=5, column=3, sticky=W)

        self.__l2=Label(self, text=" ")
        self.__l2.grid(row=6, column=0, columnspan=4,sticky=W)

        self.__lbl3 = Label(self, text = " ")
        self.__lbl3.grid(row=7, column=0, columnspan=4, sticky=W)

        self.__lb3 = Label(self, text = "1)Скільки буде 2+2*2? Відповідь дайте типом float")
        self.__lb3.grid(row=8, column=0, columnspan=4, sticky=W)

        self.__btn31 = Button(self, text="   6   ", command = self.__false3)
        self.__btn31.grid(row=9, column=0, sticky=W)

        self.__btn32 = Button(self, text="  6.0 ",command = self.__true3)
        self.__btn32.grid(row=9, column=1, sticky=W)

        self.__btn33 = Button(self, text="   8   ", command = self.__false3)
        self.__btn33.grid(row=9, column=2, sticky=W)

        self.__btn34 = Button(self, text="  8.0 ", command = self.__false3)
        self.__btn34.grid(row=9, column=3, sticky=W)

        self.__l3=Label(self, text=" ")
        self.__l3.grid(row=10, column=0, columnspan=4,sticky=W)

       

    def __true1(self):
        self.__l1["text"]="True"

    def __false1(self):
        self.__l1["text"]="False"

    def __true2(self):
        self.__l2["text"]="True"

    def __false2(self):
        self.__l2["text"]="False"

    def __true3(self):
        self.__l3["text"]="True"

    def __false3(self):
        self.__l3["text"]="False"
        
        




if __name__ == "__main__":
    main_window=Tk()

main_window.title("Test")
main_window.geometry("800x600")

test = Test(main_window)
main_window.mainloop()
        
        
