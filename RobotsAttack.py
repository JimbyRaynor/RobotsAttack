import math
import sys
import os
import time
import random
from tkinter import * 


sys.path.insert(0, "/home/deck/Documents") # needed to load LEDlib and Highscorelib
import LEDlib
import Highscorelib

# for loading files (.png, .txt), set current directory = location of this python script (needed for Linux)
current_script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_directory)

# TODO
#  introduce new enemies
# 3 men, new man each 2000      divide all scores by 10  so bonus 100,200,300

# teleporters
# ammo packs?
# zerg?
# Jim Raynor?
# Convert to PyGame, with sound, then GameMaker
# New font? Look at robotron temp score displays 1000, etc


# leave Math comments at end of each game
charRobotron = [(1,4,"#FF0000"), (1,5,"#FFFF00"), (1,6,"#FFFF00"), (1,7,"#FFFF00"), (2,4,"#FF0000"), (2,5,"#FF0000"), (2,11,"#FFFF00"), (3,1,"#90EE90"), (3,2,"#00FFFF"), (3,4,"#FFFFFF"), (3,5,"#FF0000"), (3,6,"#FF0000"), (3,9,"#FF0000"), (3,10,"#FF0000"), (3,11,"#FFFF00"), (4,0,"#FF0000"), (4,1,"#90EE90"), (4,2,"#00FFFF"), (4,3,"#FF0000"), (4,4,"#FF0000"), (4,5,"#FFFFFF"), (4,6,"#FF0000"), (4,7,"#FF0000"), (4,8,"#FF0000"), (4,9,"#FF0000"), (4,10,"#FF0000"), (4,11,"#FFFF00"), (5,0,"#FF0000"), (5,1,"#90EE90"), (5,2,"#00FFFF"), (5,3,"#FF0000"), (5,4,"#FF0000"), (5,5,"#FFFFFF"), (5,6,"#FFFFFF"), (5,7,"#FF0000"), (5,8,"#FF0000"), (6,0,"#FF0000"), (6,1,"#90EE90"), (6,2,"#00FFFF"), (6,3,"#FF0000"), (6,4,"#FF0000"), (6,5,"#FFFFFF"), (6,6,"#FF0000"), (6,7,"#FF0000"), (6,8,"#FF0000"), (6,9,"#FF0000"), (6,10,"#FF0000"), (6,11,"#FFFF00"), (7,1,"#90EE90"), (7,2,"#00FFFF"), (7,4,"#FFFFFF"), (7,5,"#FF0000"), (7,6,"#FF0000"), (7,9,"#FF0000"), (7,10,"#FF0000"), (7,11,"#FFFF00"), (8,4,"#FF0000"), (8,5,"#FF0000"), (8,11,"#FFFF00"), (9,4,"#FF0000"), (9,5,"#FFFF00"), (9,6,"#FFFF00"), (9,7,"#FFFF00")]
charRobotron2 = [(0,5,"#FFFFFF"), (0,6,"#FFFFFF"), (0,8,"#FF0000"), (0,9,"#FFFFFF"), (1,0,"#FF0000"), (1,1,"#FF0000"), (1,2,"#FF0000"), (1,4,"#FF0000"), (1,5,"#FF0000"), (1,6,"#FFFFFF"), (1,7,"#FF0000"), (1,9,"#FFFFFF"), (2,0,"#FF0000"), (2,1,"#FF0000"), (2,2,"#FF0000"), (2,3,"#FF0000"), (2,4,"#FF0000"), (2,5,"#FF0000"), (2,6,"#FF0000"), (3,0,"#FF0000"), (3,1,"#FFFFFF"), (3,2,"#FF0000"), (3,4,"#FF0000"), (3,5,"#FF0000"), (3,7,"#FF0000"), (3,8,"#FF0000"), (3,9,"#FFFFFF"), (4,0,"#FF0000"), (4,1,"#FFFFFF"), (4,2,"#FF0000"), (4,4,"#FF0000"), (4,5,"#FF0000"), (4,6,"#FFFFFF"), (4,9,"#FFFFFF"), (5,6,"#FFFFFF")]
charRobotron3 = [(1,8,"#AAAAAA"), (1,9,"#AAAAAA"), (1,10,"#AAAAAA"), (2,4,"#0000FF"), (2,5,"#0000FF"), (2,6,"#0000FF"), (2,7,"#FF0000"), (2,8,"#AAAAAA"), (2,9,"#AAAAAA"), (2,10,"#AAAAAA"), (3,0,"#FFFF00"), (3,1,"#FFFF00"), (3,2,"#FFFF00"), (3,3,"#0000FF"), (3,4,"#0000FF"), (3,5,"#0000FF"), (3,6,"#0000FF"), (3,7,"#0000FF"), (3,8,"#0000FF"), (3,9,"#0000FF"), (3,10,"#0000FF"), (3,11,"#FF0000"), (4,0,"#FFFF00"), (4,1,"#FF0000"), (4,2,"#FF0000"), (4,3,"#0000FF"), (4,4,"#0000FF"), (4,5,"#0000FF"), (4,6,"#0000FF"), (4,7,"#0000FF"), (4,8,"#0000FF"), (4,9,"#AAAAAA"), (4,10,"#AAAAAA"), (4,11,"#FF0000"), (5,0,"#FF0000"), (5,1,"#FFFFFF"), (5,2,"#FF0000"), (5,3,"#0000FF"), (5,4,"#0000FF"), (5,5,"#0000FF"), (5,6,"#0000FF"), (5,7,"#0000FF"), (5,8,"#0000FF"), (5,9,"#AAAAAA"), (5,10,"#AAAAAA"), (6,0,"#FF0000"), (6,1,"#FFFFFF"), (6,2,"#FF0000"), (6,3,"#0000FF"), (6,4,"#0000FF"), (6,5,"#0000FF"), (6,6,"#0000FF"), (6,7,"#0000FF"), (6,8,"#0000FF"), (6,9,"#0000FF"), (6,10,"#0000FF"), (6,11,"#FF0000"), (7,6,"#0000FF"), (7,7,"#FF0000"), (7,9,"#0000FF"), (7,10,"#0000FF"), (7,11,"#FF0000"), (8,6,"#0000FF"), (8,7,"#FF0000"), (8,11,"#FF0000")]
charRobotron4 = [(1,3,"#FFFF00"), (1,7,"#FFFFFF"), (1,8,"#F498EC"), (2,1,"#FFFF00"), (2,2,"#FFFF00"), (2,3,"#FFFF00"), (2,4,"#F498EC"), (2,5,"#F498EC"), (2,6,"#F498EC"), (2,7,"#F498EC"), (2,8,"#F498EC"), (2,9,"#FFFFFF"), (2,10,"#FFFFFF"), (2,11,"#FFFFFF"), (2,12,"#F498EC"), (3,0,"#FFFF00"), (3,1,"#FFFF00"), (3,2,"#FF0000"), (3,3,"#FF0000"), (3,4,"#F498EC"), (3,5,"#F498EC"), (3,6,"#F498EC"), (3,7,"#F498EC"), (3,8,"#F498EC"), (3,9,"#FFFFFF"), (3,10,"#FFFFFF"), (3,11,"#FFFFFF"), (3,12,"#F498EC"), (4,0,"#FFFF00"), (4,1,"#FF0000"), (4,2,"#90EE90"), (4,3,"#FF0000"), (4,4,"#F498EC"), (4,5,"#FF5900"), (4,6,"#FF5900"), (4,7,"#F498EC"), (4,8,"#90EE90"), (4,9,"#90EE90"), (5,0,"#FFFF00"), (5,1,"#FF0000"), (5,2,"#90EE90"), (5,3,"#FF0000"), (5,5,"#FF5900"), (5,6,"#FF5900"), (5,7,"#FFFFFF"), (5,8,"#90EE90"), (5,9,"#90EE90"), (5,10,"#FFFFFF"), (5,11,"#FFFFFF"), (5,12,"#F498EC"), (6,6,"#FF5900"), (6,7,"#FFFFFF"), (6,8,"#90EE90"), (6,9,"#90EE90"), (6,10,"#FFFFFF"), (6,11,"#FFFFFF"), (6,12,"#F498EC"), (7,8,"#90EE90"), (7,9,"#90EE90"), (7,12,"#F498EC")]

