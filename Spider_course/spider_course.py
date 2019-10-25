from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageFont ,ImageDraw
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By 

 #selenium模式
class spider_selenium:
    def __init__(self,username,password):
        self.selenium(username,password)
        self.spider()
        self.data_img()
    
    def selenium(self,username,password):             #登录网站并爬取网页
        bro = webdriver.Chrome()
        while True:
            bro.get("http://sso.jwc.whut.edu.cn/Certification/toIndex.do")
            if WebDriverWait(bro, 1, 0.5).until(EC.presence_of_element_located((By.ID,"username"))):
                break
        user_name = bro.find_element_by_id("username")
        pass_word = bro.find_element_by_id("password")
        login = bro.find_element_by_xpath("//*[@id='submit_id']")
        user_name.clear()
        user_name.send_keys(username)
        pass_word.clear() 
        pass_word.send_keys(password)
        login.click()
        WebDriverWait(bro, 10, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME,"table-class-even")))
        self.html = bro.page_source
        bro.quit()                              
    
    def spider(self):               #解析网页获取当周课表数据
        soup = BeautifulSoup(self.html,"html.parser")
        course = soup.select_one(".table-class-even")
        self.res=[[],[],[],[],[]]
        index = 0
        for each in course.find_all('tr',recursive=False):
            for child in each.find_all('td',{'style':'text-align: center'},recursive=False,limit=7):
                temp_blue = child.find('div',{'style':'margin-top: 2px; font-size: 10px; color: blue'})
                temp_red = child.find('div',{'style':'margin-top: 2px; font-size: 10px; color: red'}) 
                if temp_blue or temp_red:
                    if temp_blue:
                        self.res[index].append(temp_blue.get_text().strip().replace('\t',''))
                    else:
                        self.res[index].append(temp_red.get_text().strip().replace('\t',''))
                else:
                    self.res[index].append("None")
            index = index+1

    def data_img(self):             #将数据绘制在课表上
        img = Image.open("form.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('simhei.ttf',20)
        pos_x = 265.62
        pos_y = 270.9
        for each in self.res:
            for child in each:
                draw.text((pos_x, pos_y), child, fill = (255,0,255), font = font)
                pos_x = pos_x + 200
            pos_x = 265.6
            pos_y = pos_y + 220
        img.save("course.png")     
 
 #session模式
class spider_session:
    def __init__(self,username,password):
        self.session(username,password)
        self.spider()
        self.data_img()

    def session(self,username,password):
        #url = "http://www.sso.jwc.whut.edu.cn/Certification/login.do"
        url = 'http://202.114.50.129/Certification/login.do'
        datas = {'MsgID':'',
                 'KeyID':'',
                 'UserName':'',
                 'Password':'',
                 'rnd':'50582',
                 'return_EncData':'',
                 'code':'6579784907',
                 'userName1':'db14fb684f994923331aa060c27c3839',
                 'password1':'d54e22436a441097aa93d00ed8ca898ca4d1d075',
                 'webfinger':'ec198773ef514e44ed8cbf9ef7a114e7',
                 'type':'xs',
                 'userName':username,
                 'password':password}
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
                  'Connection': 'close'}
        bro = requests.session()
        self.html = bro.post(url,data = datas,headers = header)
     

    def spider(self):               #解析网页获取当周课表数据
        soup = BeautifulSoup(self.html.content,"lxml")
        course = soup.select_one(".table-class-even")
        self.res=[[],[],[],[],[]]
        index = 0
        for each in course.find_all('tr',recursive=False):
            for child in each.find_all('td',{'style':'text-align: center'},recursive=False,limit=7):
                temp_blue = child.find('div',{'style':'margin-top: 2px; font-size: 10px; color: blue'})
                temp_red = child.find('div',{'style':'margin-top: 2px; font-size: 10px; color: red'}) 
                if temp_blue or temp_red:
                    if temp_blue:
                        self.res[index].append(temp_blue.get_text().strip().replace('\t',''))
                    else:
                        self.res[index].append(temp_red.get_text().strip().replace('\t',''))
                else:
                    self.res[index].append("None")
            index = index+1

    def data_img(self):             #将数据绘制在课表上
        img = Image.open("form.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('simhei.ttf',20)
        pos_x = 265.62
        pos_y = 270.9
        for each in self.res:
            for child in each:
                draw.text((pos_x, pos_y), child, fill = (255,0,255), font = font)
                pos_x = pos_x + 200
            pos_x = 265.6
            pos_y = pos_y + 220
        img.save("course.png")      











