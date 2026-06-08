# 📋 Python 速查表

> 常用语法快速查阅，随用随查

## 变量与数据类型

| 类型 | 示例 | 转换函数 |
|------|------|----------|
| 整数 |  = 10 | int(x) |
| 浮点数 |  = 3.14 | loat(x) |
| 字符串 | s = 'hello' | str(x) |
| 布尔值 | lag = True | ool(x) |
| 列表 | lst = [1, 2, 3] | list(x) |
| 字典 | d = {'a': 1} | dict(x) |
| 元组 | 	 = (1, 2, 3) | 	uple(x) |
| 集合 | s = {1, 2, 3} | set(x) |

## 字符串操作

`python
s = "Hello World"

# 切片
s[0]       # 'H'
s[0:5]     # 'Hello'
s[::-1]    # 'dlroW olleH' (反转)

# 常用方法
s.upper()           # 'HELLO WORLD'
s.lower()          # 'hello world'
s.split(' ')        # ['Hello', 'World']
s.replace('World', 'Python')  # 'Hello Python'
s.strip()           # 去除首尾空格
len(s)              # 11 (长度)
f'Hello, {name}'   # 格式化字符串
`

## 列表操作

`python
lst = [1, 2, 3, 4, 5]

# 常用方法
lst.append(6)      # 末尾添加
lst.insert(0, 0)   # 指定位置插入
lst.pop()          # 末尾删除并返回
lst.remove(3)      # 删除第一个匹配的元素
lst.sort()         # 排序
lst.reverse()      # 反转
len(lst)           # 长度

# 列表推导式
[x**2 for x in range(10)]           # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]
`

## 字典操作

`python
d = {'name': 'Alice', 'age': 18, 'city': 'Beijing'}

# 常用操作
d['name']           # 'Alice' (获取)
d['gender'] = 'F'   # 添加/修改
d.pop('age')        # 删除
d.keys()           # dict_keys(['name', 'city', 'gender'])
d.values()         # dict_values(['Alice', 'Beijing', 'F'])
d.items()          # 键值对列表
'name' in d         # True (判断键是否存在)
`

## 条件与循环

`python
# 条件
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'

# for 循环
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for item in lst:
    print(item)

for i, item in enumerate(lst):
    print(f'{i}: {item}')

# while 循环
n = 0
while n < 5:
    print(n)
    n += 1

# 循环控制
for i in range(10):
    if i == 3:
        continue    # 跳过本次
    if i == 7:
        break       # 退出循环
    print(i)
`

## 函数定义

`python
def greet(name, greeting='Hello'):
    """"打招呼函数"""
    return f'{greeting}, {name}!'

# 默认参数、可变参数
def func(*args, **kwargs):
    print(args)    # (1, 2, 3)
    print(kwargs) # {'a': 1, 'b': 2}

# 匿名函数
square = lambda x: x ** 2
square(5)  # 25
`

## 文件操作

`python
# 读取
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    lines = f.readlines()

# 写入
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Hello\n')
    f.writelines(['line1\n', 'line2\n'])

# 追加
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write('new log\n')
`

## 异常处理

`python
try:
    result = 10 / 0
except ZeroDivisionError:
    print('除数不能为零')
except Exception as e:
    print(f'其他错误: {e}')
else:
    print('没有异常时执行')
finally:
    print('总是执行')
`

## 常用内置函数

`python
print()           # 输出
input()           # 输入
len()             # 长度
range(start, stop, step)  # 范围
sorted()          # 排序
reversed()        # 反转
abs()             # 绝对值
round()           # 四舍五入
min() / max()     # 最小/最大值
sum()             # 求和
type()            # 类型
isinstance()      # 类型判断
`

---

*来源：python 学习仓库 | 持续更新中*