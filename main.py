import os
import requests # 要安装requests库
import urllib.request
from lxml import etree
# xpath路径 /html/body/div[4]/div/ul/li[1]/h3/a
# /html/body/div[4]/div/ul/li[1]/a
# /html/body/div[4]/div/ul/li[2]/a
# 获取青年大学习的id
# 请求地址
url = 'http://news.cyol.com/gb/channels/vrGlAKDl/index.html'
# 用户代理
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
# 定制请求头
request = urllib.request.Request(url=url,headers=headers)
# 发送请求访问服务器，返回响应对象
response = urllib.request.urlopen(request)
# 解码响应对象，得到页面源码
content = response.read().decode('utf-8')

# 解析服务器响应的文件
parse_html = etree.HTML(content)

# 编写xpath路径，获取想要的数据,xpath的返回值是列表类型
list = parse_html.xpath('/html/body/div[4]/div/ul/li[1]/a')
# 获得列表的第一个数据
list1 = parse_html.xpath('//a[@class="transition"]/@href')[0]
print(list)
print(list1)
print(len(list1))
i = 37
list2 = list1[36:46]
print(list2)

# 获取图片并保存
# 获取id后需要重新设置url
url_pre = "https://h5.cyol.com/special/daxuexi/" + list2 + "/images/end.jpg"
print(url_pre)
url = url_pre # 图片哪来

file = os.path.expanduser('~/Desktop/大学习自动抓取图片/qingnian.jpg') # 图片去哪

response = requests.get(url) # 请求图片
imgb = response.content # 图片的二进制数据
with open(file, 'wb') as img: # 打开文件
    img.write(imgb) # 写入文件
print("Success!")
# 再也不用担心 青年大学习没有学啦！！！！