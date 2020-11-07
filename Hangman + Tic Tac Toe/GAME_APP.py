import tkinter as tk
import hangman
import playgame
class GAME_APP(tk.Tk):

    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container=tk.Frame(self)
        

        container.pack(side='top',fill='both',expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        F=StartPage

        frame = F(container, self)

        self.frames[F] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="GAME APP", font=('Ravie',50,'bold italic'),fg='Dark Blue',bg='Light Pink',padx=20,pady=10,justify='center')
        label.grid(padx=80,pady=50)
        #self.grid_columnconfigure(1,weight=1)
        #self.grid_rowconfigure(1,weight=1)

        #button = tk.Button(self, text="Tic Tac Toe",bg='Light Green',fg='Purple',bd=8,justify='center',font=('Broadway',18,'bold italic'),command=lambda: controller.show_frame(TicTacToe))
        button = tk.Button(self, text="Tic Tac Toe",bg='Light Green',fg='Purple',bd=8,justify='center',font=('Broadway',18,'bold italic'),command=self.TTT)
        button.grid(padx=30,pady=30)

        #button2 = tk.Button(self, text="Hangman",bg='Light Green',fg='Purple',bd=8,justify='center',font=('Broadway',18,'bold italic'),command=lambda: controller.show_frame(Hangman))
        button2 = tk.Button(self, text="Hangman",bg='Light Green',fg='Purple',bd=8,justify='center',font=('Broadway',18,'bold italic'),command=self.hangman_win)
        button2.grid(padx=30,pady=30)
        
    def hangman_win(self):
        bb=hangman.mainwindow()
        
    def TTT(self):
        tt=playgame.GUI()



class TicTacToe(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Tic Tac Toe", font=('Ravie',50,'bold italic'),padx=20,pady=10,justify='center')
        label.grid(padx=30,pady=30,row=1)

        button1 = tk.Button(self, text="Back to Home",bd=5,relief='raised',bg='Pink',justify='center',font=('Comic San MS',10,'italic'),command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0,column=0,sticky='w')

        

class Hangman(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hangman",font=('Ravie',50,'bold italic'),padx=20,pady=10,justify='center')
        label.grid(padx=30,pady=30,row=1,column=1)

        button1 = tk.Button(self, text="Back to Home",bd=5,relief='raised',bg='Pink',justify='center',font=('Comic San MS',10,'italic'),command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0,column=0,sticky='w')

        
        



app=GAME_APP()
app.title('Game App')
app.geometry('700x500')
app.mainloop()
