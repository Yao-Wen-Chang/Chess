
# In this file, fill in the ... parts with lines of code. Do not
# create new functions.

from random import seed, randrange
P=" ♟♜♝♞♛♚"; L,R,BL,TL="▌▐▄▀"
Norm='\033[1;m'
BonR=WonR=WonB=DonR=DonB=RonB=GonR=GonB=RonG='\033[1;m\033['
WonR+='7;31;47m' # For drawing a white piece on a red background
WonB+='7;30;47m' # For drawing a white piece on a black background
DonR+='2;37;41m' # For drawing a dark piece on a red background
DonB+='2;37;40m' # For drawing a dark piece on a black background
GonR+='2;33;41m' # For drawing gold on a red background
GonB+='2;33;40m' # For drawing gold on a black background
RonG+='2;31;43m' # For drawing red on a gold background
RonB+='7;30;41m' # For drawing red on a black background
BonR+='0;30;41m' # For drawing black on a red background

def Black(x,w,c):
    """A function to print a chess piece on a black background.
        Inputs:
         x: A single-character string indicating the value to put in
            this square. It will be one of the following: " ", "♟",
            "♜", "♝", "♞", "♛", or "♚". (Note that " " is one of the
            options, and is used for empty squares.)
         w: A boolean value indicating whether this is a white piece.
         c: An integer indicating the column of this square. (We need
            to know this because the leftmost square (c=0) has gold 
            on the left side, and the rightmost square (c=7) has gold
            on the right side.

       Outputs:
       -To begin, in the one case that c=0, 3 spaces are printed. 
       -Next, regardless of c's value the one character passed in
        as x is printed, in the indicated color.
       -Finally, in the one case that c=7, a newline character is 
        printed.                                                  """
    if w:
        if c==0:
            print(Norm,"   ",Norm,GonB,L,Norm,WonB,x," ",Norm,sep="",end="")
        elif c==7:
            print(Norm,WonB,x," ",GonB,R,Norm,sep="")
        else:
            print(Norm,WonB,x," ",Norm,sep="",end="")
    else:
        if c==0:
            print(Norm,"   ",Norm,GonB,L,Norm,DonB,x," ",Norm,sep="",end="")
        elif c==7:
            print(Norm,DonB,x," ",GonB,R,Norm,sep="")
        else:
            print(Norm,DonB,x," ",Norm,sep="",end="")

    
def Red(x,w,c):
    """A function to print a chess piece on a red background.
        Inputs: These are the same as the inputs for Black()
         x: A string indicating the value to put in this square. 
         w: A boolean value indicating whether this is a white piece.
         c: An integer indicating the column of this square. 

       Outputs:
       -To begin, in the one case that c=0, 3 spaces are printed. 
       -Next, regardless of c's value, three characters always print:
         1: A "▐" character that is red on its right side, and that 
            is either gold (if c=0) or black (otherwise) on its left
            side.
         2: The character passed in as x, in the indicated color.
         3: A "▌" character that is red on its left side and that is
            either gold (if c=7) or black (otherwise) on its right
            side.
       -Finally, in the one case that c=7, a newline is printed.
        But somethings needs to be understood here. First, you don't 
        really need to print a "\n", you can just NOT use an "end=''"
        when printing this last "▌" piece. Second, you also need to 
        change the color to GonB before going to the next line, to 
        prevent colored bars from drawing on the left.            """
    if w:
        if c==0:
            print(Norm,"   ",Norm,GonR,L,Norm,WonR,x," ",Norm,RonB,L,Norm,sep="",end="")
        elif c==7:
            print(RonB,R,WonR,x," ",GonR,R,Norm,sep="")
        else:
            print(Norm,RonB,R,Norm,WonR,x," ",Norm,RonB,L,Norm,sep="",end="")
    else:
        if c==0:
            print(Norm,"   ",Norm,GonR,L,Norm,DonR,x," ",Norm,RonB,L,Norm,sep="",end="")
        elif c==7:
            print(RonB,R,DonR,x," ",GonR,R,Norm,sep="")
        else:
            print(Norm,RonB,R,Norm,DonR,x," ",Norm,RonB,L,Norm,sep="",end="")
