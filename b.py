# 循环
# for i in range(10)       0-9
# for i in range（1,10)     1-9
# for i in range(1,11):
#     print(i)
# Ctrl+alt+L 代码格式规范整理
import urllib.request
# 下载网页
for i in range(1, 11):
    url = f'http://www.ivsky.com/tupian/index_{i}.html'
    url_path = f'{i}.html'
    urllib.request.urlretrieve(url, url_path)
    print(f'{i}下载成功')
