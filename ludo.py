#############################################################################################################        
#############################################
#
#course : 15-112 fundamentls of programming
#project : ludo game
#author : Rahaf Abboulibdah
#
#############################################




from Tkinter import*
from board_class import Board
import random
#############################################################################################################        

class Menu:
    def __init__(self,menu):
        self.menu=menu
        self.canvas=Canvas(menu,height=500,width=500)
        self.canvas.place(x=0,y=0)
        labelFont = ['times',30,'bold']
        self.lbl=Label(self.canvas,text="WELCOME TO LUDO",fg="white",bg="gray29")
        self.lbl.config(font=labelFont)
        self.lbl.place(x=40,y=100)
        self.canvas.image=PhotoImage(file="intro3.gif")
        self.canvas.create_image(0,0,image=self.canvas.image)
        self.gameModes()
        self.help=Button(self.canvas,text="Help",command=self.helpButton)
        self.help.place(x=230,y=460)
        
    def helpButton(self):
        self.menu.destroy()
        self.hlp=Tk()
        self.hlp.geometry("600x500")
        self.hlp.title("Help")
        self.hlp.resizable(0,0)
        c=Canvas(self.hlp,height=660,width=900)
        c.place(x=0,y=0)
        c.image=PhotoImage(file="help3.gif")
        c.create_image(300,240,image=c.image)
        home=Button(c,text="back",command=self.menu2)
        home.place(x=10,y=10)
        
    def menu2(self):
        self.hlp.destroy()
        menu=Tk()
        menu.geometry("500x500")
        menu.title("Ludo Star")
        menu.configure(background='gray25')
        mainMenu=Menu(menu)
        menu.mainloop()        


    def startPlaying(self):
        self.menu.destroy()
        entry=Tk()
        entry.geometry("700x780")
        entry.title("Ludo Star")
        entry.configure(background='gray25')
        game=GameWindow(entry)
        entry.resizable(0,0)
        entry.mainloop()


    def gameModes(self):
        #playing vs the computer
        buttonFont=["times",15,""]
        self.computer=Button(self.canvas,command=self.startPlaying,text="Player\nVS\nComputer ",
                         width=10,height=3,bg="red",fg="white")
        self.computer.config(font=buttonFont)
        self.computer.place(x=80,y=180)

        #two players
        button2Font=["times",15,""]
        self.multi2=Button(self.canvas,command=self.startPlaying,text="Two\nPlayers ",
                         width=10,height=3,bg="blue4",fg="white")
        self.multi2.config(font=buttonFont)
        self.multi2.place(x=290,y=180)


        #three players
        button3Font=["times",15,""]
        self.multi3=Button(self.canvas,command=self.startPlaying,text="Three\nPlayers ",
                         width=10,height=3,bg="green4",fg="white")
        self.multi3.config(font=buttonFont)
        self.multi3.place(x=80,y=310)


        #four players
        button4Font=["times",15,""]
        self.multi4=Button(self.canvas,command=self.startPlaying,text="Four\nPlayers ",
                         width=10,height=3,bg="darkgoldenrod1",fg="white")
        self.multi4.config(font=buttonFont)
        self.multi4.place(x=290,y=310)

#############################################################################################################        

class Dice:
    def __init__(self,entry):
        self.entry=entry
        self.number=StringVar()
        self.roll=Button(self.entry,command=self.rolled,textvariable=self.number,width=7,height=4)
        self.roll.place(x=600,y=700)


    def rolled(self):
        self.roll.config(state="disable")
        self.number.set(random.randint(1,6))
        last=self.number.get()

#############################################################################################################        
class GameWindow:
    def __init__(self,entry):
        self.entry=entry
        self.c=Canvas(bg="gray25",width=680,height=680,highlightbackground="gray25",highlightthickness=7)
        self.c.place(x=3,y=0)
        self.roll=Dice(self.entry)
        home=Button(self.entry,text="back",command=self.menu3)
        home.place(x=20,y=740)
        
        print self.board()
       
    def board(self):
        horizontal=Board().horizontalBoard(self.c)
        vertical=Board().verticalBoard(self.c)
        redBase=Board().baseColoring(self.c)


    def menu3(self):
        self.entry.destroy()
        menu=Tk()
        menu.geometry("500x500")
        menu.title("Ludo Star")
        menu.configure(background='gray25')
        mainMenu=Menu(menu)
        menu.mainloop()
        

