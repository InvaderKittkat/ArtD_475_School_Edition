#colors being used
#Canonical aubergine RGB(119,41,83)
#Carrot RGB(237,145,33)
#Celadon RGB(172,225,175)
#Dark tea green RGB(186,219,173)
def setup():
    size(500,500)
    smooth()
    background(119,41,83) 
    Critter()
    global x
    global y
    global w
    global h
    w = width
    h = height
def draw():

def Critter():
    ellipse(x,y,w)
