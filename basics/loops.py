# -*- coding: utf-8 -*-
\"\"\"循环语句练习\"\"\"

# ========== for 循环 ==========
print('--- for 循环 ---')

# 打印 0-4
for i in range(5):
    print(i)

# 遍历列表
fruits = ['苹果', '香蕉', '橙子']
for fruit in fruits:
    print(f'我喜欢吃: {fruit}')

# 使用 enumerate 获取索引
for index, fruit in enumerate(fruits):
    print(f'{index + 1}. {fruit}')

# ========== while 循环 ==========
print('\n--- while 循环 ---')

count = 0
while count < 5:
    print(f'计数: {count}')
    count += 1

# ========== 循环控制 ==========
print('\n--- 循环控制 ---')

for i in range(10):
    if i == 3:
        print(f'{i} 被跳过')
        continue     # 跳过这次
    if i == 7:
        print(f'{i} 时退出循环')
        break        # 退出循环
    print(i)

# ========== 列表推导式 ==========
print('\n--- 列表推导式 ---')

# 0-9 的平方
squares = [x**2 for x in range(10)]
print(f'平方: {squares}')

# 偶数
evens = [x for x in range(10) if x % 2 == 0]
print(f'偶数: {evens}')

# 包含字母的元组列表
words = ['hello', 'world', 'python']
result = [(w, len(w)) for w in words]
print(f'单词和长度: {result}')