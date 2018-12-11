#############################################################################################################        
#############################################
#
#course : 15-112 fundamentls of programming
#project : ludo game
#author : Rahaf Abboulibdah
#
#############################################



from PIL import Image
from PIL import ImageTk
from Tkinter import*
from board_class import Board
import time
import random
import glob
#############################################################################################################        

class Menu:
    def __init__(self,menu):
        self.menu=menu
        self.canvas=Canvas(menu,height=600,width=500)
        self.canvas.place(x=0,y=0)
        labelFont = ["calibri",40,"bold"]
        self.lbl=Label(self.canvas,text="WELCOME TO LUDO",fg="white",bg="gray29")
        self.lbl.config(font=labelFont)
        self.lbl.place(x=40,y=100)
        self.canvas.image=PhotoImage(file="intro3.gif")
        self.canvas.create_image(0,0,image=self.canvas.image)
        self.gameModes()
       
        self.help=Button(self.canvas,text="Help",command=self.helpButton,width=50,height=50)
        photo=ImageTk.PhotoImage(file="help.png")
        self.help.configure(image=photo)
        self.help.image=photo
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
      
        home=Button(c,text="Back",command=self.menu2,width=50,height=50)
        photo=ImageTk.PhotoImage(file="back.png")
        home.configure(image=photo)
        home.image=photo
        home.place(x=10,y=10)
        
        labelFont = ["calibri",18,"bold"]
        description1=Label(c,text="--> Ludo is a board game in which 2-4 players can play it.",justify=LEFT,bg="gray50",fg="gold")
        description1.config(font=labelFont)
        description1.place(x=10,y=170)
        descreption2=Label(c,text='''--> The board is divided into four different color parts with
        four basesto differentiate between each player.''',justify=LEFT,bg="gray50",fg="gold")
        descreption2.config(font=labelFont)
        descreption2.place(x=10,y=240)
        description3=Label(c,text='''--> Each player has four tokens. in order to win, one player
        should have all the tokens in the middle of the board.''',justify=LEFT,bg="gray50",fg="gold")
        description3.config(font=labelFont)
        description3.place(x=10,y=320)
        
    def menu2(self):
        self.hlp.destroy()
        menu=Tk()
        menu.geometry("500x520")
        menu.resizable(0,0)    

        menu.title("Ludo Game")
        menu.configure(background='gray25')
        mainMenu=Menu(menu)
        menu.mainloop()        


    def startPlaying(self,playingMode):
       
        self.menu.destroy()
        entry=Tk()
        entry.geometry("700x780")
        entry.title("Ludo Game")
        entry.configure(background='gray25')
        game=GameWindow(entry, playingMode)
        entry.resizable(0,0)    
        entry.mainloop()
        
        
        

                  
    def gameModes(self):
        #playing vs the computer
        buttonFont=["calibri",18,"bold"]
        
        self.computer=Button(self.canvas,command=lambda x=1:self.startPlaying(x),text="Player\nVS\nComputer ",
                         width=10,height=3,bg="RED",fg="white")
        self.computer.config(font=buttonFont)
        self.computer.place(x=80,y=180)

        #two players
        
   
        self.multi2=Button(self.canvas,command=lambda x=2: self.startPlaying(x),text="Two\nPlayers ",
                         width=10,height=3,bg="BLUE4",fg="white")
        self.multi2.config(font=buttonFont)
        self.multi2.place(x=290,y=180)


        #three players
        
        self.multi3=Button(self.canvas,command=lambda x=3: self.startPlaying(x),text="Three\nPlayers ",
                         width=10,height=3,bg="green4",fg="white")
        self.multi3.config(font=buttonFont)
        self.multi3.place(x=80,y=310)


        #four players
        
        self.multi4=Button(self.canvas,command=lambda x=4: self.startPlaying(4),text="Four\nPlayers ",
                         width=10,height=3,bg="darkgoldenrod1",fg="white")
        self.multi4.config(font=buttonFont)
        self.multi4.place(x=290,y=310)

