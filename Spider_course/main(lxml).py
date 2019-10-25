#-*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import requests
from PIL import Image, ImageFont ,ImageDraw
from lxml import etree
'''
import imp
import sys
class ImportBlocker(object):

    def __init__(self, *args):
        self.black_list = args

    def find_module(self, name, path=None):
        if name in self.black_list:
            return self

        return None

    def load_module(self, name):
        module = imp.new_module(name)
        module.__all__ = [] # Necessary because of how bs4 inspects the module

        return module

sys.meta_path = [ImportBlocker('bs4.builder._htmlparser')]
from bs4 import BeautifulSoup
'''
Builder.load_string('''
<screen_login>:
    name:'login'
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            orientation: 'horizontal'
            padding: 20
            spacing: 20
            size_hint: (1, None)
            Label:
                text: 'username'
                font_size: 60
            TextInput:
                id: username
                multiline: False
        BoxLayout:
            orientation: 'horizontal'
            padding: 20
            spacing: 20
            size_hint: (1,None)
            Label:
                text: 'password'
                font_size: 60
            TextInput:
                id: password
                multiline: False
        BoxLayout:
            padding: 150
            Button:
                text:'login'
                font_size: 25
                bold: True
                on_press: app.spider_course()
<screen_image>: 
    name:'image'
    Image:
        nocache: True
        source: 'course.png'       
''')

class spider_session:
    def __init__(self,username,password):
        self.session(username,password)
        self.spider()
        self.data_img()

    def session(self,username,password):
        url = "http://www.sso.jwc.whut.edu.cn/Certification/login.do"
        datas = {'MsgID':'',
                 'KeyID':'',
                 'UserName':'',
                 'Password':'',
                 'rnd':'58834',
                 'return_EncData':'',
                 'code':'3207696148',
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
        self.res=[[],[],[],[],[]]
        root = etree.HTML(self.html.content.decode('utf-8'))
        course = root.xpath('.//tbody[@class="table-class-even"]')
        index = 0
        for each in course[0].findall('.//tr'):
            for child in each.xpath('.//td[@style="text-align: center"]'):
                temp_blue = child.find('.//div[@style="margin-top: 2px; font-size: 10px; color: blue"]')
                temp_red = child.find('.//div[@style="margin-top: 2px; font-size: 10px; color: red"]')
                if temp_blue or temp_red:
                    if temp_blue:
                        self.res[index].append(str(temp_blue.xpath('string()')).strip().replace('\t',''))
                    else:
                        self.res[index].append(str(temp_red.xpath('string()')).strip().replace('\t',''))
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

class screen_parent(ScreenManager):
    pass

class screen_login(Screen):
    pass

class screen_image(Screen):
    pass

sm = screen_parent()
s_login = screen_login(name = 'login')
sm.add_widget(s_login)




class courseApp(App):
    def spider_course(self):
        spider_session('0121809361804','aonelovesay52she')
        sm.add_widget(screen_image(name = 'image'))
        sm.current= 'image'

    def build(self):
        return sm
         
    


    
    


if __name__ == '__main__':
    courseApp().run()
