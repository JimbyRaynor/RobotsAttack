import math
import sys
import os
import time
from tkinter import * 

sys.path.insert(0, "/home/deck/Documents") # needed to load LEDlib
import LEDlib

# for loading files (.png, .txt), set current directory = location of this python script (needed for Linux)
current_script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_directory)

# TODO
# auto move from closest enemy
# teleporters
# ammo packs?
# zerg?
# Jim Raynor?



# leave Math comments at end of each game
charRobotron = [(1,4,"#FF0000"), (1,5,"#FFFF00"), (1,6,"#FFFF00"), (1,7,"#FFFF00"), (2,4,"#FF0000"), (2,5,"#FF0000"), (2,11,"#FFFF00"), (3,1,"#90EE90"), (3,2,"#00FFFF"), (3,4,"#FFFFFF"), (3,5,"#FF0000"), (3,6,"#FF0000"), (3,9,"#FF0000"), (3,10,"#FF0000"), (3,11,"#FFFF00"), (4,0,"#FF0000"), (4,1,"#90EE90"), (4,2,"#00FFFF"), (4,3,"#FF0000"), (4,4,"#FF0000"), (4,5,"#FFFFFF"), (4,6,"#FF0000"), (4,7,"#FF0000"), (4,8,"#FF0000"), (4,9,"#FF0000"), (4,10,"#FF0000"), (4,11,"#FFFF00"), (5,0,"#FF0000"), (5,1,"#90EE90"), (5,2,"#00FFFF"), (5,3,"#FF0000"), (5,4,"#FF0000"), (5,5,"#FFFFFF"), (5,6,"#FFFFFF"), (5,7,"#FF0000"), (5,8,"#FF0000"), (6,0,"#FF0000"), (6,1,"#90EE90"), (6,2,"#00FFFF"), (6,3,"#FF0000"), (6,4,"#FF0000"), (6,5,"#FFFFFF"), (6,6,"#FF0000"), (6,7,"#FF0000"), (6,8,"#FF0000"), (6,9,"#FF0000"), (6,10,"#FF0000"), (6,11,"#FFFF00"), (7,1,"#90EE90"), (7,2,"#00FFFF"), (7,4,"#FFFFFF"), (7,5,"#FF0000"), (7,6,"#FF0000"), (7,9,"#FF0000"), (7,10,"#FF0000"), (7,11,"#FFFF00"), (8,4,"#FF0000"), (8,5,"#FF0000"), (8,11,"#FFFF00"), (9,4,"#FF0000"), (9,5,"#FFFF00"), (9,6,"#FFFF00"), (9,7,"#FFFF00")]
charMan = [(0,3,"#C19153"), (0,4,"#C19153"), (0,5,"#F498EC"), (0,6,"#FFFF00"), (1,3,"#C19153"), (1,4,"#C19153"), (1,5,"#F498EC"), (1,6,"#FFFF00"), (2,2,"#C19153"), (2,3,"#C19153"), (2,9,"#FFFF00"), (3,2,"#C19153"), (3,3,"#C19153"), (3,4,"#C19153"), (3,5,"#C19153"), (3,6,"#C19153"), (3,7,"#C19153"), (3,8,"#C19153"), (3,9,"#FFFF00"), (4,0,"#C19153"), (4,1,"#FFFF00"), (4,2,"#FFFF00"), (4,3,"#C19153"), (4,4,"#FF0000"), (4,5,"#C19153"), (4,6,"#FF0000"), (4,7,"#FF0000"), (4,8,"#C19153"), (4,9,"#FFFF00"), (5,0,"#C19153"), (5,1,"#FFFF00"), (5,2,"#FFFF00"), (5,3,"#FFFF00"), (5,4,"#C19153"), (5,5,"#C19153"), (5,6,"#C19153"), (6,0,"#C19153"), (6,1,"#FFFF00"), (6,2,"#FFFF00"), (6,3,"#FFFF00"), (6,4,"#C19153"), (6,5,"#C19153"), (6,6,"#C19153"), (7,0,"#C19153"), (7,1,"#FFFF00"), (7,2,"#FFFF00"), (7,3,"#C19153"), (7,4,"#FF0000"), (7,5,"#C19153"), (7,6,"#FF0000"), (7,7,"#FF0000"), (7,8,"#C19153"), (7,9,"#FFFF00"), (8,2,"#C19153"), (8,3,"#C19153"), (8,4,"#C19153"), (8,5,"#C19153"), (8,6,"#C19153"), (8,7,"#C19153"), (8,8,"#C19153"), (8,9,"#FFFF00"), (9,2,"#C19153"), (9,3,"#C19153"), (9,9,"#FFFF00"), (10,3,"#C19153"), (10,4,"#C19153"), (10,5,"#F498EC"), (10,6,"#FFFF00"), (11,3,"#C19153"), (11,4,"#C19153"), (11,5,"#F498EC"), (11,6,"#FFFF00")]
charBullet = [(0,11,"#FFFF00"), (1,11,"#C19153"), (2,11,"#FFFF00"), (3,11,"#FF0000"), (4,11,"#FFFF00"), (5,11,"#C19153"), (6,11,"#F498EC"), (7,11,"#C19153"), (8,11,"#FFFF00"), (9,11,"#FFFF00"), (10,11,"#FF0000"), (11,11,"#FFFF00"), (12,11,"#FFFF00"), (13,11,"#FF0000"), (14,11,"#F498EC"), (15,11,"#FFFF00"), (16,11,"#FF0000"), (17,11,"#FF0000"), (18,11,"#FFFF00"), (19,11,"#F498EC"), (20,11,"#AAAAAA"), (21,11,"#FFFF00"), (22,11,"#C19153"), (23,11,"#FFFF00")]