#############################################################################################################        
class GameWindow:
    def __init__(self,entry,playingMode):
        self.gameStarted = True
        self.entry=entry
        self.c=Canvas(bg="gray25",width=680,height=680,highlightbackground="gray25",highlightthickness=7)
        self.c.place(x=3,y=0)
        self.dice()
        font=["calibri",22,"bold"]
        home=Button(self.entry,text="Back",command=self.menu3,width=50,height=50)
        photo=ImageTk.PhotoImage(file="back.png")
        home.configure(image=photo)
        home.image=photo
        home.place(x=10,y=700)
        self.player=0
        print self.board()
        self.playerLst=[]
        self.playingMode=playingMode
        self.setPlayers(self.playingMode)
        self.diceRolled = None
        self.disableOtherPlayerMove()
        self.globalPath=[[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]for i in range(15)]

        self.playerDicesText = Text(self.entry, height=3, width=20, bd=0, font=font, fg= "white", bg="gray25")
        self.playerDicesText.place(x=300,y=700)
        for filename in glob.glob('dic/*.png'):
            self.image_list.append(filename)

    def dice(self):
        self.image_list = []        
        photo=ImageTk.PhotoImage(file="dic/1.png")
        
        self.diceRolled =0
        self.number=StringVar()
        self.roll=Button(self.entry,command=self.rolled,textvariable=self.number,width=50,height=50)
        self.roll.configure(image=photo)
        self.roll.image=photo
                    
        self.roll.place(x=633,y=700)
        self.number.set(self.getDiceNumber("dic/1.png"))

    def rolled(self):


        photoName = random.choice(self.image_list)
        photo=ImageTk.PhotoImage(file=photoName)

        self.roll.configure(image=photo)
        self.roll.image=photo
        diceNumber= self.getDiceNumber(photoName)
        if diceNumber != "None":
            self.number.set(diceNumber)
        else:
            self.number.set("0")
            
        last=self.number.get()
        self.diceRolled  = last
        self.validatePlayerMove()
        return last

    def getDiceNumber(self, photo):
        photo= photo.strip()
        if photo == "dic\\1.png":
            return "1"
        if photo == "dic\\2.png":
            return "2"
        if photo == "dic\\3.png":
            return "3"
        if photo == "dic\\4.png":
            return "4"
        if photo == "dic\\5.png":
            return "5"
        if photo == "dic\\6.png":
            return "6"

    
    def board(self):
        horizontal=Board().horizontalBoard(self.c)
        vertical=Board().verticalBoard(self.c)
        redBase=Board().baseColoring(self.c)

    def menu3(self):
        self.entry.destroy()
        menu=Tk()
        menu.geometry("500x520")
        menu.title("Ludo Game")
        menu.configure(background='gray25')
        mainMenu=Menu(menu)
        menu.mainloop()

    def setPlayers(self,playingMode):
        

        if playingMode == 1: # AI Playing mode
            
            playerBlue = Player(0)
            playerGreen = Player(2)
            self.playerLst.append(playerBlue)# Blue Player user1
            self.playerLst.append(playerGreen)# Green Player Computer
            self.currentPlayer = self.playerLst[0]
            self.AILudo(self.playerLst)

        elif playingMode == 2: # 2 player Playing mode
            playerBlue = Player(0)
            playerGreen = Player(2)
            self.playerLst.append(playerBlue)# Blue Player user1
            self.playerLst.append(playerGreen)# Green Player user2
            self.currentPlayer = self.playerLst[0]
            self.selfLudo(self.playerLst)   

        elif playingMode == 3: # 3 player Playing mode
            playerBlue = Player(0)
            playerRed = Player(1)
            playerGreen = Player(2)
            self.playerLst.append(playerBlue)# Blue Player user1
            self.playerLst.append(playerRed)# Red Player user2
            self.playerLst.append(playerGreen)#Green Player user3
            self.currentPlayer = self.playerLst[0]
            self.selfLudo(self.playerLst)
            
        elif playingMode == 4: # 4 player Playing mode
            playerBlue = Player(0)
            playerRed = Player(1)
            playerGreen = Player(2)
            playerYellow = Player(3)
            self.playerLst.append(playerBlue)# Blue Player user1
            self.playerLst.append(playerRed)# Red Player user2
            self.playerLst.append(playerGreen)#Green Player user
            self.playerLst.append(playerYellow)#Yellow Player user
            self.currentPlayer = self.playerLst[0]
            self.selfLudo(self.playerLst)


        
    def selfLudo(self,palyersLst):
        self.tokenBtnLst=[0]*4
        self.blueTokenCoor=[[70,484],[162,484],[70,576],[162,576]]
        self.redTokenCoor=[[70,70],[162,70],[70,162],[162,162]]
        self.greenTokenCoor=[[484,70],[576,70],[484,162],[576,162]]
        self.yellowTokenCoor=[[484,484],[576,484],[484,576],[576,576]]
        self.gameStarted = True
        rollValue = self.diceRolled
       
        for player in palyersLst:
          
            if player.color== "BLUE" and self.diceRolled!=None:
                for i in range(4):
                    photo=ImageTk.PhotoImage(file="bluePlayer.png")
                    self.tokenBtnLst[i]=Button(self.c,command= lambda x=player,y=i: self.moveToken(x,y),width=43,height=43,borderwidth=0)
                    self.tokenBtnLst[i].place(x=(self.blueTokenCoor[i][0]),y=(self.blueTokenCoor[i][1]))
                    player.lstOfTokens[i].tokenBtn = self.tokenBtnLst[i]
                    self.tokenBtnLst[i].configure(image=photo)
                    self.tokenBtnLst[i].image=photo
                   


            if player.color== "RED" and self.diceRolled!=None:
                photo=ImageTk.PhotoImage(file="redPlayer.png")
                for i in range(4):   
                    self.tokenBtnLst[i]=Button(self.c, command= lambda x=player,y=i: self.moveToken(x,y),width=43,height=43,borderwidth=0)
                    self.tokenBtnLst[i].place(x=(self.redTokenCoor[i][0]),y=(self.redTokenCoor[i][1]))
                    player.lstOfTokens[i].tokenBtn = self.tokenBtnLst[i]
                    self.tokenBtnLst[i].configure(image=photo)
                    self.tokenBtnLst[i].image=photo
                   

            if player.color== "GREEN" and self.diceRolled!=None:
                photo=ImageTk.PhotoImage(file="greenPlayer.png")
                for i in range(4):   
                    self.tokenBtnLst[i]=Button(self.c, command= lambda x=player,y=i: self.moveToken(x,y),width=43,height=43,borderwidth=0)
                    self.tokenBtnLst[i].place(x=(self.greenTokenCoor[i][0]),y=(self.greenTokenCoor[i][1]))
                   
                    player.lstOfTokens[i].tokenBtn = self.tokenBtnLst[i]
                    self.tokenBtnLst[i].configure(image=photo)
                    self.tokenBtnLst[i].image=photo
                   

            if player.color== "YELLOW" and self.diceRolled!=None:
                photo=ImageTk.PhotoImage(file="yellowPlayer.png")
                for i in range(4):   
                    self.tokenBtnLst[i]=Button(self.c,command= lambda x=player,y=i: self.moveToken(x,y),width=43,height=43,borderwidth=0)
                    self.tokenBtnLst[i].place(x=(self.yellowTokenCoor[i][0]),y=(self.yellowTokenCoor[i][1]))
                    player.lstOfTokens[i].tokenBtn = self.tokenBtnLst[i]
                    self.tokenBtnLst[i].configure(image=photo)
                    self.tokenBtnLst[i].image=photo
                   


    def moveToken(self,player,tokenIndex):
        
      

        tokenLastPathIndex = int(self.currentPlayer.lstOfTokens[tokenIndex].tokenlastIndex)
        if len(self.currentPlayer.lstOfRolls)!=0:
            roleValue = int(self.currentPlayer.lstOfRolls[0])
            
            if roleValue == 6 and len(self.currentPlayer.lstOfRolls) <= 1:
                 return
            if roleValue == 6:
                if tokenLastPathIndex == -1: # this token in origin base
                    player.lstOfTokens[tokenIndex].tokenBtn.place(x=self.currentPlayer.playerPath[0][0]*46,y=self.currentPlayer.playerPath[0][1]*46)
                    self.currentPlayer.lstOfTokens[tokenIndex].tokenlastIndex = self.currentPlayer.playerPath.index(self.currentPlayer.playerPath[0])
                    self.checkGlobalPath(tokenLastPathIndex,tokenIndex,self.currentPlayer,roleValue)
                else:
                    tokenLastPathIndex += roleValue
                    tokenEndLst=[56,55,54,53,52,51]
                    valueEndLst=[1,2,3,4,5,6]
                    if self.currentPlayer.playerPath[tokenLastPathIndex-roleValue]!=self.currentPlayer.playerPath[56]:
                        if  tokenLastPathIndex <= 56 :
                            player.lstOfTokens[tokenIndex].tokenBtn.place(x=self.currentPlayer.playerPath[tokenLastPathIndex][0]*46,y=self.currentPlayer.playerPath[tokenLastPathIndex][1]*46)
                            self.currentPlayer.lstOfTokens[tokenIndex].tokenlastIndex = tokenLastPathIndex
                            self.checkGlobalPath(tokenLastPathIndex,tokenIndex,self.currentPlayer,roleValue)

                    else:
                        for i in range(6):
                            if tokenLastPathIndex-roleValue==tokenEndLst[i] and roleValue==valueEndLst[i]:
                                player.lstOfTokens[tokenIndex].tokenBtn.place(x=self.currentPlayer.playerPath[tokenLastPathIndex][0]*46,y=self.currentPlayer.playerPath[tokenLastPathIndex][1]*46)
                                self.currentPlayer.lstOfTokens[tokenIndex].tokenlastIndex = tokenLastPathIndex
                                self.checkGlobalPath(tokenLastPathIndex,tokenIndex,self.currentPlayer,roleValue)
                                player.lstOfTokens[tokenIndex].tokenBtn.config(state="disable")
                        
                            else:
                                self.updateDice()
                                self.getNextPlayer()
                                self.disableOtherPlayerMove()
                            

            else:
                if tokenLastPathIndex == -1: # this token in origin base but not valid move
                    return
                else:
                    
                    if tokenLastPathIndex == -1: # this token in origin base
                        player.lstOfTokens[tokenIndex].tokenBtn.place(x=self.currentPlayer.playerPath[0][0]*46,y=self.currentPlayer.playerPath[0][1]*46)
                        self.currentPlayer.lstOfTokens[tokenIndex].tokenlastIndex = self.currentPlayer.playerPath.index(self.currentPlayer.playerPath[0])
                        self.checkGlobalPath(tokenLastPathIndex,tokenIndex,self.currentPlayer,roleValue)
                    else:
                        tokenLastPathIndex += roleValue
                        print tokenLastPathIndex
                        tokenEndLst=[56,55,54,53,52,51]
                        valueEndLst=[1,2,3,4,5,6]
                        if self.currentPlayer.playerPath[tokenLastPathIndex-roleValue]!=self.currentPlayer.playerPath[56]:
                            if  tokenLastPathIndex <= 56 :
                                player.lstOfTokens[tokenIndex].tokenBtn.place(x=self.currentPlayer.playerPath[tokenLastPathIndex][0]*46,y=self.currentPlayer.playerPath[tokenLastPathIndex][1]*46)
                                self.currentPlayer.lstOfTokens[tokenIndex].tokenlastIndex = tokenLastPathIndex
                                self.checkGlobalPath(tokenLastPathIndex,tokenIndex,self.currentPlayer,roleValue)

                        else:
                            for i in range(6):
                                if tokenLastPathIndex-roleValue==tokenEndLst[i] and roleValue==valueEndLst[i]:
                                    player.lstOfTokens[tokenIndex].tokenBtn.place(x=self.currentPlayer.playerPath[tokenLastPathIndex][0]*46,y=self.currentPlayer.playerPath[tokenLastPathIndex][1]*46)
                                    self.currentPlayer.lstOfTokens[tokenIndex].tokenlastIndex = tokenLastPathIndex
                                    self.checkGlobalPath(tokenLastPathIndex,tokenIndex,self.currentPlayer,roleValue)
                                    player.lstOfTokens[tokenIndex].tokenBtn.config(state="disable")
                                else:
                                    self.updateDice()
                                    self.getNextPlayer()
                                    self.disableOtherPlayerMove()
                            
                                    
