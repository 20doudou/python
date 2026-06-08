# -*- coding: utf-8 -*-
\"\"\"变量与数据类型练习\"\"\"

# ========== 基本数据类型 ==========
name = '小明'           # 字符串
age = 18                # 整数
height = 1.75           # 浮点数
is_student = True        # 布尔值

print(f'姓名: {name}')
print(f'年龄: {age} 岁')
print(f'身高: {height} 米')
print(f'是学生: {is_student}')

# ========== 容器类型 ==========
# 列表 (可以修改)
fruits = ['苹果', '香蕉', '橙子']
print(f'水果列表: {fruits}')
fruits.append('葡萄')
print(f'添加后: {fruits}')

# 元组 (不可修改)
colors = ('红色', '绿色', '蓝色')
print(f'颜色元组: {colors}')

# 集合 (去重)
numbers = {1, 2, 3, 3, 3}
print(f'集合(自动去重): {numbers}')

# 字典 (键值对)
person = {
    'name': '小红',
    'age': 20,
    'city': '上海'
}
print(f'字典: {person}')
print(f'姓名: {person[\"name\"]}')

# ========== 类型转换 ==========
x = '100'
y = int(x)          # 字符串转整数
z = float(x)        # 字符串转浮点数
s = str(y)          # 整数转字符串

print(f'类型转换: {x} -> int: {y} -> float: {z} -> str: {s}')