STEPD = 6 # speed of characters. This changes dx,dy.

MAXx = 800
MAXy = 600

STARTX = MAXx//2  # start location of human
STARTY = MAXy//2

LEVELSTART = 0   # change with start keys 1,2,3,...,9

mainwin = Tk()
mainwin.geometry(str(MAXx)+"x"+str(MAXy)) 
canvas1 = Canvas(mainwin,width=MAXx,height= MAXy,bg="black")
canvas1.place(x=0,y=0)

score = 0
highscore = 0
PlayerAlive = False
CanFire = True



def save_high_score(myhighscore, filename=""):
    filename="highscore.txt"
    with open(filename, "w") as file:  # file is automatically closed when with block is completed
        file.write(str(myhighscore))

def load_high_score(filename=""):
    filename="highscore.txt"
    try:
        with open(filename, "r") as file:  # file is automatically closed when with block is completed
            return int(file.read())
    except FileNotFoundError:
        return 0  # Default to 0 if no high score file exists
    
def on_close():
    save_high_score(highscore)  # Save score before exiting
    mainwin.destroy()  # Close the window
mainwin.protocol("WM_DELETE_WINDOW", on_close)  # Bind closing action
       
def checkcollisionrect(object1,object2):
     x1,y1,x2,y2 = object1.collisionrect 
     a1,b1,a2,b2 = object2.collisionrect
     x1 = x1 + object1.x
     y1 = y1 + object1.y
     x2 = x2 + object1.x
     y2 = y2 + object1.y 
     a1 = a1 + object2.x
     b1 = b1 + object2.y
     a2 = a2 + object2.x
     b2 = b2 + object2.y 
     if x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2:
          return False
     else:
          return True
     
def checkcollisionPointsinRect(object1,object2,pixelsize):
    a1,b1,a2,b2 = object2.collisionrect
    a1 = a1 + object2.x
    b1 = b1 + object2.y
    a2 = a2 + object2.x
    b2 = b2 + object2.y
    for p in object1.RotatedCollisionPoints:
        x1 = p[0]*pixelsize + object1.x
        y1 = p[1]*pixelsize + object1.y
        if x1 >= a1 and x1 <= a2 and y1 >= b1 and y1 <= b2:
            return True
    return False
        

myship = LEDlib.LEDobj(canvas1,STARTX,STARTY,dx = 0,dy = 0,CharPoints=charMan, pixelsize = 2,typestring = "human")
myship.collisionrect = (4,3,44,45)

myrobot = LEDlib.LEDobj(canvas1,200,200,dx = 0,dy = 0,CharPoints=charRobotron, pixelsize = 2,typestring = "robot")
myrobot.collisionrect = (0,0,21,25)
myrobot.collisionrectshow = True
myrobot.draw()

scoreddisplay = []
enemylist = []
solidlist = []
bulletlist = []
      
displayscore = LEDlib.LEDscoreobj(canvas1,x=210,y=10,score=0,colour="white",pixelsize=3, charwidth = 24,numzeros=5)
displaytextscore = LEDlib.LEDtextobj(canvas1,x=235,y=35,text="SCORE",colour="yellow",pixelsize = 2, charwidth=14, solid = True)

displayhighscore = LEDlib.LEDscoreobj(canvas1,x=MAXx-121,y=10,score=highscore,colour="white",pixelsize=3, charwidth = 24,numzeros=5)
displaytexthighscore = LEDlib.LEDtextobj(canvas1,x=MAXx-105,y=35,text="HISCORE",colour="yellow",pixelsize = 2, charwidth=14, solid = True)