##                       
            del self.currentPlayer.lstOfRolls[0]
            

            if len(self.currentPlayer.lstOfRolls) == 0:
                if self.someOneWon==True:
                    self.playerDicesText.delete('1.0',END)
                    self.playerDicesText.insert(END," Congratulations ! you Won :)")
                else:
                    self.updateDice()
                    self.getNextPlayer()
                    self.disableOtherPlayerMove()

            else:
                inOrigin=0
                inWin=0
                for i in self.currentPlayer.lstOfTokens:
                    if i.tokenlastIndex==-1:
                        inOrigin+=1
                for j in self.currentPlayer.lstOfTokens:
                    if j.tokenlastIndex==56:
                        inWin+=1
                if (inOrigin + inWin) == 4 and  len(self.currentPlayer.lstOfRolls)>0 and  self.currentPlayer.lstOfRolls[0] != str(6):
                    self.updateDice()
                    self.getNextPlayer()
                    self.disableOtherPlayerMove()
                
        return          
       
    def checkGlobalPath(self, tokenLastPathIndex,tokenIndex,currentPlayer,roleValue):
        color=self.currentPlayer.color
        coordinate=self.currentPlayer.playerPath[self.currentPlayer.lstOfTokens[tokenIndex].tokenlastIndex]
        otherCase=True
       
        
        #--------------------------------------------------------------------------------------------------------------------
        #if token in base
        if tokenLastPathIndex==-1:
            print "------------------- CASE 1 ------------------------"
            print coordinate,self.currentPlayer.lstOfTokens[tokenIndex].tokenlastIndex
            row=coordinate[0]
            column=coordinate[1]
            print self.globalPath[row][column]
            #if the new spot is not occupide
            if self.globalPath[row][column]==-1:
                print "------------------- CASE 1-1 ------------------------"

                print "first time"
                self.globalPath[row][column]=[color,tokenIndex]

            #else if the new sopt is occupide with same color of token
            elif self.globalPath[row][column]!=-1 and (color==self.globalPath[row][column][0]) :
                
                print "------------------- CASE 1-2 ------------------------"
                print "same color in first spot "
                oldValue=self.globalPath[row][column]
                self.globalPath[row][column]=[oldValue,[color,tokenIndex]]
                print "the appending value of same color in base: ",self.globalPath[row][column]
                    
            #else if the new sopt is occupide with different color of token

            elif self.globalPath[row][column]!=-1 and (color!=self.globalPath[row][column][0][0]) :
                #if [row,column] in safeZones:
                    
                print "------------------- CASE 1-3 ------------------------"
                oldColor=self.currentPlayer.color
                oldToken=self.globalPath[row][column][0]    
                newCoor=self.getTokenBackToBase(oldToken,self.globalPath[row][column][1])
                print newCoor,self.globalPath[row][column][1],self.globalPath[row][column]
                print self.currentPlayer.playerPath
                
                oldPlayer = self.playerLst[self.getPlayerIndex(oldToken)]
                oldPlayer.lstOfTokens[self.globalPath[row][column][1]].tokenBtn.config(state="active")
                tokenIndex = oldPlayer.lstOfTokens[self.globalPath[row][column][1]].tokenId
                coord = self.getTokenBackToBase(oldPlayer.color,tokenIndex )
                
                coordX = int(coord[0])
                coordY = int(coord[1])
                print "coord :", coord, " coordX:",coordX, " coorY:", coordY
                oldPlayer.lstOfTokens[self.globalPath[row][column][1]].tokenBtn.place(x=coordX,y=coordY)
                oldPlayer.lstOfTokens[self.globalPath[row][column][1]].tokenlastIndex=-1
                self.entry.update()
                oldPlayer.lstOfTokens[self.globalPath[row][column][1]].tokenBtn.config(state="disable")
                #self.currentPlayer.color=oldColor
                self.globalPath[row][column]=[oldColor,tokenIndex]

        #if token in board
        elif tokenLastPathIndex!=-1  :
            #print "------------------- CASE 2 ------------------------"

            #print tokenLastPathIndex
            prevIndex = self.currentPlayer.lstOfTokens[tokenIndex].tokenlastIndex
            #print "prevIndex: ", prevIndex
            prevCoord=self.currentPlayer.playerPath[prevIndex-roleValue]
            #print "this is the prev coord :  ",prevCoord
            prevRow=prevCoord[0]
            prevColumn=prevCoord[1]
            row=coordinate[0]
            column=coordinate[1]
            #print row,column
            #print type(self.globalPath[row][column]),self.globalPath[prevRow][prevColumn]
            #if the old spot has two tokens with same colors
            tokenToBeMoved=self.globalPath[row][column]
 
            if self.globalPath[prevRow][prevColumn] != -1 and type(self.globalPath[prevRow][prevColumn][1])!= int and type(self.globalPath[prevRow][prevColumn][1])==list:
                #print "------------------- CASE 2-1 ------------------------"
                #print  " the old spot has two tokens with same colors"
                newPthSaved=self.globalPath[prevRow][prevColumn]
                newSpotValue=self.globalPath[prevRow][prevColumn][1]
                #print "this is the prev row :", newSpotValue

                
                print "this is the row:",row,"this is the col:",column, "color of the occupied token:  "#,self.globalPath[row][column][0]

                #if the new spot is not occupide
                if self.globalPath[row][column]==-1:
                    print "------------------- CASE 2-1-1 ------------------------"
                    self.globalPath[prevRow][prevColumn]=newPthSaved[0]
                    self.globalPath[row][column]=newSpotValue
                    
                #else if the new spot is occupide with same color token
                elif self.globalPath[row][column]!=-1 and (type(self.globalPath[row][column][1])==list or self.globalPath[row][column][1]==color) :
                    print "------------------- CASE 2-1-2 ------------------------"

                    tokenInBoard=self.globalPath[row][column]
                    oldValue=newSpotValue
                    self.globalPath[row][column]=[oldValue,tokenInBoard]
                    self.globalPath[prevRow][prevColumn]=newPthSaved[0]
                    #else if the new spot is occupide with different color token
                elif self.globalPath[row][column]!=-1:
                    print "------------------- CASE 2-1-3 ------------------------"
                    oldColor=self.currentPlayer.color
                    oldToken=self.globalPath[row][column][0]   
                    newCoor=self.getTokenBackToBase(oldToken,self.globalPath[row][column][1])
                    print newCoor,self.globalPath[row][column][1],self.globalPath[row][column]
                    print self.currentPlayer.playerPath
                    
                    oldPlayer = self.playerLst[self.getPlayerIndex(oldToken)]
                    oldPlayer.lstOfTokens[self.globalPath[row][column][1]].tokenBtn.config(state="active")
                    tokenIndex = oldPlayer.lstOfTokens[self.globalPath[row][column][1]].tokenId
                    coord = self.getTokenBackToBase(oldPlayer.color,tokenIndex )
                    
                    coordX = int(coord[0])
                    coordY = int(coord[1])
                    print "coord :", coord, " coordX:",coordX, " coorY:", coordY
                    oldPlayer.lstOfTokens[self.globalPath[row][column][1]].tokenBtn.place(x=coordX,y=coordY)
                    oldPlayer.lstOfTokens[self.globalPath[row][column][1]].tokenlastIndex=-1
                    self.entry.update()
                    oldPlayer.lstOfTokens[self.globalPath[row][column][1]].tokenBtn.config(state="disable")
                    #self.currentPlayer.color=oldColor
                    self.globalPath[row][column]=[oldColor,tokenIndex]
            #else if the old spot has only one token                
            elif otherCase:
                print "------------------- CASE 2-2 ------------------------"
                print  " the old spot has only one token colors"
                print "this is the prev value: ",self.globalPath[prevRow][prevColumn]
                self.globalPath[prevRow][prevColumn]=-1
                print "this is the new value : ",self.globalPath[prevRow][prevColumn]
                row=coordinate[0]
                column=coordinate[1]
                #if the new spot is not occupide
                if self.globalPath[row][column]==-1:
                    print "------------------- CASE 2-2-1 ------------------------"
                    self.globalPath[prevRow][prevColumn]=-1
                    self.globalPath[row][column]=[color,tokenIndex]
                    
                    print "not in base, the color of the spot",self.globalPath[row][column][0]

                    
                #else if the new spot is occupide with same  color token    
                elif self.globalPath[row][column]!=-1 and (color==self.globalPath[row][column][0] or color==self.globalPath[row][column][0][0]) :
                    print "------------------- CASE 2-2-2 ------------------------"
                    print "same color in first spot "
                    oldValue=self.globalPath[row][column]
                    self.globalPath[row][column]=[oldValue,[color,tokenIndex]]
        
                #else if the new spot is occupide with different color token
                elif self.globalPath[row][column]!=-1 :
                    print "------------------- CASE 2-2-3 ------------------------"
                    oldToken=self.globalPath[row][column][0]
                    print oldToken
                    oldColor=self.currentPlayer.color
                    print oldColor
                    print self.currentPlayer.color
                    if type(self.globalPath[row][column][1])==list:
                       print "move invalid, due to the block"
                    else:
                        
                        newCoor=self.getTokenBackToBase(oldToken,self.globalPath[row][column][1])
                        print newCoor,self.globalPath[row][column][1],self.globalPath[row][column]
                        print self.currentPlayer.playerPath
                        
                        oldPlayer = self.playerLst[self.getPlayerIndex(oldToken)]
                        oldPlayer.lstOfTokens[self.globalPath[row][column][1]].tokenBtn.config(state="active")
                        tokenIndex = oldPlayer.lstOfTokens[self.globalPath[row][column][1]].tokenId
                        coord = self.getTokenBackToBase(oldPlayer.color,tokenIndex )
                        
                        coordX = int(coord[0])
                        coordY = int(coord[1])
                        print "coord :", coord, " coordX:",coordX, " coorY:", coordY
                        oldPlayer.lstOfTokens[self.globalPath[row][column][1]].tokenBtn.place(x=coordX,y=coordY)
                        oldPlayer.lstOfTokens[self.globalPath[row][column][1]].tokenlastIndex=-1
                        self.entry.update()
                        oldPlayer.lstOfTokens[self.globalPath[row][column][1]].tokenBtn.config(state="disable")
                        self.globalPath[row][column]=[oldColor,tokenIndex]
