# 目标:天气预报查询
# 1让用户输入查询的城市
# 2通过天气预报接口获取对应天气
import requests

city=input('请输入城市名称:')
url=f'http://api.map.baidu.com/telematics/v3/weather?location={city}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'
content = requests.get(url).text
print(content)