def DrawBoard(B,W):
    """A function to draw a chess board with its pieces.
        Inputs:
         B: This is the board. It must be a list of 8 strings, which
            indicate the 8 rows of the chessboard. The 8 strings are
            each 8 characters wide, indicating the 8 rows of the
            chessboard. The individual characters in the strings are
            any of the following: " ","♟","♜","♝","♞","♛", or "♚".
         W: This is a list of 16 complex numbers. Each number encodes
            the row/column position of one of the 16 white pieces.
            (We don't need a similar list of dark pieces, because
            anything that is not white can print as dark.

       Outputs:
        The output is to print the eight rows of the board, along 
        with two more rows for the top and bottom gold border.    """
    
    def DrawRow(r,B,W):
        """A function to draw a single row of the chess board.
           Input:
            r: An integer indicating the row number.
            B: This is the board.
            W: This is a list of white piece locations.

           Outputs:
            The output is the printing of the indicated row.      """
        if r==0:
            print(Norm,"   ",Norm,GonB,BL*25,Norm,sep="")
            for column in range(8):
                for a in range(len(W)):
                    if r==W[a].real and column==W[a].imag:
                        if column%2 == 0:
                            Red(B[r][column],1,column)
                            break
                        else:
                            Black(B[r][column],1,column)
                            break
                if a==len(W)-1 and r!=W[a].real or column!=W[a].imag:        
                    if column%2 == 0:          
                           Red(B[r][column],0,column)
                    else:
                         Black(B[r][column],0,column)
        elif r==1:
            for column in range(8):
                for a in range(len(W)):
                    if r==W[a].real and column==W[a].imag:
                        if column%2==0:
                            Black(B[r][column],1,column)
                            break
                        else:
                            Red(B[r][column],1,column)
                            break
                if a==len(W)-1 and r!=W[a].real or column!=W[a].imag: 
                    if column%2==0:
                        Black(B[r][column],0,column)
                    else:
                        Red(B[r][column],0,column)        
        elif r==2:
            for column in range(8):
                for a in range(len(W)):
                    if r==W[a].real and column==W[a].imag:
                        if column%2==0:
                            Red(B[r][column],1,column)
                            break
                        else:
                            Black(B[r][column],1,column)
                            break
                if a==len(W)-1 and r!=W[a].real or column!=W[a].imag:        
                    if column%2==0:
                        Red(B[r][column],0,column)
                    else:
                        Black(B[r][column],0,column)
        elif r==3:
            for column in range(8):
                for a in range(len(W)):
                    if r==W[a].real and column==W[a].imag:
                        if column%2==0:
                            Black(B[r][column],1,column)
                            break
                        else:
                            Red(B[r][column],1,column)
                            break
                if a==len(W)-1 and r!=W[a].real or column!=W[a].imag:
                    if column%2==0:
                        Black(B[r][column],0,column)
                    else:
                        Red(B[r][column],0,column)       
        elif r==4:
            for column in range(8):
                for a in range(len(W)):
                    if r==W[a].real and column==W[a].imag:
                        if column%2==0:
                            Red(B[r][column],1,column)
                            break
                        else:
                            Black(B[r][column],1,column)
                            break
                if a==len(W)-1 and r!=W[a].real or column!=W[a].imag:
                    if column%2==0:
                        Red(B[r][column],0,column)
                    else:
                        Black(B[r][column],0,column)
        elif r==5:
            for column in range(8):
                for a in range(len(W)):
                    if r==W[a].real and column==W[a].imag:
                        if column%2==0:
                            Black(B[r][column],1,column)
                            break
                        else:
                            Red(B[r][column],1,column)
                            break
                if a==len(W)-1 and r!=W[a].real or column!=W[a].imag: 
                    if column%2==0:
                        Black(B[r][column],0,column)
                    else:
                        Red(B[r][column],0,column)        
        elif r==6:
            for column in range(8):
                for a in range(len(W)):
                    if r==W[a].real and column==W[a].imag:
                        if column%2==0:
                            Red(B[r][column],1,column)
                            break
                        else:
                            Black(B[r][column],1,column)
                            break
                if a==len(W)-1 and r!=W[a].real or column!=W[a].imag: 
                    if column%2==0:
                        Red(B[r][column],0,column)
                    else:
                        Black(B[r][column],0,column)        
        elif r==7:
            for column in range(8):
                for a in range(len(W)):
                    if r==W[a].real and column==W[a].imag:
                        if column%2==0:
                            Black(B[r][column],1,column)
                            break
                        else:
                            Red(B[r][column],1,column)
                            break
                if a==len(W)-1 and r!=W[a].real or column!=W[a].imag:
                    if column%2==0:
                        Black(B[r][column],0,column)
                    else:
                        Red(B[r][column],0,column)        
            print(Norm,"   ",Norm,GonB,TL*25,Norm,sep="",end="\n\n\n")
    for i in range(8):
        DrawRow(i,B,W)