charMan = [(0,3,"#C19153"), (0,4,"#C19153"), (0,5,"#F498EC"), (0,6,"#FFFF00"), (1,3,"#C19153"), (1,4,"#C19153"), (1,5,"#F498EC"), (1,6,"#FFFF00"), (2,2,"#C19153"), (2,3,"#C19153"), (2,9,"#FFFF00"), (3,2,"#C19153"), (3,3,"#C19153"), (3,4,"#C19153"), (3,5,"#C19153"), (3,6,"#C19153"), (3,7,"#C19153"), (3,8,"#C19153"), (3,9,"#FFFF00"), (4,0,"#C19153"), (4,1,"#FFFF00"), (4,2,"#FFFF00"), (4,3,"#C19153"), (4,4,"#FF0000"), (4,5,"#C19153"), (4,6,"#FF0000"), (4,7,"#FF0000"), (4,8,"#C19153"), (4,9,"#FFFF00"), (5,0,"#C19153"), (5,1,"#FFFF00"), (5,2,"#FFFF00"), (5,3,"#FFFF00"), (5,4,"#C19153"), (5,5,"#C19153"), (5,6,"#C19153"), (6,0,"#C19153"), (6,1,"#FFFF00"), (6,2,"#FFFF00"), (6,3,"#FFFF00"), (6,4,"#C19153"), (6,5,"#C19153"), (6,6,"#C19153"), (7,0,"#C19153"), (7,1,"#FFFF00"), (7,2,"#FFFF00"), (7,3,"#C19153"), (7,4,"#FF0000"), (7,5,"#C19153"), (7,6,"#FF0000"), (7,7,"#FF0000"), (7,8,"#C19153"), (7,9,"#FFFF00"), (8,2,"#C19153"), (8,3,"#C19153"), (8,4,"#C19153"), (8,5,"#C19153"), (8,6,"#C19153"), (8,7,"#C19153"), (8,8,"#C19153"), (8,9,"#FFFF00"), (9,2,"#C19153"), (9,3,"#C19153"), (9,9,"#FFFF00"), (10,3,"#C19153"), (10,4,"#C19153"), (10,5,"#F498EC"), (10,6,"#FFFF00"), (11,3,"#C19153"), (11,4,"#C19153"), (11,5,"#F498EC"), (11,6,"#FFFF00")]
charBullet = [(0,11,"#FFFF00"), (1,11,"#C19153"), (2,11,"#FFFF00"), (3,11,"#FF0000"), (4,11,"#FFFF00"), (5,11,"#C19153"), (6,11,"#F498EC"), (7,11,"#C19153"), (8,11,"#FFFF00"), (9,11,"#FFFF00"), (10,11,"#FF0000"), (11,11,"#FFFF00"), (12,11,"#FFFF00"), (13,11,"#FF0000"), (14,11,"#F498EC"), (15,11,"#FFFF00"), (16,11,"#FF0000"), (17,11,"#FF0000"), (18,11,"#FFFF00"), (19,11,"#F498EC"), (20,11,"#AAAAAA"), (21,11,"#FFFF00"), (22,11,"#C19153"), (23,11,"#FFFF00")]

