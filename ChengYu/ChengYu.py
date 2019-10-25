import sqlite3
from pypinyin import lazy_pinyin,pinyin
import random
import os
class idiom():
    def __init__(self):
        self.con = sqlite3.connect("cycd.db")
        self.cur = self.con.cursor()

    #str1为被参照成语，str2为参照成语
    def IsRight(self,str1,str2,dif):          
        self.cur.execute("select PingYin from cycd where ChengYu='"+str2+"'")
        temp = self.cur.fetchone()
        if temp:
            if dif == '1':
                if lazy_pinyin(str2)[0] == lazy_pinyin(str1)[-1]:
                    return True
                else:
                    return False
            elif dif == '2':
                self.Pyres_head = temp[0].split("  ")[0]
                self.cur.execute("select PingYin from cycd where ChengYu='"+str1+"'")
                self.Pyres_tail = self.cur.fetchone()[0].split("  ")[-1]
                if self.Pyres_head == self.Pyres_tail:
                    return True
                else:
                    return False
            elif dif == '3':
                 if str1[-1] == str2[0]:
                     return True
                 else:
                     return False
        else:
            return False                
   
    #电脑依据玩家成语选出成语,直接返回成语或返回False      
    def GetIdiom(self,str,dif):
        if dif == '1':
            fir_py = pinyin(str)[-1][0][0]                #缩小扫描范围
            self.cur.execute("select ChengYu from cycd where PingYin like'"+fir_py+"%'")
            list = self.cur.fetchall()
            Last_list = []
            for each in list: 
               if lazy_pinyin(each[0])[0] == lazy_pinyin(str)[-1]:
                    Last_list.append(each[0])
            if Last_list:
                return random.choice(Last_list)
            else:
                return False
        elif dif == '2':
            self.cur.execute("select PingYin from cycd where ChengYu='"+str+"'")
            res = self.cur.fetchone()[0].split("  ")[-1]
            self.cur.execute("select ChengYu,PingYin from cycd where PingYin Like '"+res+"  %'")
            list = self.cur.fetchall()
            Last_list = []
            if not list:
                return False
            for each in list:
                flag = each[1].split("  ")[-1]               #判断电脑给出成语是否有解
                self.cur.execute("select ChengYu,PingYin from cycd where PingYin Like '"+flag+"  %'")
                if self.cur.fetchone():
                    Last_list.append(each[0])
            if Last_list:
                return  random.choice(Last_list)
            else:
                print("这个成语你可得给我接好了~")
                return random.choice(list)[0]
        elif dif == '3':
            self.cur.execute("select ChengYu from cycd where ChengYu Like '"+str[-1]+"%'")
            list = self.cur.fetchall()
            if list:
                return random.choice(list)[0]
            else:
                return False
           
def Gamemain():
    Iobject = idiom()
    flag = 1
    first = 1
    print("welcome to 成语接龙!")
    while True:
        dif = input("请选择难度（其中1-简单，2--中等，3--困难）：")               #确保玩家输入数字
        if dif != '1' and dif != '2' and dif != '3':
            continue
        break
    while flag:
        Player_str = input("请输入你的成语:")
        if first:
            Iobject.cur.execute("select PingYin from cycd where ChengYu='"+Player_str+"'")
            temp = Iobject.cur.fetchone()
            if not temp:
                print("该成语不符合成语接龙游戏规则，请重新输入！")
                continue

        if not first:
            if not Iobject.IsRight(res,Player_str,dif):
                print("该成语不符合成语接龙游戏规则，请重新输入！")
                continue
        first = 0
        res = Iobject.GetIdiom(Player_str,dif)
        if res:
            print("电脑："+res)
            continue
        else:
            print("打得不错！")
            first = 1
            flag = int(input("是否重新开始？（重新开始输入1，否则输入0）"))
            if flag:
                first = 1
    os._exit(0)
          
if __name__ == '__main__':
    Gamemain()


            