##
##        for i in range(15):
##            print self.globalPath[i]


                        
    def getPlayerIndex(self, playerColor):
        for i in range(len(self.playerLst)):
            if self.playerLst[i].color == playerColor:
                return i
                        
    def getTokenBackToBase(self,playerColor,tokenIndex):
      
        if playerColor=="RED": 
            redTokenCoor=[[70,70],[162,70],[70,162],[162,162]]
            return redTokenCoor[tokenIndex]
        if playerColor=="BLUE":
            blueTokenCoor=[[70,484],[162,484],[70,576],[162,576]]
            return blueTokenCoor[tokenIndex]
        if playerColor=="GREEN":    
            greenTokenCoor=[[484,70],[576,70],[484,162],[576,162]]
            return greenTokenCoor[tokenIndex]
        else:
            yellowTokenCoor=[[484,484],[576,484],[484,576],[576,576]]
            return yellowTokenCoor[tokenIndex]
        
    def validatePlayerMove(self):
        inOrigin=0
        for i in self.currentPlayer.lstOfTokens:
            if i.tokenlastIndex==-1:
                inOrigin+=1
        
        if inOrigin == 4:
            if len(self.currentPlayer.lstOfRolls) == 0:
                if self.diceRolled==str(6):
                    self.currentPlayer.lstOfRolls.append(self.diceRolled)
                else:
                    self.currentPlayer.lstOfRolls =[]
                    self.updateDice()
                    self.getNextPlayer()
                    self.disableOtherPlayerMove()

            elif len(self.currentPlayer.lstOfRolls) == 1:
                   self.currentPlayer.lstOfRolls.append(self.diceRolled)
         
            elif len(self.currentPlayer.lstOfRolls) == 2 and self.currentPlayer.lstOfRolls[1] == str(6):
                if self.diceRolled !=str(6):
                   self.currentPlayer.lstOfRolls.append(self.diceRolled)
            
                else:
                    self.currentPlayer.lstOfRolls =[]
                    self.updateDice()
                    self.getNextPlayer()
                    self.disableOtherPlayerMove()
 

        elif inOrigin != 4:
     
            if len(self.currentPlayer.lstOfRolls) == 0:
                   self.currentPlayer.lstOfRolls.append(self.diceRolled)
                   
     
            elif len(self.currentPlayer.lstOfRolls) == 1 and self.currentPlayer.lstOfRolls[0] == str(6):
                   self.currentPlayer.lstOfRolls.append(self.diceRolled)
         
            elif len(self.currentPlayer.lstOfRolls) == 2 and self.currentPlayer.lstOfRolls[1] == str(6):
                if self.diceRolled !=str(6):
                   self.currentPlayer.lstOfRolls.append(self.diceRolled)
            
                else:
                    self.currentPlayer.lstOfRolls =[]
                    self.updateDice()
                    self.getNextPlayer()
                    self.disableOtherPlayerMove()
 

        if  len(self.currentPlayer.lstOfRolls) != 0:
            self.playerDicesText.delete('1.0',END)
            self.playerDicesText.insert(END,self.currentPlayer.lstOfRolls)
            

        if self.playingMode==1 and self.currentPlayer.color=="GREEN" and self.currentPlayer.lstOfRolls !=[]:
           # print " inside validate (1)"
            if len(self.currentPlayer.lstOfRolls )==2 and self.currentPlayer.lstOfRolls[1]!= str(6) :
                #print " inside validate (2)"
                self.AiMoveToken(inOrigin)
            elif len(self.currentPlayer.lstOfRolls)==3:
               # print " inside validate (3)"
                self.AiMoveToken(inOrigin)

            elif self.currentPlayer.lstOfRolls[0]!= str(6):
                #print " inside validate (4)"
                self.AiMoveToken(inOrigin)
                


    
    def updateDice(self):
        self.entry.update()
        self.entry.after(300)
        self.diceRolled = 1
        self.number.set(self.diceRolled)
        photo=ImageTk.PhotoImage(file="dic/1.png")
        self.roll.configure(image=photo)
        self.roll.image=photo
            
    def getNextPlayer(self):
        self.playerDicesText.delete('1.0',END)
        lastIndex = len(self.playerLst) - 1 
        if self.currentPlayer != self.playerLst[lastIndex]:
            self.currentPlayer=self.playerLst[self.playerLst.index(self.currentPlayer)+1]
        else:
            self.currentPlayer=self.playerLst[0]


    def playerMove(self):
        if len(self.currentPlayer.lstOfRolls) !=0:
            return True
        else:
            return False
        
        


    
    def disableOtherPlayerMove(self):
        currentColor = self.currentPlayer.color
        for player in self.playerLst:
            if player.color != currentColor:  
                for i in range(4):   
                    player.lstOfTokens[i].tokenBtn.config(state="disable")

            else:  
                for i in range(4):
                    if player.lstOfTokens[i].tokenlastIndex != 56:
                        player.lstOfTokens[i].tokenBtn.config(state="active")