def DrawAnInitialBoard():
    """A function to create and draw an initial board. This means the
       board is: ["♜♝♞♛♚♞♝♜","♟♟♟♟♟♟♟♟","        ","        ",
                  "        ","        ","♟♟♟♟♟♟♟♟","♜♝♞♛♚♞♝♜"].
       and it also means that the white pieces are in the last two 
       rows.

       But I have RULES for you to follow.
        1. You cannot use any string quotes and you cannot call the
           str function in your implementation. I am making this rule
           to give you experience with slicing and string operators.
           I want to point out that the P string holds the symbols
           that you need.
           (I also want to point out that you should *start* by using
           the above-provided 8 strings for your board. Only after
           you get that working should you then create again the list
           of strings, but this time without using quotes.)
        2: Try to use as few characters as possible to implement this
           function. I will grade on based on how few characters you
           use (ignoring spaces, tabs, and newlines). My solution
           uses 102 characters.                                   """
    B = [
         [P[2],P[3],P[4],P[5],P[6],P[4],P[3],P[2]],
         [P[1],P[1],P[1],P[1],P[1],P[1],P[1],P[1]],
         [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]],
         [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]],
         [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]],
         [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]],
         [P[1],P[1],P[1],P[1],P[1],P[1],P[1],P[1]],
         [P[2],P[3],P[4],P[5],P[6],P[4],P[3],P[2]]
        ]
    W=[6+0j,6+1j,6+2j,6+3j,6+4j,6+5j,6+6j,6+7j,7+0j,7+1j,7+2j,7+3j,7+4j,7+5j,7+6j,7+7j]
    DrawBoard(B,W)
   
#DrawAnInitialBoard()

def DrawRandomBoard():
    """A function to create and draw a board with all 32 pieces in
       random positions.                                          """
    def RandomPlacement(color,otherColor):
        """A function to randomly place the 16 pieces of one color.
            Inputs:
             color: An empty list that we'll add these 16 pieces to. 
             otherColor: The list for the other color. (This list 
                         will be empty on the first call and full on
                         the second call.)

            Outputs:
             The color list will now contain 16 complex numbers, to
             indicate the row/column positions of these pieces. 
             These numbers must be unique, occurring only once in
             either color or otherColor.
                                       """                            
        i=1
        while i<=16:
            a=randrange(0,8,1)
            b=randrange(0,8,1)
            if complex(a,b) not in color and complex(a,b) not in otherColor:          
                color.append(complex(a,b))
                i+=1
            
              
        
    seed(0) # Comment this line to make it run differently each time
    W=[];D=[];B=[] #This B object is the board.
    RandomPlacement(W, D)
    RandomPlacement(D, W)
   
    # Now that we know where the pieces go, we need to create the
    # eight rows of the board, inserting pieces into those spots.
    # Here, it does not matter how you decide to map the 16 pieces
    # of each color to the 16 positions in the W or D lists.
    B=[
       [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]],
       [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]],
       [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]],
       [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]],
       [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]],
       [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]],
       [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]],
       [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]]
      ]
    wTimes=0
    dTimes=0
    for i in range(8):
        for j in range(8):
            for a in range(16):
                if W[a].real==i and W[a].imag==j:
                    wTimes+=1
                    if wTimes<9:
                        B[i][j]=P[1]
                    elif wTimes<11:
                        B[i][j]=P[2]
                    elif wTimes<13:
                        B[i][j]=P[3]
                    elif wTimes<15:
                        B[i][j]=P[4]
                    elif wTimes<16:
                        B[i][j]=P[5]
                    elif wTimes<17:
                        B[i][j]=P[6]
            for a in range(16):                                          
                if D[a].real==i and D[a].imag==j:    
                    dTimes+=1
                    if dTimes<9:
                        B[i][j]=P[1]
                    elif dTimes<11:
                        B[i][j]=P[2]
                    elif dTimes<13:
                        B[i][j]=P[3]
                    elif dTimes<15:
                        B[i][j]=P[4]
                    elif dTimes<16:
                        B[i][j]=P[5]
                    elif dTimes<17:
                        B[i][j]=P[6]       
                   
            
       
    
    DrawBoard(B,W)
#DrawRandomBoard()

B = [
         [P[2],P[3],P[4],P[5],P[6],P[4],P[3],P[2]],
         [P[1],P[1],P[1],P[1],P[1],P[1],P[1],P[1]],
         [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]],
         [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]],
         [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]],
         [P[0],P[0],P[0],P[0],P[0],P[0],P[0],P[0]],
         [P[1],P[1],P[1],P[1],P[1],P[1],P[1],P[1]],
         [P[2],P[3],P[4],P[5],P[6],P[4],P[3],P[2]]
     ]
W=[6+0j,6+1j,6+2j,6+3j,6+4j,6+5j,6+6j,6+7j,7+0j,7+1j,7+2j,7+3j,7+4j,7+5j,7+6j,7+7j]
D=[0+0j,0+1j,0+2j,0+3j,0+4j,0+5j,0+6j,0+7j,1+0j,1+1j,1+2j,1+3j,1+4j,1+5j,1+6j,1+7j]

