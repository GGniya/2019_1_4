# 目标 下载图片
# 1需要获取 src name
# 2图片相关信息在网页中
# 3需要下载网页

import requests  # 通过requests获取网页资源
import urllib.request
from lxml import etree

for a in range(10):
    url = f'http://www.ivsky.com/tupian/ziranfengjing_t2800/index_{a}.html'
    # 参数1 url.网址
    # 参数2 params 其他参数 默认为None
    # 参数3 **kwarms,
    content = requests.get(url).text
    print(content)
    root = etree.HTML(content)
    imgs = root.xpath('//img/@src')
    for i in range(18):
       urllib.request.urlretrieve(imgs[i], f'{a}00{i + 1}缩略图.jpg')  # 两个参数:一个下载链接/存储路径'+'存储文件名
       urllib.request.urlretrieve(imgs[i].replace('/t/', '/pre/'), f'{a}00{i + 1}高清图.jpg')
#         字符串替换 replace(a,b) 把a替换成b