STEPD = 6 # speed of ship. This changes dx,dy.

MAXx = 800
MAXy = 600

STARTX = MAXx//2  # start location of human
STARTY = MAXy//2

LEVELSTART = 1   # change with start keys 1,2,3,...,9

mainwin = Tk()
mainwin.geometry(str(MAXx)+"x"+str(MAXy)) 
canvas1 = Canvas(mainwin,width=MAXx,height= MAXy,bg="black")
canvas1.place(x=0,y=0)

score = 0
bonusscore = 1000
highscore = Highscorelib.load_high_score("highscore.txt")
PlayerAlive = False
CanFire = True
RobotSpeed = 0.2
HUMANSPEED = 0.3


class SplitCharobj: # this object splits a char into two, lasting timealive milliseconds
    def __init__(self,mainwin, canvas,myChar,pixelsize,offset,x=0,y=0,dx=0,dy=0,timealive=1000):
        self.CharPoints = self.split(myChar,offset)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.CanMove = True
        self.LEDPoints = []        
        self.pixelsize = pixelsize
        self.canvas = canvas
        self.mainwin = mainwin
        self.currentindex = 0
        self.timealive = timealive
        self.mainwin.after(self.timealive,self.remove)
        self.move()
    def split(self,myChar,offset):
        newChar = []
        for x,y,z in myChar:
            if y % 2 == offset:
                newChar.append((x,y*4,z))
        return newChar
    def undraw(self):
        for p in self.LEDPoints:
            self.canvas.delete(p)
        self.LEDPoints.clear()
    def draw(self):
        self.undraw()
        LEDlib.psize = self.pixelsize
        LEDlib.createCharColourSolid(self.canvas,self.x,self.y,self.CharPoints,self.LEDPoints)
    def move(self):
        if self.CanMove:
           self.x = self.x + self.dx
           self.y = self.y + self.dy
           self.draw()
           self.mainwin.after(20,self.move) # move every 20 ms
    def remove(self):
        self.CanMove = False
        self.undraw()
        del self