def SyntacticallyLegal(*theMove):
    lengthOfTheMove=len(theMove)
    if lengthOfTheMove==6:
        if (theMove[0]=='Q'or theMove[0]=='K'or theMove[0]=='N'or theMove[0]=='B'or theMove[0]=='R')and(theMove[1]>="a"and theMove[1]<="h"and theMove[4]>="a"and theMove[4]<="h")and(theMove[2]>='1' and theMove[2]<='8' and theMove[5]>='1' and theMove[5]<='8')and(theMove[3]=='x'):
            return True
        else: 
            return False
    elif lengthOfTheMove==5:
        if (theMove[0]=='Q'or theMove[0]=='K'or theMove[0]=='N'or theMove[0]=='B'or theMove[0]=='R')and(theMove[1]>="a"and theMove[1]<="h"and theMove[3]>="a"and theMove[3]<="h")and(theMove[2]>='1' and theMove[2]<='8' and theMove[4]>='1' and theMove[4]<='8'):        
            return True
        elif (theMove[0]=='Q'or theMove[0]=='K'or theMove[0]=='N'or theMove[0]=='B'or theMove[0]=='R')and(theMove[1]>="a"and theMove[1]<="h"and theMove[3]>="a"and theMove[3]<="h")and(theMove[4]>='1' and theMove[4]<='8')and(theMove[2]=='x'): 
            return True
        elif (theMove[0]=='Q'or theMove[0]=='K'or theMove[0]=='N'or theMove[0]=='B'or theMove[0]=='R')and(theMove[3]>="a"and theMove[3]<="h")and(theMove[1]>='1' and theMove[1]<='8' and theMove[4]>='1' and theMove[4]<='8')and(theMove[2]=='x'):
            return True
        elif (theMove[0]>="a"and theMove[0]<="h"and theMove[3]>="a"and theMove[3]<="h")and(theMove[1]>='1' and theMove[1]<='8' and theMove[4]>='1' and theMove[4]<='8')and(theMove[2]=='x'):
            return True
        else:
            return False
    elif lengthOfTheMove==4: 
        if (theMove[2]>="a"and theMove[2]<="h")and(theMove[0]>='1' and theMove[0]<='8' and theMove[3]>='1' and theMove[3]<='8')and(theMove[1]=='x'):
            return True
        elif (theMove[0]>="a"and theMove[0]<="h"and theMove[2]>="a"and theMove[2]<="h")and(theMove[3]>='1' and theMove[3]<='8')and(theMove[1]=='x'):
            return True
        elif (theMove[0]>="a"and theMove[0]<="h"and theMove[2]>="a"and theMove[2]<="h")and(theMove[1]>='1' and theMove[1]<='8' and theMove[3]>='1' and theMove[3]<='8'):
            return True
        elif (theMove[0]=='Q'or theMove[0]=='K'or theMove[0]=='N'or theMove[0]=='B'or theMove[0]=='R')and(theMove[2]>="a"and theMove[2]<="h")and(theMove[3]>='1' and theMove[3]<='8')and(theMove[1]=='x'):    
            return True
        elif (theMove[0]=='Q'or theMove[0]=='K'or theMove[0]=='N'or theMove[0]=='B'or theMove[0]=='R')and(theMove[2]>="a"and theMove[2]<="h")and(theMove[1]>='1' and theMove[1]<='8' and theMove[3]>='1' and theMove[3]<='8'):
            return True
        elif (theMove[0]=='Q'or theMove[0]=='K'or theMove[0]=='N'or theMove[0]=='B'or theMove[0]=='R')and(theMove[1]>="a"and theMove[1]<="h"and theMove[2]>="a"and theMove[2]<="h")and(theMove[3]>='1' and theMove[3]<='8'):
            return True
        else:
            return False
    elif lengthOfTheMove==3:
        if (theMove[1]>="a"and theMove[1]<="h")and(theMove[2]>='1' and theMove[2]<='8')and(theMove[0]=='x'): 
            return True
        elif (theMove[1]>="a"and theMove[1]<="h")and(theMove[0]>='1' and theMove[0]<='8' and theMove[2]>='1' and theMove[2]<='8'):         
            return True
        elif (theMove[0]>="a"and theMove[0]<="h"and theMove[1]>="a"and theMove[1]<="h")and(theMove[2]>='1' and theMove[2]<='8'):
            return True
        elif (theMove[0]=='Q'or theMove[0]=='K'or theMove[0]=='N'or theMove[0]=='B'or theMove[0]=='R')and(theMove[1]>="a"and theMove[1]<="h")and(theMove[2]>='1' and theMove[2]<='8'):            
            return True
        else:
            return False
    elif lengthOfTheMove==2:
        if (theMove[0]>="a"and theMove[0]<="h")and(theMove[1]>='1' and theMove[1]<='8'):
            return True
        else:
            return False 
                                                            
