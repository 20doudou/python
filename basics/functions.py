# -*- coding: utf-8 -*-
\"\"\"函数定义与调用练习\"\"\"

# ========== 基础函数 ==========
def greet(name):
    \"\"\"打招呼函数\"\"\"
    return f'你好, {name}!'

print(greet('小明'))

# ========== 默认参数 ==========
def greet_with_title(name, title='同学'):
    return f'你好, {title}{name}!'

print(greet_with_title('小红', '老师'))
print(greet_with_title('小刚'))  # 使用默认参数

# ========== 可变参数 ==========
def sum_all(*numbers):
    \"\"\"求所有数字的和\"\"\"
    total = 0
    for n in numbers:
        total += n
    return total

print(f'求和: 1+2+3 = {sum_all(1, 2, 3)}')
print(f'求和: 1+2+3+4+5 = {sum_all(1, 2, 3, 4, 5)}')

# ========== 关键字参数 ==========
def print_info(**info):
    \"\"\"打印键值对信息\"\"\"
    for key, value in info.items():
        print(f'{key}: {value}')

print_info(name='小明', age=18, city='北京')

# ========== 匿名函数 ==========
square = lambda x: x ** 2
print(f'lambda: 5的平方 = {square(5)}')

# 配合 map 使用
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f'map + lambda: {squared}')

# ========== 递归函数 ==========
def factorial(n):
    \"\"\"计算阶乘\"\"\"
    if n <= 1:
        return 1
    return n * factorial(n - 1)

for i in range(1, 6):
    print(f'{i}! = {factorial(i)}')