class SparkScoreObj: # for displaying temporary score displays (when awarding points)
    def __init__(self,mainwin, canvas,x=0,y=0,score = 0, colour = "white",pixelsize =2, charwidth = 24, numzeros = 4,solid=False,bg = True,dx=0,dy=0,timealive=1000):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.colour = colour
        self.score = score
        self.CanMove = True
        self.numzeros = numzeros
        self.LEDPoints = []        
        self.pixelsize = pixelsize
        self.canvas = canvas
        self.mainwin = mainwin
        self.charwidth = charwidth
        self.solid = solid
        self.bg = bg
        self.currentindex = 0
        self.timealive = timealive
        self.mainwin.after(self.timealive,self.remove)
        self.move()
    def undraw(self):
        for p in self.LEDPoints:
            self.canvas.delete(p)
        self.LEDPoints.clear()
    def draw(self):
        self.undraw()
        LEDlib.psize = self.pixelsize
        LEDlib.charwidth = self.charwidth
        LEDlib.ShowColourScore2(self.canvas,self.x,self.y,self.colour,self.score,self.LEDPoints,self.numzeros,self.solid,self.bg)
    def move(self):
        if self.CanMove:
           self.x = self.x + self.dx
           self.y = self.y + self.dy
           self.draw()
           self.mainwin.after(20,self.move) # move every 20 ms
    def remove(self):
        self.CanMove = False
        self.undraw()
        del self
        
    
def on_close():
    Highscorelib.save_high_score(highscore,"highscore.txt")  # Save high score before exiting
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
myship.collisionrect = (2,2,20,18)
#myship.showcollisionrect()


scoreddisplay = []
enemylist = []
solidlist = []
bulletlist = []
robotlist = []
humanlist  = []
liveslist = []


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

def randyloc():
    return random.randint(53,MAXy-100)

def randxloc():
    return random.randint(20,MAXx-20)

def addship(i):
    liveslist.append(LEDlib.LEDobj(canvas1,340+i*30,20,dx = 0,dy = 0,CharPoints=charMan, pixelsize = 2,typestring = "human"))

def removeship():
     global PlayerAlive
     if len(liveslist) >= 1:
       lastship = liveslist[len(liveslist)-1]
       lastship.undraw()
       liveslist.remove(lastship)
     else:
       print("Game Over")
       PlayerAlive = False

for i in range(2):
      addship(i)

def createplayfield():
    for i in range(LEVELSTART+4):
      x = randxloc()
      y = randyloc()
      myrobot = LEDlib.LEDobj(canvas1,x,y,dx = 0,dy = 0,CharPoints=charRobotron, pixelsize = 2,typestring = "robot")
      myrobot.collisionrect = (0,0,21,25)
      #myrobot.showcollisionrect()
      robotlist.append(myrobot)
    Mikey = LEDlib.LEDobj(canvas1,randxloc(),randyloc(),dx = 0,dy = 0,CharPoints=charRobotron2, pixelsize = 2,typestring = "human")
    Mikey.collisionrect = (0,0,12,19)
    Mikey.dx = -HUMANSPEED
    #Mikey.showcollisionrect()
    Father = LEDlib.LEDobj(canvas1,randxloc(),randyloc(),dx = 0,dy = 0,CharPoints=charRobotron3, pixelsize = 2,typestring = "human")
    Father.collisionrect = (0,0,17,24)
    Father.dy = HUMANSPEED
    #Father.showcollisionrect()
    Mother = LEDlib.LEDobj(canvas1,randxloc(),randyloc(),dx = 0,dy = 0,CharPoints=charRobotron4, pixelsize = 2,typestring = "human")
    Mother.collisionrect = (0,0,17,25)
    Mother.dx = HUMANSPEED
    #Mother.showcollisionrect()
    humanlist.append(Mikey)
    humanlist.append(Father)
    humanlist.append(Mother)


def eraseplayfield():
    for itemlist in (enemylist, solidlist, humanlist, robotlist):
        for item in itemlist:
           item.undraw()
        itemlist.clear()
    
hitcounter = 0

def moverobots():
    for r in robotlist:
        if r.x < myship.x:
            r.x = r.x + RobotSpeed
        if r.y < myship.y:
            r.y = r.y + RobotSpeed
        if r.x > myship.x:
            r.x = r.x - RobotSpeed
        if r.y > myship.y:
            r.y = r.y - RobotSpeed
        r.draw()