def SemanticallyLegal(color,*theMove):
    
    global B
    global W
    global D
       
    
    lengthOfTheMove=len(theMove)
    listOfTheMove=list(theMove)
    if listOfTheMove[lengthOfTheMove-1]=='8':
        listOfTheMove[lengthOfTheMove-1]=0
    elif listOfTheMove[lengthOfTheMove-1]=='7':
        listOfTheMove[lengthOfTheMove-1]=1
    elif listOfTheMove[lengthOfTheMove-1]=='6':
        listOfTheMove[lengthOfTheMove-1]=2
    elif listOfTheMove[lengthOfTheMove-1]=='5':
        listOfTheMove[lengthOfTheMove-1]=3        
    elif listOfTheMove[lengthOfTheMove-1]=='4':
        listOfTheMove[lengthOfTheMove-1]=4
    elif listOfTheMove[lengthOfTheMove-1]=='3':
        listOfTheMove[lengthOfTheMove-1]=5
    elif listOfTheMove[lengthOfTheMove-1]=='2':
        listOfTheMove[lengthOfTheMove-1]=6
    elif listOfTheMove[lengthOfTheMove-1]=='1':
        listOfTheMove[lengthOfTheMove-1]=7
            
    if listOfTheMove[lengthOfTheMove-2]=='a':
        listOfTheMove[lengthOfTheMove-2]=0
    elif listOfTheMove[lengthOfTheMove-2]=='b':
        listOfTheMove[lengthOfTheMove-2]=1
    elif listOfTheMove[lengthOfTheMove-2]=='c':
        listOfTheMove[lengthOfTheMove-2]=2
    elif listOfTheMove[lengthOfTheMove-2]=='d':
        listOfTheMove[lengthOfTheMove-2]=3        
    elif listOfTheMove[lengthOfTheMove-2]=='e':
        listOfTheMove[lengthOfTheMove-2]=4
    elif listOfTheMove[lengthOfTheMove-2]=='f':
        listOfTheMove[lengthOfTheMove-2]=5
    elif listOfTheMove[lengthOfTheMove-2]=='g':
        listOfTheMove[lengthOfTheMove-2]=6
    elif listOfTheMove[lengthOfTheMove-2]=='h':
        listOfTheMove[lengthOfTheMove-2]=7
         
    whitePawnInitial=[6+0j,6+1j,6+2j,6+3j,6+4j,6+5j,6+6j,6+7j]
    darkPawnInitial=[1+0j,1+1j,1+2j,1+3j,1+4j,1+5j,1+6j,1+7j]     
         
    endPointRow= listOfTheMove[lengthOfTheMove-1]
    endPointCol= listOfTheMove[lengthOfTheMove-2]
    tempPointRow=endPointRow
    tempPointCol=endPointCol
    endPoint=complex(endPointRow,endPointCol)
    
    if endPoint in W:
        checkEndPointColor=1  #end point is white piece
    elif endPoint in D:
        checkEndPointColor=2  #end point is dark piece
    else:
        checkEndPointColor=3  #end point is empty
        
    if 'x' in listOfTheMove:
        if color=="white":#find white start point
            if checkEndPointColor==1:
                return None
            elif checkEndPointColor==2:#only with white piece
                if listOfTheMove[0]=='K':
                    endPointRow+=1
                    if endPointRow>7:
                        endPointRow=tempPointRow
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)    
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                                
                    endPointRow-=1        
                    if endPointRow<0:
                        endPointRow=tempPointRow
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    endPointCol+=1
                    if endPointCol>7:
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                            
                    endPointCol-=1
                    if endPointCol<0:                    
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                            
                    endPointRow+=1
                    endPointCol+=1
                    if endPointRow>7 or    endPointCol>7:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol    
                    
                    endPointRow+=1
                    endPointCol-=1
                    if endPointRow>7 or    endPointCol<0:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                            
                    endPointRow-=1    
                    endPointCol+=1
                    if endPointRow<0 or    endPointCol>7:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                        
                    endPointRow-=1
                    endPointCol-=1
                    if endPointRow<0 or    endPointCol<0:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                elif listOfTheMove[0]=='Q':
                    while 1:
                        endPointRow+=1
                        if endPointRow>7:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1        
                        if endPointRow<0:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol+=1
                        if endPointCol>7:
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol-=1
                        if endPointCol<0:                    
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol+=1
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol-=1
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1    
                        endPointCol+=1
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=1
                        endPointCol-=1
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                elif listOfTheMove[0]=='B':
                    while 1:
                        endPointRow+=1
                        endPointCol+=1
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol-=1
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1    
                        endPointCol+=1
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=1
                        endPointCol-=1
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                elif listOfTheMove[0]=='R':
                    while 1:
                        endPointRow+=1
                        if endPointRow>7:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1        
                        if endPointRow<0:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol+=1
                        if endPointCol>7:
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol-=1
                        if endPointCol<0:                    
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                elif listOfTheMove[0]=='N':
                    while 1:
                        endPointRow+=2
                        endPointCol+=1
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=2
                        endPointCol-=1
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=2    
                        endPointCol+=1
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=2
                        endPointCol-=1
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol+=2
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol-=2
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1    
                        endPointCol+=2
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=1
                        endPointCol-=2
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                else:#pawn
                    endPointRow+=1
                    endPointCol-=1
                    if endPointRow>7 or    endPointCol<0:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[1] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    endPointRow+=1
                    endPointCol+=1
                    if endPointRow>7 or    endPointCol>7:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[1] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                                                
            else:
                return None
        elif color=="black":#find dark start point
            if checkEndPointColor==1:#only with black piece
                if listOfTheMove[0]=='K':
                    endPointRow+=1
                    if endPointRow>7:
                        endPointRow=tempPointRow
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                                
                    endPointRow-=1        
                    if endPointRow<0:
                        endPointRow=tempPointRow
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    endPointCol+=1
                    if endPointCol>7:
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                            
                    endPointCol-=1
                    if endPointCol<0:                    
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                            
                    endPointRow+=1
                    endPointCol+=1
                    if endPointRow>7 or    endPointCol>7:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol    
                    
                    endPointRow+=1
                    endPointCol-=1
                    if endPointRow>7 or    endPointCol<0:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                            
                    endPointRow-=1    
                    endPointCol+=1
                    if endPointRow<0 or    endPointCol>7:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                        
                    endPointRow-=1
                    endPointCol-=1
                    if endPointRow<0 or    endPointCol<0:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                elif listOfTheMove[0]=='Q':
                    while 1:
                        endPointRow+=1
                        if endPointRow>7:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)        
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1        
                        if endPointRow<0:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol+=1
                        if endPointCol>7:
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol-=1
                        if endPointCol<0:                    
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol+=1
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol-=1
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1    
                        endPointCol+=1
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=1
                        endPointCol-=1
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                elif listOfTheMove[0]=='B':
                    while 1:
                        endPointRow+=1
                        endPointCol+=1
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol-=1
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1    
                        endPointCol+=1
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=1
                        endPointCol-=1
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                elif listOfTheMove[0]=='R':
                    while 1:
                        endPointRow+=1
                        if endPointRow>7:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1        
                        if endPointRow<0:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol+=1
                        if endPointCol>7:
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol-=1
                        if endPointCol<0:                    
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                elif listOfTheMove[0]=='N':
                    while 1:
                        endPointRow+=2
                        endPointCol+=1
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=2
                        endPointCol-=1
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=2    
                        endPointCol+=1
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=2
                        endPointCol-=1
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol+=2
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol-=2
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1    
                        endPointCol+=2
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=1
                        endPointCol-=2
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                else:#pawn
                    endPointRow-=1
                    endPointCol+=1
                    if endPointRow>7 or    endPointCol<0:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[1] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    endPointRow-=1
                    endPointCol-=1
                    if endPointRow>7 or    endPointCol>7:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[1] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
            elif checkEndPointColor==2:
                return None
            else:
                return None        
    elif 'x' not in listOfTheMove:
        if checkEndPointColor==3:#with white and black piece
            if color=="white":
                if listOfTheMove[0]=='K':
                    endPointRow+=1
                    if endPointRow>7:
                        endPointRow=tempPointRow
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                                
                    endPointRow-=1        
                    if endPointRow<0:
                        endPointRow=tempPointRow
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    endPointCol+=1
                    if endPointCol>7:
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                            
                    endPointCol-=1
                    if endPointCol<0:                    
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                            
                    endPointRow+=1
                    endPointCol+=1
                    if endPointRow>7 or    endPointCol>7:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol    
                    
                    endPointRow+=1
                    endPointCol-=1
                    if endPointRow>7 or    endPointCol<0:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                            
                    endPointRow-=1    
                    endPointCol+=1
                    if endPointRow<0 or    endPointCol>7:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                        
                    endPointRow-=1
                    endPointCol-=1
                    if endPointRow<0 or    endPointCol<0:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in W):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                elif listOfTheMove[0]=='Q':
                    while 1:
                        endPointRow+=1
                        if endPointRow>7:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1        
                        if endPointRow<0:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol+=1
                        if endPointCol>7:
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol-=1
                        if endPointCol<0:                    
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol+=1
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol-=1
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1    
                        endPointCol+=1
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=1
                        endPointCol-=1
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                elif listOfTheMove[0]=='B':
                    while 1:
                        endPointRow+=1
                        endPointCol+=1
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol-=1
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1    
                        endPointCol+=1
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=1
                        endPointCol-=1
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                elif listOfTheMove[0]=='R':
                    while 1:
                        endPointRow+=1
                        if endPointRow>7:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1        
                        if endPointRow<0:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol+=1
                        if endPointCol>7:
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol-=1
                        if endPointCol<0:                    
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                elif listOfTheMove[0]=='N':
                    while 1:
                        endPointRow+=2
                        endPointCol+=1
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=2
                        endPointCol-=1
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=2    
                        endPointCol+=1
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=2
                        endPointCol-=1
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol+=2
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol-=2
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1    
                        endPointCol+=2
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=1
                        endPointCol-=2
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in W):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                else:#pawn
                    endPointRow+=2
                    if endPointRow>7:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[1] and (complex(endPointRow,endPointCol)in W) and (complex(endPointRow,endPointCol) in whitePawnInitial):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    endPointRow+=1
                    if endPointRow>7:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[1] and (complex(endPointRow,endPointCol)in W) :
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
            elif color=="black":
                if listOfTheMove[0]=='K':
                    endPointRow+=1
                    if endPointRow>7:
                        endPointRow=tempPointRow
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                                
                    endPointRow-=1        
                    if endPointRow<0:
                        endPointRow=tempPointRow
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    endPointCol+=1
                    if endPointCol>7:
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                            
                    endPointCol-=1
                    if endPointCol<0:                    
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                            
                    endPointRow+=1
                    endPointCol+=1
                    if endPointRow>7 or    endPointCol>7:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol    
                    
                    endPointRow+=1
                    endPointCol-=1
                    if endPointRow>7 or    endPointCol<0:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                            
                    endPointRow-=1    
                    endPointCol+=1
                    if endPointRow<0 or    endPointCol>7:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                        
                    endPointRow-=1
                    endPointCol-=1
                    if endPointRow<0 or    endPointCol<0:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[6] and (complex(endPointRow,endPointCol)in D):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                elif listOfTheMove[0]=='Q':
                    while 1:
                        endPointRow+=1
                        if endPointRow>7:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1        
                        if endPointRow<0:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol+=1
                        if endPointCol>7:
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol-=1
                        if endPointCol<0:                    
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol+=1
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol-=1
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1    
                        endPointCol+=1
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=1
                        endPointCol-=1
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[5] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                elif listOfTheMove[0]=='B':
                    while 1:
                        endPointRow+=1
                        endPointCol+=1
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol-=1
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1    
                        endPointCol+=1
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=1
                        endPointCol-=1
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[3] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                elif listOfTheMove[0]=='R':
                    while 1:
                        endPointRow+=1
                        if endPointRow>7:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1        
                        if endPointRow<0:
                            endPointRow=tempPointRow
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol+=1
                        if endPointCol>7:
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointCol-=1
                        if endPointCol<0:                    
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[2] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                elif listOfTheMove[0]=='N':
                    while 1:
                        endPointRow+=2
                        endPointCol+=1
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            break
                            endPointCol=tempPointCol
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=2
                        endPointCol-=1
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=2    
                        endPointCol+=1
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=2
                        endPointCol-=1
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol+=2
                        if endPointRow>7 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow+=1
                        endPointCol-=2
                        if endPointRow>7 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:
                        endPointRow-=1    
                        endPointCol+=2
                        if endPointRow<0 or    endPointCol>7:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    while 1:    
                        endPointRow-=1
                        endPointCol-=2
                        if endPointRow<0 or    endPointCol<0:
                            endPointRow=tempPointRow
                            endPointCol=tempPointCol
                            break
                        if B[endPointRow][endPointCol]==P[4] and (complex(endPointRow,endPointCol)in D):
                            return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                else:#pawn
                    endPointRow-=2
                    if endPointRow<0:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[1] and (complex(endPointRow,endPointCol)in D) and (complex(endPointRow,endPointCol) in darkPawnInitial):
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol
                    
                    endPointRow-=1
                    if endPointRow<0:
                        endPointRow=tempPointRow
                        endPointCol=tempPointCol
                    if B[endPointRow][endPointCol]==P[1] and (complex(endPointRow,endPointCol)in D) :
                        return complex(endPointRow,endPointCol)
                    endPointRow=tempPointRow
                    endPointCol=tempPointCol        
        else:
            return None    
                           
   
                
