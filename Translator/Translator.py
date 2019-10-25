import urllib.request
import urllib.parse
import json

while True:
    text = input("请输入需要翻译的内容：")
    url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {'i':text,'doctype':'json'}
    head = { }
    head['Referer'] = 'http://fanyi.youdao.com'
    head['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    print("翻译结果是：%s" %(target['translateResult'][0][0]['tgt']))

