x = 0;
def setup():
    size(500,500)
    
def draw():
    global x
    background(random(0,255))
    translate(250,250)
    strokeWeight(30)
    line(0,0,x,0)
    strokeWeight(1)
    ellipse(x,0,30,30)
    x = x + 1