def movehumans():
    for h in humanlist:
        h.move()
        if h.x < 0 : h.dx = -h.dx
        if h.y < 53 : h.dy = -h.dy
        if h.x > MAXx-20 : h.dx = -h.dx
        if h.y > MAXy-100 : h.dy = -h.dy
        if random.randint(0,100) > 95: 
            r = random.randint(0,5)
            if r == 0: h.dx = HUMANSPEED 
            if r == 1: h.dx = -HUMANSPEED 
            if r == 2: h.dx = 0 
            if r == 3: h.dy = HUMANSPEED
            if r == 4: h.dy = -HUMANSPEED
            if r == 5: h.dx = 0 


def gameloop():
    global  score, highscore, hitcounter, PlayerAlive, RobotSpeed, bonusscore, LEVELSTART
    if not PlayerAlive: return
    bulletstoremove = []
    robotstoremove = []
    for bullet in bulletlist:
        if bullet.x > MAXx or bullet.x < 0 or bullet.y < 0 or bullet.y > MAXy:
           bulletstoremove.append(bullet)
        for myrobot in robotlist:
           if checkcollisionPointsinRect(bullet,myrobot,myrobot.pixelsize):
              SplitCharobj(mainwin, canvas1,myrobot.CharPoints,myrobot.pixelsize,offset=0,x=myrobot.x,y=myrobot.y,dx=-bullet.dy,dy=bullet.dx,timealive=500)
              SplitCharobj(mainwin, canvas1,myrobot.CharPoints,myrobot.pixelsize,offset=1,x=myrobot.x,y=myrobot.y,dx=bullet.dy,dy=-bullet.dx,timealive=500)
              robotstoremove.append(myrobot)
              bulletstoremove.append(bullet) 
              RobotSpeed = RobotSpeed + 0.2 
              score = score + 10
              if score > highscore: 
                highscore = score
                displayhighscore.update(highscore)
              displayscore.update(score)   
        bullet.move()
    for myrobot in robotlist:
        if checkcollisionrect(myship,myrobot):
              removeship()
              if PlayerAlive:
                 setlevel()
    for b in bulletstoremove:
           if b in bulletlist: # b could have been added more than once to bulletstoremove, if it hits multiple enemies
             b.undraw()
             bulletlist.remove(b)
             del b
    for r in robotstoremove:
           if r in robotlist:
             r.undraw()
             robotlist.remove(r)
             del r      
    for human in humanlist:
       if checkcollisionrect(myship,human):
            #pointsawarded = LEDlib.LEDscoreobj(canvas1,x=human.x-7,y=human.y+10,score=bonusscore,colour="yellow",pixelsize=1, charwidth = 8, solid = True, bg = False)
            tempdisplay = SparkScoreObj(mainwin,canvas1,x=human.x-7,y=human.y+10,score = bonusscore, colour = "red", pixelsize = 1, charwidth = 8, solid = True,bg=False,dx=0,dy=-1,timealive=1000)
            #scoreddisplay.append(pointsawarded)
            human.undraw()
            humanlist.remove(human)
            score = score + bonusscore
            bonusscore = bonusscore + 1000
            if bonusscore > 5000: bonusscore = 5000
            if score > highscore: 
                highscore = score
                displayhighscore.update(highscore)
            displayscore.update(score)
    for solid in solidlist:
         if checkcollisionrect(myship,solid): 
            myship.dx = 0
            myship.dy = 0
            break # exit the for loop
    if len(robotlist) == 0:
        LEVELSTART += 1
        createplayfield
        setlevel()
    moverobots()
    movehumans()
    mainwin.after(30,gameloop)

def setlevel():
    global walls,pointsset,score, highscore, PlayerAlive, RobotSpeed, bonusscore
    eraseplayfield()
    createplayfield()
    myship.resetposition(STARTX,STARTY)
    displaylevel.update(LEVELSTART)
    PlayerAlive = True
    myship.dy = 0
    myship.dx = 0
    RobotSpeed = 0.2
    bonusscore = 1000

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
    bullet.CollisionPoints = [(0,11,0),(5,11,0),(10,11,0),(15,11,0),(20,11,0),(24,11,0)] # z is colour (ignored) for rotation
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
    if not PlayerAlive: return
    if key == "w":
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
    if not PlayerAlive or not CanFire: return
    makebullet(x=myship.x+12,y=myship.y+12,dx=24,dy=24,rotateangle=45)
    makebullet(x=myship.x+12,y=myship.y-36,dx=24,dy=-24,rotateangle=-45)
    makebullet(x=myship.x-24,y=myship.y-24,dx=-24,dy=-24,rotateangle=-45-90)
    makebullet(x=myship.x-36,y=myship.y+12,dx=-24,dy=24,rotateangle=-45)


mainwin.bind("<KeyPress>", mykey)
mainwin.bind("<space>", on_space)
mainwin.mainloop()