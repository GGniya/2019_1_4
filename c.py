# # 基本数据类型
# # a=10
# # b=3.14
# # c=True
# # d='a'
# # print(a)
# # print(type(a))
# # print(type(b))
# # print(type(c))
# # print(type(d))
# # list列表
# # 创建列表    列表中尽量存放同一类型的东西
# a=[]
# a=list()
# a=[10,20,30]
# a=['zhangshan','lisi','wangwu']
# a=[10,'zhangshan',3.14,True]
# # 2.向列表添加元素
# # insert 插入
# # append 追加        一般不用在意位置 使用更频繁
# # insert 参数1 index 索引，就是数字，一般从0开始
# #        参数2 object 对象 python里的所有东西都属于对象
# a.insert(0,40)  #  将40这个对象插入第0个位置
# a.insert(3,60)  #  将60这个对象插入第“3”个位置--实际是第“四”个位置
# a.insert(30,100) #如果索引超出范围，默认拼接在最后
# a.append('lisi') #追加到末尾
# print(a)
# 方案一
# citys=['郑州','北京','广州']
# print(citys)
# # 方案二
# citys=[]
# citys.append('郑州')
# citys.append('北京')
# citys.append('广州')
# citys.append('北京')
# print(citys)
# 3.删除
# remove 移除 移除符合条件的第一个对象
# pop 删除 表示删除第+1个元素-通过索引值删除对象(使用更频繁删除精确)
# print(citys)
# # citys.remove('北京')
# citys.pop(0)
# print(citys)
# 4.修改     (edit 编辑   modify 修改 update 更新)
# 列表名字[想要删除的索引值]='想要修改的值'
# citys[2]='深圳'
# print(citys)
# 5.查找  (find 查找 search 搜索  locate 定位)
#
# print('北京'in citys)
# print('拉萨' in citys)
# 列表整理
# 练习题目
# 1.创建一个空列表 imgs
# 2利用for循环向列表中追加10个元素,分别是001.jpg,002.j
# 3从列表中获取一个名称并下载(用print代替)
# 4下载成功并将其删除
import urllib.request
imgs=[]
for i in range(1,11):
    imgs.append(f'00{i}.jpg')
img_name=imgs[0]
print(f'{img_name}下载成功')
imgs.pop(0)


