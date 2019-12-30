# -*- coding: UTF-8 -*-
import lxml
from bs4 import BeautifulSoup

'''
2019年12月14日 17:29:52
ROCEYS
Youtube视频页面HTML解析脚本
生成URL+tab+标题输出
'''

soup = BeautifulSoup(open('有水印视频列表.txt'),features='lxml')

#获取所有视频标题
titles = soup.find_all(id='video-title')

#获取所有视频url
urls = soup.find_all(class_='yt-simple-endpoint style-scope ytd-playlist-video-renderer')
print('数量：{}'.format(len(urls)))

u = []
for a in urls:
    u.append(a['href'].split('&')[0])

t = []
for b in titles:
    t.append(b.string)

i = 0
with open('华农兄弟带水印视频URL标题合集.txt', 'wt', encoding='utf8') as sfile:
    while i < 360:
        print('{}\t{}'.format(u[i],t[i]),file=sfile)
        i+=1