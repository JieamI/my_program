import turtle as tt
import time
def Drawline(draw):          #绘制数码管的每一段
    tt.up()
    tt.fd(5)             #绘制每一段之间的间距
    if(draw):
        tt.down()
    else:
        tt.up()
    tt.fd(40)
    tt.up()
    tt.fd(5)             #绘制每一段之间的间距
    tt.right(90)

def Drawdigit(i):            #绘制数码管的每个数字
    if i in [2,3,4,5,6,8,9]:
        Drawline(True)
    else:
        Drawline(False)

    if i in [0,1,3,4,5,6,7,8,9]:
        Drawline(True)
    else:
        Drawline(False)

    if i in [0,2,3,5,6,8,9]:
        Drawline(True)
    else:
        Drawline(False)

    if i in [0,2,6,8]:
        Drawline(True)
    else:
        Drawline(False)

    tt.left(90)

    if i in [0,4,5,6,8,9]:
        Drawline(True)
    else:
        Drawline(False)

    if i in [0,2,3,5,6,7,8,9]:
        Drawline(True)
    else:
        Drawline(False)

    if i in [0,1,2,3,4,7,8,9]:
        Drawline(True)
    else:
        Drawline(False)

    tt.right(180)
    tt.penup()
    tt.fd(20)

def Number(num):
    list = []
    list.append(int(num / 10))
    list.append(num % 10)
    return list

def reset():
    tt.reset()
    tt.down()
    tt.fd(-50)
    


 
if __name__ == '__main__':
    n = 99
    while n >= 0:
        reset()
        tt.screensize(800,600, "black")
        tt.pensize(8)
        tt.pencolor("red")
        tt.hideturtle()
        tt.Turtle().screen.delay(0)
        Drawdigit(Number(n)[0])
        Drawdigit(Number(n)[1])
        time.sleep(1)
        n = n-1
    
     
        









   