######################################################################################################################
#                                                           AI mode
######################################################################################################################

    def AILudo(self,playersLst):
        self.tokenBtnLst=[0]*4
        self.blueTokenCoor=[[70,484],[162,484],[70,576],[162,576]]
        self.greenTokenCoor=[[484,70],[576,70],[484,162],[576,162]]

        for player in playersLst:
          
            if player.color== "BLUE" and self.diceRolled!=None:
                for i in range(4):
                    photo=ImageTk.PhotoImage(file="bluePlayer.png")
                    self.tokenBtnLst[i]=Button(self.c,command= lambda x=player,y=i: self.moveToken(x,y),width=43,height=43,borderwidth=0)
                    self.tokenBtnLst[i].place(x=(self.blueTokenCoor[i][0]),y=(self.blueTokenCoor[i][1]))
                    player.lstOfTokens[i].tokenBtn = self.tokenBtnLst[i]
                    self.tokenBtnLst[i].configure(image=photo)
                    self.tokenBtnLst[i].image=photo
    

            if player.color== "GREEN" and self.diceRolled!=None:
                photo=ImageTk.PhotoImage(file="greenPlayer.png")
                for i in range(4):   
                    self.tokenBtnLst[i]=Button(self.c,width=43,height=43,borderwidth=0)
                    self.tokenBtnLst[i].place(x=(self.greenTokenCoor[i][0]),y=(self.greenTokenCoor[i][1]))
                   
                    player.lstOfTokens[i].tokenBtn = self.tokenBtnLst[i]
                    self.tokenBtnLst[i].configure(image=photo)
                    self.tokenBtnLst[i].image=photo






    def AiMoveToken(self,inOrigin):
                           
            #if at least one token in board, check Sequentially:
            #1) if the token is in danger, escape
            #2) if the token can win, make a move to win 
            #3) if the token can attack another token , attack   

        length = len (self.currentPlayer.playerPath)

        AiGreenPath=[(8,1),(8,2),(8,3),
                    (8,4),(8,5),(9,6),(10,6),(11,6),(12,6),
                    (13,6),(14,6),(14,7),(14,8),(13,8),(12,8),
                    (11,8),(10,8),(9,8),(8,9),(8,10),(8,11),
                    (8,12),(8,13),(8,14),(7,14),(6,14),(6,13),
                    (6,12),(6,11),(6,10),(6,9),(5,8),(4,8),
                    (3,8),(2,8),(1,8),(0,8),(0,7),(0,6),(1,6),
                    (2,6),(3,6),(4,6),(5,6),(6,5),(6,4),(6,3),
                    (6,2),(6,1),(6,0),(7,0),(8,0)]
        
        tokenIndex=0
        noOfRolls= len(self.currentPlayer.lstOfRolls)
    #check if all tokens in origin, call allTokensInBase function
        while len(self.currentPlayer.lstOfRolls) >0:
            if inOrigin==4:
                    if self.currentPlayer.lstOfRolls[0]== str(6):
                        self.moveToken(self.currentPlayer,tokenIndex)
                        self.currentPlayer.lstOfTokens[tokenIndex].tokenlastIndex = self.currentPlayer.playerPath.index(self.currentPlayer.playerPath[0])
                        tokenIndex+=1
                        noOfRolls -=1
                    else:
                        
                        self.moveToken(self.currentPlayer,tokenIndex-1)
                        if self.currentPlayer.lstOfRolls==[]:
                           return       
                        else:
                            self.getPlayerPriority(AiGreenPath)    
                        

                        
                    
            else:
                getNextTokenOut=0
                for index in range(4):
                    if int(self.currentPlayer.lstOfTokens[getNextTokenOut].tokenlastIndex):
                        getNextTokenOut=index
             
                if self.currentPlayer.lstOfRolls[0]== str(6):
                    self.moveToken(self.currentPlayer,getNextTokenOut)
                    self.currentPlayer.lstOfTokens[getNextTokenOut].tokenlastIndex = self.currentPlayer.playerPath.index(self.currentPlayer.playerPath[0])
                    
                
                else:
                        
                    priority=self.getPlayerPriority(AiGreenPath)
                    choosenCase=-1
                    value=0
                    for case in range(3):
                        oneCase=priority[case]
                        for i in range(len(oneCase)):
                            if oneCase[i] == 1 and choosenCase ==-1:
                                choosenCase= case
                                self.moveToken(self.currentPlayer,i)
                                

                    if choosenCase==-1:
                        self.moveToken(self.currentPlayer,value)       
                                
 

           
                

    def getPlayerPriority(self, AiGreenPath):
        finalMatrix=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        pathCheckLst=[0,0,0,0,0,0]
        tokenLength= len(self.currentPlayer.lstOfTokens)
        AIwinningPath=[(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6)]
       
        #--------------------------------------------------------------------------------------------------                
            
  
       # check if token in danger case 
        for token in range (tokenLength):
            print "danger case started ", tokenLength
            tokenLastIndex = self.currentPlayer.lstOfTokens[token].tokenlastIndex

            if tokenLastIndex > -1:
                for position in range (6):
                    row=AiGreenPath[tokenLastIndex-position-1][0]
                    column=AiGreenPath[tokenLastIndex-position-1][1]
                    pathCheckLst[position]=self.globalPath[row][column]
                
                for values in pathCheckLst:
                    if values !=-1:
                        finalMatrix[0][token]=1
        
        #--------------------------------------------------------------------------------------------------                
                    
        # check if token can kill or eat other tokens (kill case):            
                    
        for secondToken in range (tokenLength):
            tokenLastIndex = self.currentPlayer.lstOfTokens[secondToken].tokenlastIndex


            if tokenLastIndex <=50 and tokenLastIndex >-1:
                for secondPosition in range (6):
                   
                    row=AiGreenPath[tokenLastIndex+1][0]
                    column=AiGreenPath[tokenLastIndex+1][1]
            
                    pathCheckLst[secondPosition]=self.globalPath[row][column]
                for secondValues in range(len(pathCheckLst)):

                        if pathCheckLst[secondValues] != -1 and type(pathCheckLst[secondValues][1])==list and pathCheckLst[secondValues][0][0]!="GREEN":
                            finalMatrix[1][secondToken]=-1

                        elif pathCheckLst[secondValues] != -1:
                            finalMatrix[1][secondToken]=1
                            
                       
        #--------------------------------------------------------------------------------------------------                
        #in case a token can win, congratulation..!!! win case                

        for thirdToken in range (tokenLength):
            tokenLastIndex = self.currentPlayer.lstOfTokens[thirdToken].tokenlastIndex
            for thirdPosition in range (6):
                if 51<=(tokenLastIndex+(thirdPosition+1))<=56:
                    finalMatrix[2][thirdToken]=1

                
                        
        
        return finalMatrix
        
    def someOneWon(self):
        wons=0
        for i in self.currentPlayer.lstOfTokens:
            if i.tokenlastIndex==56:
                wons+=1
        if wons==4:
            return True
        else:
            return False
