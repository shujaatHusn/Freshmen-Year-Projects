import tkinter as tk

LARGE_FONT = ("Verdana", 30, 'bold')


# framework for multiple windows
class mainwindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('HANGMAN')

        # This container contains all pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # these are pages we want to navigate to
        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):  # for each page
            frame = F(container, self)  # create the page
            self.frames[F] = frame  # store into frames
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)  # let the first page be StartPage

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # this command raises that frame to the top


class StartPage(tk.Frame):
    # initialing guess left to be used in making hangman
    guesses_left = 6
    #initialising no. of correct guesses so that we can proceed to next level after correctly guessing word
    correct_guess = 8

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # gui features
        label = tk.Label(self, text="WELCOME TO HANGMAN!This is level 1:EASY", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text="Enter your guesses in the box below(make sure caps lock is turned off)", font='times 20')
        label.pack()



        # initialising canvas for drawing hangman
        self.canvas = tk.Canvas(self, width=500, height=600)
        self.canvas.pack(side='right')



        line1 = self.canvas.create_line(300, 150, 450, 50)
        line2 = self.canvas.create_line(450, 50, 450, 550)

        self.ansbox = tk.Entry(self,width=6, font="Times 30 bold", bg="white", borderwidth=2, relief="solid")
        self.ansbox.pack(side='top')
        self.ansbox.focus()

        v = tk.StringVar()

        self.textbox1 = tk.Label(self,width=4, font="Times 20 bold", bg="yellow", textvariable=v, state='disabled',
                                 borderwidth=2, relief="groove")
        self.textbox1.pack(side='left')
        v.set('p')

        self.textbox2 = tk.Label(self,width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox2.pack(side='left')

        self.textbox3 = tk.Label(self,width=4, font="times 20 bold", bg="yellow", textvariable=v, state='disabled',
                                 borderwidth=2, relief="groove")
        self.textbox3.pack(side='left')
        v.set('p')

        self.textbox4 = tk.Label(self,width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox4.pack(side='left')

        self.textbox5 = tk.Label(self,width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox5.pack(side='left')

        self.textbox6 = tk.Label(self,width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox6.pack(side='left')

        self.textbox7 = tk.Label(self,width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox7.pack(side='left')

        self.textbox8 = tk.Label(self,width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox8.pack(side='left')

        self.textbox9 = tk.Label(self,width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox9.pack(side='left')

        self.textbox10 = tk.Label(self,width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox10.pack(side='left')

        # command for exit button is left
        self.exitbutton = tk.Button(self, padx=1, pady=1, text='EXIT GAME', font="times 20 bold", fg='white',
                                    bg="red", borderwidth=15)#,command=exit)
        self.exitbutton.pack(side='bottom')

        self.enterbutton = tk.Button(self, padx=1, pady=1, text='ENTER', font="times 20 bold",
                                     bg="green", fg="white", borderwidth=15,
                                     command=lambda: self.enter(parent, controller))
        self.enterbutton.pack(side='top')

        #self.nextlevelbutton = tk.Button(self, text="NEXT LEVEL", command=lambda: controller.show_frame(PageOne),
         #                                state='disabled', font="times 20 bold", borderwidth=15,bg='white',fg='green')
        #self.nextlevelbutton.pack()

        self.invisible = tk.Label()#to save repeated letters

        #label showing incorrect entries
        self.wrong = tk.Label(self,width=8,font='20',bg='white', borderwidth=2, relief="groove")
        self.wrong.pack(side='bottom')

        # a dictionary that maps the textboxes to their respective correct answers
        self.answers = {'o': self.textbox2, 'u': self.textbox4, 'l': self.textbox5, 'a': self.textbox6,
                        't': self.textbox7, 'i': self.textbox8, 'o': self.textbox9, 'n': self.textbox10}
        self.l = []#initialising list to add correct answers of players so that they aren't counted as a correct
                    #answer if players enters them repaeatedly


        self.dupe = {'o': self.textbox2} #for duplicates

    # comparing letters
    def enter(self, parent, controller):
        ans = str(self.ansbox.get())
        if ans != '':
            if ans in 'oulation':
                self.ansbox.delete(0, 'end')
                # it'll search for 'o' in the dictionary and access its value which happens to be a textbox so the answer
                #  which the players enters is displayed as the text of the textbox
                self.answers[ans]['text'] = ans
                # works exactly like above statement except that when there is no key, adds answer to an invisible textbox
                self.dupe.get(ans, self.invisible)['text'] = ans
                self.correctans = ans
                self.repeated(parent, controller)
            else:
                self.ansbox.delete(0, 'end')
                text = self.wrong.cget("text") + ans
                self.wrong.configure(text=text)
                self.hangman(parent, controller)
                self.popupmsg2()

    # repeated correct entries
    def repeated(self, parent, controller):
        if self.correctans not in self.l:
            self.l.append(self.correctans)
            self.correctguess(parent, controller)
            self.popupmsg()


        else:
            w = tk.Tk()
            label = tk.Label(w, text="you already guessed that!make a new guess", font='times 30',
                             fg='blue')
            label.pack()
            w.after(2000, lambda: w.destroy())
            w.mainloop()

    # creating parts of hangman on incorrect guesses
    def hangman(self, parent, controller):
        StartPage.guesses_left = StartPage.guesses_left - 1
        if self.guesses_left == 5:
            oval = self.canvas.create_oval(250, 150, 350, 250, fill='brown')
        elif self.guesses_left == 4:
            line = self.canvas.create_line(300, 250, 300, 400, fill='brown')
        elif self.guesses_left == 3:
            line = self.canvas.create_line(300, 300, 230, 350, fill='brown')
        elif self.guesses_left == 2:
            line = self.canvas.create_line(300, 300, 370, 350, fill='brown')
        elif self.guesses_left == 1:
            line = self.canvas.create_line(300, 400, 250, 450, fill='brown')
        elif self.guesses_left == 0:
            line = self.canvas.create_line(300, 400, 350, 450, fill='brown')
            w = tk.Tk()
            label = tk.Label(w, text="WHOOPS!YOU'RE OUT OF GUESSES!"
                                     "IM AFRAID YOU CAN'T PROCEED:(", font='times 30', fg='red')
            label.pack()
            B1 = tk.Button(w, text="Okay") #, command=exit)
            B1.pack()
            w.mainloop()

    def correctguess(self, parent, controller):
        StartPage.correct_guess -= 1
        #print(StartPage.correct_guess)

        if StartPage.correct_guess == 1:
            w = tk.Tk()
            label = tk.Label(w, text='''GREAT JOB!YOU CAN NOW PROCEED TO THE NEXT LEVEL!
                        FYI>>>DEFINITION OF POPULATION:
                        all the inhabitants of a particular place''', font='times 30', fg='purple')
            label.pack()
            B1 = tk.Button(w, text="Got it, thanks!", font='20', command=lambda: controller.show_frame(PageOne) or w.destroy())
            B1.pack()


            #self.nextlevelbutton.config(state='normal')
            w.mainloop()


    # popup msg for correct entry
    def popupmsg(self):

        w = tk.Tk()
        label = tk.Label(w, text='That is correct! :D', font='times 30', fg='green')
        label.pack()
        w.after(2000, lambda: w.destroy())  # Destroy the widget after 2 seconds
        w.mainloop()
        return

    # popup for incorrect entry
    def popupmsg2(self):
        w = tk.Tk()
        label = tk.Label(w, text="That is incorrect", font='times 30', fg='red')
        label.pack()
        w.after(2000, lambda: w.destroy())  # Destroy the widget after 2 seconds
        w.mainloop()


class PageOne(tk.Frame):
    # initialing guess left to be used in making hangman
    guesses_left = 6
    # initialising no. of correct guesses so that we can proceed to next level after correctly guessing word
    correct_guess = 6

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="LEVEL 2:INTERMEDIATE", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text="Enter your guesses in the box below(make sure caps lock is turned off)",
                         font='times 20')
        label.pack()

        #button1 = tk.Button(self, text="PREVIOUS LEVEL",command=lambda: controller.show_frame(StartPage))
        #button1.pack()



        # initialising canvas for drawing hangman
        self.canvas = tk.Canvas(self, width=500, height=600)
        self.canvas.pack(side='right')

        # label = self.canvas.create_text(200, 560, fill="blue", font="times 15 bold", text="Enter your guesses below!")

        line1 = self.canvas.create_line(300, 150, 450, 50)
        line2 = self.canvas.create_line(450, 50, 450, 550)

        self.ansbox = tk.Entry(self, width=6, font="Times 30 bold", bg="white", borderwidth=2, relief="solid")
        self.ansbox.pack(side='top')
        self.ansbox.focus()

        v = tk.StringVar()

        self.textbox1 = tk.Label(self, width=4, font="Times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox1.pack(side='left')

        self.textbox2 = tk.Label(self, width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox2.pack(side='left')

        self.textbox3 = tk.Label(self, width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox3.pack(side='left')

        self.textbox4 = tk.Label(self, width=4, font="times 20 bold", bg="yellow",textvariable=v, state='disabled',
                                 borderwidth=2, relief="groove")
        self.textbox4.pack(side='left')
        v.set('m')

        self.textbox5 = tk.Label(self, width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox5.pack(side='left')

        self.textbox6 = tk.Label(self, width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox6.pack(side='left')

        self.textbox7 = tk.Label(self, width=4, font="times 20 bold", bg="yellow",  textvariable=v, state='disabled',
                                 borderwidth=2, relief="groove")
        self.textbox7.pack(side='left')
        v.set('m')





        # command for exit button is left
        self.exitbutton = tk.Button(self, padx=1, pady=1, text='EXIT GAME', font="times 20 bold", fg='white', bg="red",
                                    borderwidth=15) #, command=exit)
        self.exitbutton.pack(side='bottom')

        self.enterbutton = tk.Button(self, padx=1, pady=1, text='ENTER', font="times 20 bold", bg="green", fg="white",
                                     borderwidth=15, command=lambda: self.enter(parent, controller))
        self.enterbutton.pack(side='top')

        #self.nextlevelbutton = tk.Button(self, text="NEXT LEVEL", command=lambda: controller.show_frame(PageTwo),
        #                                 state='disabled', font="times 20 bold", borderwidth=15, bg='white',fg='green')
        #self.nextlevelbutton.pack()

        self.invisible = tk.Label()  # to save repeated letters

        # label showing incorrect entries
        self.wrong = tk.Label(self, width=8, font='20', bg='white', borderwidth=2, relief="groove")
        self.wrong.pack(side='bottom')

        # a dictionary that maps the textboxes to their respective correct answers
        self.answers = {'p': self.textbox1, 'r': self.textbox2, 'e': self.textbox3, 'i': self.textbox5,
                        'u': self.textbox6}
        self.l = []  # initialising list to add correct answers of players so that they aren't counted as a correct
        # answer if players enters them repaeatedly



        # comparing letters

    def enter(self, parent, controller):
        ans = str(self.ansbox.get())
        if ans != '':
            if ans in 'preiu':
                self.ansbox.delete(0, 'end')
                # it'll search for 'o' in the dictionary and access its value which happens to be a textbox so the answer
                #  which the players enters is displayed as the text of the textbox
                self.answers[ans]['text'] = ans

                self.correctans = ans
                self.repeated(parent, controller)
            else:
                self.ansbox.delete(0, 'end')
                text = self.wrong.cget("text") + ans
                self.wrong.configure(text=text)
                self.hangman(parent, controller)
                self.popupmsg2()

        # repeated correct entries

    def repeated(self, parent, controller):
        if self.correctans not in self.l:
            self.l.append(self.correctans)
            self.correctguess(parent, controller)
            self.popupmsg()


        else:
            w = tk.Tk()
            label = tk.Label(w, text="you already guessed that!make a new guess", font='times 30', fg='blue')
            label.pack()
            w.after(2000, lambda: w.destroy())
            w.mainloop()

        # creating parts of hangman on incorrect guesses

    def hangman(self, parent, controller):
        PageOne.guesses_left = PageOne.guesses_left - 1
        print(PageOne.guesses_left)
        if self.guesses_left == 5:
            oval = self.canvas.create_oval(250, 150, 350, 250, fill='brown')
        elif self.guesses_left == 4:
            line = self.canvas.create_line(300, 250, 300, 400, fill='brown')
        elif self.guesses_left == 3:
            line = self.canvas.create_line(300, 300, 230, 350, fill='brown')
        elif self.guesses_left == 2:
            line = self.canvas.create_line(300, 300, 370, 350, fill='brown')
        elif self.guesses_left == 1:
            line = self.canvas.create_line(300, 400, 250, 450, fill='brown')
        elif self.guesses_left == 0:
            line = self.canvas.create_line(300, 400, 350, 450, fill='brown')
            w = tk.Tk()
            label = tk.Label(w, text="WHOOPS!YOU'RE OUT OF GUESSES!"
                                     "IM AFRAID YOU CAN'T PROCEED:(", font='times 30', fg='red')
            label.pack()
            B1 = tk.Button(w, text="Okay") #, command=exit)
            B1.pack()
            w.mainloop()

    def correctguess(self, parent, controller):
        PageOne.correct_guess -= 1
        print(PageOne.correct_guess)

        if PageOne.correct_guess == 1:
            w = tk.Tk()
            label = tk.Label(w, text='''YOU DID IT!NOW IT'S TIME FOR A TOUGH ONE!
                        FYI>>>DEFINITION OF PREMIUM:
                        something given as a reward, prize, or incentive''', font='times 30', fg='purple')
            label.pack()
            B1 = tk.Button(w, text="Got it, thanks!", font='20',command=lambda: controller.show_frame(PageTwo) or w.destroy())
            B1.pack()

           # self.nextlevelbutton.config(state='normal')
            w.mainloop()


        # popup msg for correct entry

    def popupmsg(self):

        w = tk.Tk()
        label = tk.Label(w, text='That is correct! :D', font='times 30', fg='green')
        label.pack()
        w.after(2000, lambda: w.destroy())  # Destroy the widget after 2 seconds
        w.mainloop()
        return

        # popup for incorrect entry

    def popupmsg2(self):
        w = tk.Tk()
        label = tk.Label(w, text="That is incorrect", font='times 30', fg='red')
        label.pack()
        w.after(2000, lambda: w.destroy())  # Destroy the widget after 2 seconds
        w.mainloop()


class PageTwo(tk.Frame):
    # initialing guess left to be used in making hangman
    guesses_left = 6
    # initialising no. of correct guesses so that we can proceed to next level after correctly guessing word
    correct_guess = 9

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="LEVEL 3:PROFESSIONAL", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text="Enter your guesses in the box below(make sure caps lock is turned off)",
                         font='times 20')
        label.pack()



        # initialising canvas for drawing hangman
        self.canvas = tk.Canvas(self, width=500, height=600)
        self.canvas.pack(side='right')

        # label = self.canvas.create_text(200, 560, fill="blue", font="times 15 bold", text="Enter your guesses below!")

        line1 = self.canvas.create_line(300, 150, 450, 50)
        line2 = self.canvas.create_line(450, 50, 450, 550)

        self.ansbox = tk.Entry(self, width=6, font="Times 30 bold", bg="white", borderwidth=2, relief="solid")
        self.ansbox.pack(side='top')
        self.ansbox.focus()

        v = tk.StringVar()

        self.textbox1 = tk.Label(self, width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox1.pack(side='left')

        self.textbox2 = tk.Label(self, width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox2.pack(side='left')

        self.textbox3 = tk.Label(self, width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox3.pack(side='left')

        self.textbox4 = tk.Label(self, width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox4.pack(side='left')

        self.textbox5 = tk.Label(self, width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox5.pack(side='left')

        self.textbox6 = tk.Label(self, width=4, font="Times 20 bold", bg="yellow", textvariable=v, state='disabled',
                                 borderwidth=2, relief="groove")
        self.textbox6.pack(side='left')
        v.set('e')

        self.textbox7 = tk.Label(self, width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox7.pack(side='left')

        self.textbox8 = tk.Label(self, width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox8.pack(side='left')

        self.textbox9 = tk.Label(self, width=4, font="Times 20 bold", bg="yellow", textvariable=v, state='disabled',
                                 borderwidth=2, relief="groove")
        self.textbox9.pack(side='left')
        v.set('e')

        self.textbox10 = tk.Label(self, width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox10.pack(side='left')

        self.textbox11 = tk.Label(self, width=4, font="times 20 bold", bg="yellow", borderwidth=2, relief="groove")
        self.textbox11.pack(side='left')

        # command for exit button is left
        self.exitbutton = tk.Button(self, padx=1, pady=1, text='EXIT GAME', font="times 20 bold", fg='white', bg="red",
                                    borderwidth=15) #, command=exit)
        self.exitbutton.pack(side='bottom')

        self.enterbutton = tk.Button(self, padx=1, pady=1, text='ENTER', font="times 20 bold", bg="green", fg="white",
                                     borderwidth=15, command=lambda: self.enter(parent, controller))
        self.enterbutton.pack(side='top')

        # label showing incorrect entries
        self.wrong = tk.Label(self, width=8, font='20', bg='white', borderwidth=2, relief="groove")
        self.wrong.pack(side='bottom')



        self.invisible = tk.Label()  # to save repeated letters

        # a dictionary that maps the textboxes to their respective correct answers
        self.answers = {'c': self.textbox1, 'o': self.textbox2, 'u': self.textbox3, 'n': self.textbox4,
                        't': self.textbox5, 'r': self.textbox7, 'f': self.textbox8, 'i': self.textbox10,'t': self.textbox11}
        self.l = []  # initialising list to add correct answers of players so that they aren't counted as a correct
        # answer if players enters them repaeatedly

        self.dupe = {'t': self.textbox5}  # for duplicates

        # comparing letters

    def enter(self, parent, controller):
        ans = str(self.ansbox.get())
        if ans != '':
            if ans in 'countrfit':
                self.ansbox.delete(0, 'end')
                # it'll search for 'o' in the dictionary and access its value which happens to be a textbox so the answer
                #  which the players enters is displayed as the text of the textbox
                self.answers[ans]['text'] = ans
                # works exactly like above statement except that when there is no key, adds answer to an invisible textbox
                self.dupe.get(ans, self.invisible)['text'] = ans
                self.correctans = ans
                self.repeated(parent, controller)
            else:
                self.ansbox.delete(0, 'end')
                text = self.wrong.cget("text") + ans
                self.wrong.configure(text=text)
                self.hangman(parent, controller)
                self.popupmsg2()

        # repeated correct entries

    def repeated(self, parent, controller):
        if self.correctans not in self.l:
            self.l.append(self.correctans)
            self.correctguess(parent, controller)
            self.popupmsg()


        else:
            w = tk.Tk()
            label = tk.Label(w, text="you already guessed that!make a new guess", font='times 30', fg='blue')
            label.pack()
            w.after(2000, lambda: w.destroy())
            w.mainloop()

        # creating parts of hangman on incorrect guesses

    def hangman(self, parent, controller):
        PageTwo.guesses_left = PageTwo.guesses_left - 1
        print(PageTwo.guesses_left)
        if self.guesses_left == 5:
            oval = self.canvas.create_oval(250, 150, 350, 250, fill='brown')
        elif self.guesses_left == 4:
            line = self.canvas.create_line(300, 250, 300, 400, fill='brown')
        elif self.guesses_left == 3:
            line = self.canvas.create_line(300, 300, 230, 350, fill='brown')
        elif self.guesses_left == 2:
            line = self.canvas.create_line(300, 300, 370, 350, fill='brown')
        elif self.guesses_left == 1:
            line = self.canvas.create_line(300, 400, 250, 450, fill='brown')
        elif self.guesses_left == 0:
            line = self.canvas.create_line(300, 400, 350, 450, fill='brown')
            w = tk.Tk()
            label = tk.Label(w, text="WHOOPS!YOU'RE OUT OF GUESSES!"
                                     "IM AFRAID YOU CAN'T PROCEED:(", font='times 30', fg='red')
            label.pack()
            B1 = tk.Button(w, text="Okay") #, command=exit)
            B1.pack()
            w.mainloop()

    def correctguess(self, parent, controller):
        PageTwo.correct_guess -= 1
        print(PageTwo.correct_guess)

        if PageTwo.correct_guess == 1:
            w = tk.Tk()
            label = tk.Label(w, text='''WOAH!CONGRATS!YOU'RE NOW A PRO AT THIS!!!
                            FYI>>>DEFINITION OF COUNTERFEIT:
                        a fraudulent imitation of something else''', font='times 30', fg='purple')
            label.pack()


            B1 = tk.Button(w, text="YAY THANKS!",font='20') #command=exit
            B1.pack()
            w.mainloop()

        # popup msg for correct entry

    def popupmsg(self):

        w = tk.Tk()
        label = tk.Label(w, text='That is correct! :D', font='times 30', fg='green')
        label.pack()
        w.after(2000, lambda: w.destroy())  # Destroy the widget after 2 seconds
        w.mainloop()
        return

        # popup for incorrect entry

    def popupmsg2(self):
        w = tk.Tk()
        label = tk.Label(w, text="That is incorrect", font='times 30', fg='red')
        label.pack()
        w.after(2000, lambda: w.destroy())  # Destroy the widget after 2 seconds
        w.mainloop()

if __name__=='__main__':
    app = mainwindow()
    app.mainloop()