def Legal(color,*theMove):
    returnOfSyntacticallyLegal=SyntacticallyLegal(*theMove)
    returnOfSemanticallyLegal=SemanticallyLegal(color,*theMove)
    if returnOfSyntacticallyLegal==False or returnOfSemanticallyLegal==None :
        return False
    else:
        return returnOfSemanticallyLegal
            
def GetAMove(count,color=None):
    if color is None:
        color=[]
        if count%2!=0:
            color.append("white")
        else:
            color.append("black")    
    while 1:
        print("this turn is:",color[0])
        theMove=input("Enter your move:")
        listOfTheMove=list(theMove)
        lengthOfTheMove=len(theMove)
        
        if listOfTheMove[lengthOfTheMove-1]=='8':
            listOfTheMove[lengthOfTheMove-1]=0
        elif listOfTheMove[lengthOfTheMove-1]=='7':
            listOfTheMove[lengthOfTheMove-1]=1
        elif listOfTheMove[lengthOfTheMove-1]=='6':
            listOfTheMove[lengthOfTheMove-1]=2
        elif listOfTheMove[lengthOfTheMove-1]=='5':
            listOfTheMove[lengthOfTheMove-1]=3        
        elif listOfTheMove[lengthOfTheMove-1]=='4':
            listOfTheMove[lengthOfTheMove-1]=4
        elif listOfTheMove[lengthOfTheMove-1]=='3':
            listOfTheMove[lengthOfTheMove-1]=5
        elif listOfTheMove[lengthOfTheMove-1]=='2':
            listOfTheMove[lengthOfTheMove-1]=6
        elif listOfTheMove[lengthOfTheMove-1]=='1':
            listOfTheMove[lengthOfTheMove-1]=7
                
        if listOfTheMove[lengthOfTheMove-2]=='a':
            listOfTheMove[lengthOfTheMove-2]=0
        elif listOfTheMove[lengthOfTheMove-2]=='b':
            listOfTheMove[lengthOfTheMove-2]=1
        elif listOfTheMove[lengthOfTheMove-2]=='c':
            listOfTheMove[lengthOfTheMove-2]=2
        elif listOfTheMove[lengthOfTheMove-2]=='d':
            listOfTheMove[lengthOfTheMove-2]=3        
        elif listOfTheMove[lengthOfTheMove-2]=='e':
            listOfTheMove[lengthOfTheMove-2]=4
        elif listOfTheMove[lengthOfTheMove-2]=='f':
            listOfTheMove[lengthOfTheMove-2]=5
        elif listOfTheMove[lengthOfTheMove-2]=='g':
            listOfTheMove[lengthOfTheMove-2]=6
        elif listOfTheMove[lengthOfTheMove-2]=='h':
            listOfTheMove[lengthOfTheMove-2]=7
         
        
        
        returnOfLegal=Legal(color[0],*theMove)
        if returnOfLegal==False:
            continue
        else:
            tempList=[]
            tempList.append(complex(listOfTheMove[lengthOfTheMove-1],listOfTheMove[lengthOfTheMove-2]))
            tempList.append(returnOfLegal)
            return tempList
        
            