class Tokens:
    def __init__(self):
        #self.canvas=GameWindow().__init__()
        self.bluePath=[(6,13),(6,12),(6,11),(6,10),(6,9),
                       (5,8),(4,8),(3,8),(2,8),(1,8),(0,8),
                       (0,7),(0,6),(1,6),(2,6),(3,6),(4,6),
                       (5,6),(6,5),(6,4),(6,3),(6,2),(6,1),
                       (6,0),(7,0),(8,0),(8,1),(8,2),(8,3),
                       (8,4),(8,5),(9,6),(10,6),(11,6),(12,6),
                       (13,6),(14,6),(14,7),(14,8),(13,8),(12,8),
                       (11,8),(10,8),(9,8),(8,9),(8,10),(8,11),
                       (8,12),(8,13),(8,14),(7,14),(7,13),(7,12),
                       (7,11),(7,10),(7,9),(7,8)]
                       

        self.redPath=[(1,6),(2,6),(3,6),(4,6),
                    (5,6),(6,5),(6,4),(6,3),(6,2),(6,1),
                    (6,0),(7,0),(8,0),(8,1),(8,2),(8,3),
                    (8,4),(8,5),(9,6),(10,6),(11,6),(12,6),
                    (13,6),(14,6),(14,7),(14,8),(13,8),(12,8),
                    (11,8),(10,8),(9,8),(8,9),(8,10),(8,11),
                    (8,12),(8,13),(8,14),(7,14),(6,14),(6,13),
                    (6,12),(6,11),(6,10),(6,9),(5,8),(4,8),
                    (3,8),(2,8),(1,8),(0,8),(0,7),(1,7),(2,7),
                    (3,7),(4,7),(5,7),(6,7)]
      

        self.greenPath=[(8,1),(8,2),(8,3),
                    (8,4),(8,5),(9,6),(10,6),(11,6),(12,6),
                    (13,6),(14,6),(14,7),(14,8),(13,8),(12,8),
                    (11,8),(10,8),(9,8),(8,9),(8,10),(8,11),
                    (8,12),(8,13),(8,14),(7,14),(6,14),(6,13),
                    (6,12),(6,11),(6,10),(6,9),(5,8),(4,8),
                    (3,8),(2,8),(1,8),(0,8),(0,7),(0,6),(1,6),
                    (2,6),(3,6),(4,6),(5,6),(6,5),(6,4),(6,3),
                    (6,2),(6,1),(6,0),(7,0),(7,1),(7,2),(7,3),
                    (7,4),(7,5),(7,6)]

        self.yellowPath=[(13,8),(12,8),(11,8),(10,8),(9,8),
                       (8,9),(8,10),(8,11),(8,12),(8,13),
                       (8,14),(7,14),(6,14),(6,13),(6,12),
                       (6,11),(6,10),(6,9),(5,8),(4,8),
                       (3,8),(2,8),(1,8),(0,8),(0,7),(0,6),
                       (1,6),(2,6),(3,6),(4,6),(5,6),(6,5),
                       (6,4),(6,3),(6,2),(6,1),(6,0),(7,0),
                       (8,0),(8,1),(8,2),(8,3),(8,4),(8,5),
                       (9,6),(10,6),(11,6),(12,6),(13,6),
                       (14,6),(14,7),(13,7),(12,7),(11,7),
                       (10,7),(9,7),(8,7)]
        
        
    def createTokens(self,canvas,player):  
        lines="gray25"
        if player=="RED":
            self.canvas=canvas
            self.canvas.create_oval(80,80,104,104,fill="brown4",outline=lines)
            self.canvas.create_oval(172,80,196,104,fill="brown4",outline=lines)
            self.canvas.create_oval(80,172,104,196,fill="brown4",outline=lines)
            self.canvas.create_oval(172,172,196,196,fill="brown4",outline=lines)   
                       
#############################################################################################################        

class player:
    def __init__(self):
        self.color="blue"
        self.tokens=Tokens()
        self.coordinates=Tokens().createTokens
        
        
   


menu=Tk()
menu.geometry("500x500")
menu.title("Ludo Star")
menu.configure(background='gray25')
mainMenu=Menu(menu)
menu.mainloop()        