dlx = 50
displaylevel = LEDlib.LEDscoreobj(canvas1,x=MAXx//2+20+dlx,y=10,score=LEVELSTART,colour="white",pixelsize=3, charwidth = 24,numzeros=0)
displaytextlevel = LEDlib.LEDtextobj(canvas1,x=MAXx//2+dlx,y=35,text="LEVEL",colour="yellow",pixelsize = 2, charwidth=14, solid = True)

LEDpoints = []
LEDlib.psize=3
LEDlib.pixelline(canvas1,x=0,y=52,dx=1,dy=0,n= 267, colour= "light green", LEDpoints=LEDpoints)
LEDlib.pixelline(canvas1,x=0,y=MAXy-70,dx=1,dy=0,n= 267, colour= "light green", LEDpoints=LEDpoints)

line1 = "Robots Attack"
line1text = LEDlib.LEDtextobj(canvas1,x=4,y=100,text=line1,colour="light green",pixelsize = 4, charwidth=28)

def displaytitle():
    line1text.draw()

def undrawtitle():
    line1text.undraw()

def createplayfield():
    print("Make enemy robots and walls")
    #if stype == strawberrytype:
    #      fruit = LEDobj(canvas1,x*wallsize+8,y*wallsize+DOWNOFFSET,dx = 0,dy = 0,CharPoints=charPacmanStrawberry, pixelsize = 2,typestring = "fruit")
    #      fruit.collisionrect = (0,6,22,30)
    #      fruit.PointsType = 200
    #      #fruit.showcollisionrect()
    #      fruitlist.append(fruit)

def eraseplayfield():
    for itemlist in (enemylist, solidlist, scoreddisplay):
        for item in itemlist:
           item.undraw()
        itemlist.clear()
    
hitcounter = 0

def gameloop():
    global  score, highscore, hitcounter
    bulletstoremove = []
    for bullet in bulletlist:
        bullet.move()
        if bullet.x > MAXx or bullet.x < 0 or bullet.y < 0 or bullet.y > MAXy:
           bulletstoremove.append(bullet)
        if checkcollisionPointsinRect(bullet,myrobot,myrobot.pixelsize):
            hitcounter += 1
            print("hit",hitcounter) 
    for b in bulletstoremove:
           b.undraw()
           bulletlist.remove(b)
           del b
    for fruit in enemylist:
       if checkcollisionrect(myship,fruit):
            pointsawarded = LEDlib.LEDscoreobj(canvas1,x=fruit.x-7,y=fruit.y+10,score=fruit.PointsType,colour="yellow",pixelsize=2, charwidth = 15, solid = True, bg = False)
            scoreddisplay.append(pointsawarded)
            fruit.undraw()
            enemylist.remove(fruit)
            score = score + fruit.PointsType
            if score > highscore: 
                highscore = score
                displayhighscore.update(highscore)
            displayscore.update(score)
    for solid in solidlist:
         if checkcollisionrect(myship,solid): 
            myship.dx = 0
            myship.dy = 0
            break # exit the for loop
    mainwin.after(30,gameloop)

def setlevel():
    global walls,pointsset,score, highscore, PlayerAlive
    eraseplayfield()
    createplayfield()
    myship.resetposition(STARTX,STARTY)
    score = 0
    highscore = load_high_score()
    displaylevel.update(LEVELSTART)
    PlayerAlive = True
    myship.dy = 0
    myship.dx = 0

def reload():
    global CanFire
    CanFire = True
    mainwin.after(200,reload) 



setlevel()
gameloop()
reload()

def makebullet(x,y,dx,dy,rotateangle):
    global CanFire
    bullet = LEDlib.LEDobj(canvas1,x,y,dx,dy,CharPoints=charBullet, pixelsize = 2,typestring = "bullet")
    bullet.CollisionPoints = [(0,11,0),(10,11,0),(20,11,0),(24,11,0)] # z is colour (ignored) for rotation
    bullet.RotatedCollisionPoints = bullet.CollisionPoints.copy()
    bullet.rotate(rotateangle)
    #bullet.showcollisionlines()
    bulletlist.append(bullet)
    CanFire = False


# cannot easily do diagonals (only one key at a time is detected, pygame can detect multiple keypresses at once)
def mykey(event):
    global PlayerAlive,score, highscore, LEVELSTART, CanFire
    key = event.keysym.lower()
    if key in "0123456789":
        undrawtitle()
        if key == "0":
            displaytitle()
        LEVELSTART = int(key)
        setlevel()
    elif key == "w":
         myship.y += -STEPD
    elif key == "up" and CanFire:
         makebullet(x=myship.x-12,y=myship.y-30,dx=0,dy=-24,rotateangle=90)
    elif key == "d":
         myship.x += STEPD
    elif key == "right" and CanFire:
         makebullet(x=myship.x+6,y=myship.y-12,dx=24,dy=0,rotateangle=0)
    elif key == "a":
         myship.x += -STEPD
    elif key == "left" and CanFire:
         makebullet(x=myship.x-44,y=myship.y-12,dx=-24,dy=0,rotateangle=0)
    elif key == "s":
         myship.y += STEPD
    elif key == "down" and CanFire:
         makebullet(x=myship.x-12,y=myship.y+24,dx=0,dy=24,rotateangle=90)
    myship.draw()
       
# 4 direction shoot when space is pressed (limited ammo)
def on_space(event):
    global CanFire
    makebullet(x=myship.x+12,y=myship.y+12,dx=24,dy=24,rotateangle=45)
    makebullet(x=myship.x+12,y=myship.y-36,dx=24,dy=-24,rotateangle=-45)
    makebullet(x=myship.x-24,y=myship.y-24,dx=-24,dy=-24,rotateangle=-45-90)
    makebullet(x=myship.x-36,y=myship.y+12,dx=-24,dy=24,rotateangle=-45)


mainwin.bind("<KeyPress>", mykey)
mainwin.bind("<space>", on_space)
mainwin.mainloop()