def PlayGame():
    count=0
    while 1:
        DrawBoard(B,W)
        count+=1
        returnOfGetAMove=GetAMove(count)#end first , start last
        if count%2!=0:#white turn
            for i in W:
                if returnOfGetAMove[1]==i:
                    W.remove(i)#delete start point
                    W.append(returnOfGetAMove[0])#add end point
            for j in D:
                if returnOfGetAMove[0]==j:
                    D.remove(j)
            B[int(returnOfGetAMove[0].real)][int(returnOfGetAMove[0].imag)]=B[int(returnOfGetAMove[1].real)][int(returnOfGetAMove[1].imag)]    
            B[int(returnOfGetAMove[1].real)][int(returnOfGetAMove[1].imag)]=P[0]
        elif count%2==0:#black turn
            for i in D:
                if returnOfGetAMove[1]==i:
                    D.remove(i)#delete start point
                    D.append(returnOfGetAMove[0])#add end point
            for j in W:        
                   if returnOfGetAMove[0]==j:
                    W.remove(j)
            B[int(returnOfGetAMove[0].real)][int(returnOfGetAMove[0].imag)]=B[int(returnOfGetAMove[1].real)][int(returnOfGetAMove[1].imag)]    
            B[int(returnOfGetAMove[1].real)][int(returnOfGetAMove[1].imag)]=P[0]
        

PlayGame()