#############################################################################################################   

class Tokens:
    def __init__(self):
        self.tokenlastIndex=-1 # -1, token did not move yet on board
        self.tokenId=None
        self.tokenColor=None
        self.tokenBtn=None
        
        
        
    def createTokens(self,canvas,player):  
        lines="gray25"
        if player=="RED":
            self.canvas=canvas
            self.canvas.create_oval(80,80,104,104,fill="brown4",outline=lines)
            self.canvas.create_oval(172,80,196,104,fill="brown4",outline=lines)
            self.canvas.create_oval(80,172,104,196,fill="brown4",outline=lines)
            self.canvas.create_oval(172,172,196,196,fill="brown4",outline=lines)   

    
                   
#############################################################################################################        

class Player:
    
    global bluePath, redPath, greenPath, yellowPath 
    bluePath=[(6,13),(6,12),(6,11),(6,10),(6,9),
                       (5,8),(4,8),(3,8),(2,8),(1,8),(0,8),
                       (0,7),(0,6),(1,6),(2,6),(3,6),(4,6),
                       (5,6),(6,5),(6,4),(6,3),(6,2),(6,1),
                       (6,0),(7,0),(8,0),(8,1),(8,2),(8,3),
                       (8,4),(8,5),(9,6),(10,6),(11,6),(12,6),
                       (13,6),(14,6),(14,7),(14,8),(13,8),(12,8),
                       (11,8),(10,8),(9,8),(8,9),(8,10),(8,11),
                       (8,12),(8,13),(8,14),(7,14),(7,13),(7,12),
                       (7,11),(7,10),(7,9),(7,8)]
                       

    redPath=[(1,6),(2,6),(3,6),(4,6),
                    (5,6),(6,5),(6,4),(6,3),(6,2),(6,1),
                    (6,0),(7,0),(8,0),(8,1),(8,2),(8,3),
                    (8,4),(8,5),(9,6),(10,6),(11,6),(12,6),
                    (13,6),(14,6),(14,7),(14,8),(13,8),(12,8),
                    (11,8),(10,8),(9,8),(8,9),(8,10),(8,11),
                    (8,12),(8,13),(8,14),(7,14),(6,14),(6,13),
                    (6,12),(6,11),(6,10),(6,9),(5,8),(4,8),
                    (3,8),(2,8),(1,8),(0,8),(0,7),(1,7),(2,7),
                    (3,7),(4,7),(5,7),(6,7)]
      

    greenPath=[(8,1),(8,2),(8,3),
                    (8,4),(8,5),(9,6),(10,6),(11,6),(12,6),
                    (13,6),(14,6),(14,7),(14,8),(13,8),(12,8),
                    (11,8),(10,8),(9,8),(8,9),(8,10),(8,11),
                    (8,12),(8,13),(8,14),(7,14),(6,14),(6,13),
                    (6,12),(6,11),(6,10),(6,9),(5,8),(4,8),
                    (3,8),(2,8),(1,8),(0,8),(0,7),(0,6),(1,6),
                    (2,6),(3,6),(4,6),(5,6),(6,5),(6,4),(6,3),
                    (6,2),(6,1),(6,0),(7,0),(7,1),(7,2),(7,3),
                    (7,4),(7,5),(7,6)]

    yellowPath=[(13,8),(12,8),(11,8),(10,8),(9,8),
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
        
    def __init__(self,playerNo):
        self.lstOfTokens=[]
        self.color="BLUE"
        self.lstOfRolls=[]
        for i in range(4):
            self.token=Tokens()
            self.token.tokenId =i
            self.token.tokenColor = playerNo
            self.lstOfTokens.append(self.token)
        self.coordinates=Tokens().createTokens
        self.playerPath=[]

        if playerNo == 0: # the blue player
            self.playerPath = bluePath
            self.color="BLUE"
        elif playerNo == 1: # the red player
            self.playerPath = redPath
            self.color="RED"
        elif playerNo == 2: # the green player
            self.playerPath = greenPath
            self.color="GREEN"
        elif playerNo == 3: # the yellow player
            self.playerPath = yellowPath
            self.color="YELLOW"


            
            

menu=Tk()
menu.geometry("500x520")
menu.title("Ludo Game")
menu.configure(background='gray25')
mainMenu=Menu(menu)
menu.mainloop()        


