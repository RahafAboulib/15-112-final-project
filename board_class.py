#############################################################################################################        
#############################################
#
#course : 15-112 fundamentls of programming
#project : ludo game
#author : Rahaf Abboulibdah
#
#############################################
       
class Board:
    def __init__(self):
        self.squareWidth=46
        self.squareHeight=46
        self.x=0
        self.y=0
        self.horzLst=[]
        self.vertLst=[]
        
    def horizontalBoard(self,canvas):
        w1=self.squareWidth
        h1=self.squareHeight
        lines="black"
        for col in range(0,15):
            lst=[]
            count=0
            for row in range(6,9):
                if col in (1,2,3,4,5) and row==7:
                    canvas.create_rectangle(w1*col,h1*row,(w1*col)+w1,(h1*row)+h1, fill="brown3",outline=lines)
                elif col in (9,10,11,12,13) and row==7:
                    canvas.create_rectangle(w1*col,h1*row,(w1*col)+w1,(h1*row)+h1,fill="gold",outline=lines)
                elif col==1 and row==6:
                    canvas.create_rectangle(w1*col,h1*row,(w1*col)+w1,(h1*row)+h1, fill="brown3",outline=lines)
                elif col==13 and row==8:
                    canvas.create_rectangle(w1*col,h1*row,(w1*col)+w1,(h1*row)+h1,fill="gold",outline=lines)
                elif col==2 and row==8:
                    canvas.create_rectangle(w1*col,h1*row,(w1*col)+w1,(h1*row)+h1,fill="gray61",outline=lines)
                elif col==12 and row==6:
                    canvas.create_rectangle(w1*col,h1*row,(w1*col)+w1,(h1*row)+h1,fill="gray61",outline=lines)
                else:
                    canvas.create_rectangle(w1*col,h1*row,(w1*col)+w1,(h1*row)+h1,fill="gray99",outline=lines)

                   
                lst.append((row,col))
            self.horzLst.append(lst)
        print self.horzLst
        return self.horzLst



    def verticalBoard(self,canvas):
        w1=self.squareWidth
        h1=self.squareHeight
        lines="black"
        for col in range(6,9):
            lst=[]
            count=0
            for row in range(0,15):
                if row in (1,2,3,4,5) and col==7:
                    
                    canvas.create_rectangle(w1*col,h1*row,(w1*col)+w1,(h1*row)+h1, fill="forest green",outline=lines)

                elif row in (9,10,11,12,13) and col==7:
                    canvas.create_rectangle(w1*col,h1*row,(w1*col)+w1,(h1*row)+h1,fill="blue",outline=lines)

                elif row==1 and col==8:
                    canvas.create_rectangle(w1*col,h1*row,(w1*col)+w1,(h1*row)+h1, fill="forest green",outline=lines)

                elif row==13 and col==6:
                    canvas.create_rectangle(w1*col,h1*row,(w1*col)+w1,(h1*row)+h1,fill="blue",outline=lines)
                elif row==2 and col==6:
                    canvas.create_rectangle(w1*col,h1*row,(w1*col)+w1,(h1*row)+h1,fill="gray61",outline=lines)
                elif row==12 and col==8:
                    canvas.create_rectangle(w1*col,h1*row,(w1*col)+w1,(h1*row)+h1,fill="gray61",outline=lines)

                else:
                    canvas.create_rectangle(w1*col,h1*row,(w1*col)+w1,(h1*row)+h1,fill="gray99",outline=lines)

                lst.append((row,col))
            self.vertLst.append(lst)
        print self.vertLst
        return self.vertLst


    def baseColoring(self,canvas):
        lines="gray25"
        #REDBASE
        canvas.create_rectangle(0,0,276,276,fill="brown3",outline=lines)
        canvas.create_rectangle(46, 46,230,230,fill="white",outline=lines)
        canvas.create_oval(70,70,114,114,fill="brown3",outline=lines)
        canvas.create_oval(162,70,206,114,fill="brown3",outline=lines)
        canvas.create_oval(70,162,114,206,fill="brown3",outline=lines)
        canvas.create_oval(162,162,206,206,fill="brown3",outline=lines)
        #BLUEBASE
        canvas.create_rectangle(0,414,276,690,fill="blue",outline=lines)
        canvas.create_rectangle(46,460,230,644,fill="white",outline=lines)
        canvas.create_oval(70,484,114,528,fill="blue",outline=lines)
        canvas.create_oval(162,484,206,528,fill="blue",outline=lines)
        canvas.create_oval(70,576,114,620,fill="blue",outline=lines)
        canvas.create_oval(162,576,206,620,fill="blue",outline=lines)
        #GREENBASE
        canvas.create_rectangle(414,0,690,276,fill="forest green",outline=lines)
        canvas.create_rectangle(460, 46,644,230,fill="white",outline=lines)
        canvas.create_oval(484,70,528,114,fill="forest green",outline=lines)
        canvas.create_oval(576,70,620,114,fill="forest green",outline=lines)
        canvas.create_oval(484,162,528,206,fill="forest green",outline=lines)
        canvas.create_oval(576,162,620,206,fill="forest green",outline=lines)
        #YELLOWBASE
        canvas.create_rectangle(414,414,690,690,fill="gold",outline=lines)
        canvas.create_rectangle(460, 460,644,644,fill="white",outline=lines)
        canvas.create_oval(484,484,528,528,fill="gold",outline=lines)
        canvas.create_oval(576,484,620,528,fill="gold",outline=lines)
        canvas.create_oval(484,576,528,620,fill="gold",outline=lines)
        canvas.create_oval(576,576,620,620,fill="gold",outline=lines)
        #CENTER
        canvas.create_polygon(276,276,414,276,345,345,fill="forest green",outline=lines)
        canvas.create_polygon(276,276,276,414,345,345,fill="brown3",outline=lines)
        canvas.create_polygon(414,414,414,276,345,345,fill="gold",outline=lines)
        canvas.create_polygon(414,414,276,414,345,345,fill="blue",outline=lines)

