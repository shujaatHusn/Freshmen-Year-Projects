class playGame(object):
    disabled=[]
    
    def chooseWinner(self):
        result={'X':'You won!', 'O':'Whoops! The computer out-smarted you!', 'D':'Draw'}
        winner="No winner yet"
            #checking columns
        if self.c1r1['text']==self.c1r2['text'] and self.c1r2['text']==self.c1r3['text']:
            winner=str(self.c1r1['text'])
            
        elif self.c2r1['text']==self.c2r2['text'] and self.c2r2==self.c2r3['text']:
            winner=str(self.c2r1['text'])
            
        elif self.c3r1['text']==self.c3r2['text'] and self.c3r2['text']==self.c3r3['text']:
            winner=str(self.c3r1['text'])
        
        
        #checking rows
        if self.c1r1['text']==self.c2r1['text'] and self.c2r1['text']==self.c3r1['text']:
            winner=self.c1r1['text']
        elif self.c1r2['text']==self.c2r2['text'] and self.c2r2['text']==self.c3r2['text']:
            winner=self.c1r2['text']
        elif self.c1r3['text']==self.c2r3['text'] and self.c2r3['text']==self.c3r3['text']:
            winner=self.c1r3['text']
            
        #checking diagonals
        if self.c1r1['text']==self.c2r2['text'] and self.c2r2['text']==self.c3r3['text']:
            winner=self.c1r1['text']
        elif self.c3r1['text']==self.c2r2['text'] and self.c2r2['text']==self.c1r3['text']:
            winner=self.c3r1['text']
        else:
            if all(button['state']=='disabled' for button in self.buttons):
                winner='D'
        
        self.announce['text']=result.get(winner)    
    turns=0
    def userTurn(self,buttonName):
        playGame.turns+=1
        #user's chosen button is disabled and added to disabled list
        buttonName.configure(state='disabled',text='X')
        self.disabled.append(buttonName)
        
        #choosing button for computer
        import random
        if len(self.disabled)<8:
            compButton=random.choice(self.buttons)
            while str(compButton['state'])=='disabled':
                compButton=random.choice(self.buttons)
            else:
                #disables computer's chosen button
                compButton.configure(state='disabled',text="O")
                self.disabled.append(compButton)
        self.chooseWinner()


    class GUI(playGame):
        def __init__(self):    
    
            import tkinter as tk
            self.home=tk.Tk()
            self.home.title("Tic Tac Toe")
            self.home.geometry("160x300")
            w,h=6,3                      
            
            self.c1r1=tk.Button(text='',width=w, height=h, command=lambda: self.userTurn(self.c1r1))
            self.c1r1.pack()
            
            
          
            self.c1r2=tk.Button(text='',width=w, height=h, command=lambda: self.userTurn(self.c1r2))
            self.c1r2.pack()
            
         
            self.c1r3=tk.Button(text='',width=w, height=h, command=lambda: self.userTurn(self.c1r3))
            self.c1r3.pack()
    
    
    
            self.c2r1=tk.Button(text='',width=w, height=h, command=lambda: self.userTurn(self.c2r1))
            self.c2r1.pack()
    
            self.c2r2=tk.Button(text='',width=w, height=h, command=lambda: self.userTurn(self.c2r2))
            self.c2r2.pack()
    
            self.c2r3=tk.Button(text='',width=w, height=h, command=lambda: self.userTurn(self.c2r3))
            self.c2r3.pack()
    
    
    
            self.c3r1=tk.Button(text='',width=w, height=h, command=lambda: self.userTurn(self.c3r1))
            self.c3r1.pack()
    
            self.c3r2=tk.Button(text='',width=w, height=h, command=lambda: self.userTurn(self.c3r2))
            self.c3r2.pack()
    
            self.c3r3=tk.Button(text='',width=w, height=h, command=lambda: self.userTurn(self.c3r3))
            self.c3r3.pack()
            
            self.buttons=[self.c1r1,self.c1r2, self.c1r3, self.c2r1, self.c2r2, self.c2r3, self.c3r1, self.c3r2, self.c3r3]
            
            self.announce=tk.Label(text='No winner yet',width=w, height=h)
            self.announce.pack()
            
            
            
            self.home.mainloop()
        
if __name__=='__main__':      
    x=GUI() 
