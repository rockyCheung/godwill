# -*- coding:utf-8 -*-
import random
from bchanges.conf.GuaCi import *


class BChanges(object):

    def __init__(self):
        pass
    #爻 yao
    def yoyo(self,seed):
        if seed == 0:
            seed = 10
        #change 1
        sky, land, human = bc.chaos(49, seed)
        sky, land, human = bc.change(sky, land, human)
        grass = sky + land
        #change 2
        sky, land, human = bc.chaos(grass, seed)
        sky, land, human = bc.change(sky, land, human)
        grass = sky + land
        #change 3
        sky, land, human = bc.chaos(grass, seed)
        sky, land, human = bc.change(sky, land, human)
        grass = sky + land
        return grass/4

    #变
    def change(self,sky,land,human):
        sky_change = sky%4
        land_change = land%4
        if sky_change == 0:
            sky_change = 4
        sky = sky - sky_change
        human = human + sky_change
        if land_change == 0:
            land_change = 4
        land = land - land_change
        human = human + land_change
        return sky,land,human

    #混沌初开，将49颗算子分为天、地、人三部分
    def chaos(self,grass,seed):
        sky = random.randrange(1,grass,seed)
        land = grass-sky-1
        human = 1
        return sky,land,human
    def drawYo(self,yo,pen,x,y):
        if yo == 0:
            pen.penup()
            pen.goto(x,y)
            pen.pendown()
            pen.forward(200)
        else:
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.forward(90)
            pen.penup()
            pen.goto(x+20, y)
            pen.pendown()
            pen.forward(90)

if __name__=="__main__":

    bc = BChanges()
    num = eval(input("Please intput first number:"))
    seed1 = int(num)
    yo1 = bc.yoyo(seed1)

    num = eval(input("Please intput second number:"))
    seed2 = int(num)
    yo2 = bc.yoyo(seed2)

    num = eval(input("Please intput third number:"))
    seed3 = int(num)
    yo3 = bc.yoyo(seed3)

    num = eval(input("Please intput fourth number:"))
    seed4 = int(num)
    yo4 = bc.yoyo(seed4)

    num = eval(input("Please intput fifth number:"))
    seed5 = int(num)
    yo5 = bc.yoyo(seed5)

    num = eval(input("Please intput sixth number:"))
    seed6 = int(num)
    yo6 = bc.yoyo(seed6)
    yoyo = "i_"+str(int(yo1)&1)+str(int(yo2)&1)+str(int(yo3)&1)+str(int(yo4)&1)+str(int(yo5)&1)+str(int(yo6)&1)
    print(yoyo)
    print("##########################################################################################################################################")

    # print yoyo
    for s in gua_ci[yoyo]:
        # t.write(str(s), font=("Arial", 10, "normal"))
        print((str(s)))
    print("##########################################################################################################################################")
    f = False
    try:
        f = open(DATA_PATH+'/gua_ci/'+yoyo, 'r')
        content = f.readlines()
        for i in content:
            print(i)
    finally:
        if f:
            f.close()
    print(
        "##########################################################################################################################################")

