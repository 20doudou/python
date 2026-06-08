# -*- coding: utf-8 -*-
\"\"\"
for 循环 vs while 循环 — 完整对比练习
练习题：注册用户输入判断流程
\"\"\"

# ============================================================
# 一、for 循环的四种用法
# ============================================================

print('=' * 50)
print('  for 循环的四种用法')
print('=' * 50)

# 用法1：range() 遍历数字序列
print('\n--- 用法1: range() ---')

# range(stop) → 0 到 stop-1
print('range(5):', list(range(5)))           # [0,1,2,3,4]

# range(start, stop) → start 到 stop-1
print('range(2,8):', list(range(2,8)))       # [2,3,4,5,6,7]

# range(start, stop, step) → 带步长
print('range(0,10,2):', list(range(0,10,2))) # [0,2,4,6,8]
print('range(9,2,-2):', list(range(9,2,-2))) # [9,7,5,3] (倒序)

# 用法2：遍历列表/元组/字符串
print('\n--- 用法2: 遍历容器 ---')

fruits = ['苹果', '香蕉', '橙子']
for fruit in fruits:
    print(f'  我喜欢吃: {fruit}')

name = 'Python'
for char in name:
    print(char, end=' ')                     # P y t h o n
print()

# 用法3：enumerate() 获取索引 + 元素
print('\n--- 用法3: enumerate() ---')

fruits = ['苹果', '香蕉', '橙子']
for index, fruit in enumerate(fruits):
    print(f'  {index}: {fruit}')
# 输出:
#   0: 苹果
#   1: 香蕉
#   2: 橙子

# 用法4：zip() 同时遍历多个列表
print('\n--- 用法4: zip() ---')

names = ['小明', '小红', '小刚']
scores = [95, 88, 72]
for name, score in zip(names, scores):
    print(f'  {name}: {score}分')


# ============================================================
# 二、流程图代码实现 — 注册用户输入判断
# ============================================================

print('\n' + '=' * 50)
print('  流程图实现：注册用户输入判断')
print('=' * 50)

list_names = ['jack', 'tom', 'mary', 'lily']

# ------------------------------------------------------------
# 版本A：for 循环（固定次数）
# ------------------------------------------------------------
print('\n【版本 A】for 循环版（固定最多尝试5次）')
print('-' * 40)

for i in range(5):
    user = input('请输入用户名称: ')
    
    if user in list_names:
        print('✅ 输入正确提示 — 用户名有效!')
        break                                # 正确 → 结束循环
    else:
        print('❌ 用户名不存在，请重新输入')     # 错误 → 继续循环
else:
    # 注意！这是 for 的 else 子句：
    # 只有 for 循环「正常结束」（没被 break）才会执行
    print('⚠️ 输出输入错误5次提示 — 尝试次数已用完!')

# ------------------------------------------------------------
# 版本B：while 循环（条件控制）
# ------------------------------------------------------------
print('\n【版本 B】while 循环版（条件控制）')
print('-' * 40)

count = 0                                    # 计数器必须手动初始化!
max_attempts = 5                             # 最大尝试次数

while count < max_attempts:                  # 条件控制循环
    user = input('请输入用户名称: ')
    
    if user in list_names:
        print('✅ 输入正确提示 — 用户名有效!')
        break                                # 正确 → 结束循环
    else:
        print('❌ 用户名不存在，请重新输入')     # 错误 → 继续循环
        count += 1                           # 手动更新计数器! 忘了就死循环!
else:
    # while 的 else：条件为假时执行（即 count >= max_attempts）
    print('⚠️ 输出输入错误5次提示 — 尝试次数已用完!')


# ============================================================
# 三、for vs while 核心对比分析
# ============================================================

print('\n' + '=' * 50)
print('  for vs while 核心对比')
print('=' * 50)

comparison = '''
┌─────────────┬──────────────────┬──────────────────┐
│   对比维度   │    for 循环      │   while 循环      │
├─────────────┼──────────────────┼──────────────────┤
│ 本质        │ 遍历型           │ 条件型            │
│ 适用场景    │ 已知次数/遍历容器 │ 不确定次数/等条件 │
│ 循环变量    │ 自动管理         │ 必须手动初始化+更新│
│ 死循环风险  │ 低               │ 高                │
│ 可读性      │ 更直观           │ 需看条件逻辑       │
│ else 配合   │ 循环正常结束执行  │ 条件为假时执行     │
└─────────────┴──────────────────┴──────────────────┘

本质区别:
  for 循环 = \"我要把这堆东西一个个过一遍\"
            → 关注的是「遍历对象」本身

  while 循环 = \"只要这个条件成立，我就一直做\"
              → 关注的是「退出条件」

实用性结论:
  ✅ 能用 for 就用 for（更安全更清晰）
  ✅ 只有「不确定循环次数」时才用 while
'''
print(comparison)


# ============================================================
# 四、更多实战对比示例
# ============================================================

print('\n' + '=' * 50)
print('  实战对比示例')
print('=' * 50)

# 示例1：求 1~100 的和
print('\n【示例1】求 1~100 的和')

# for 版本（推荐）
total_for = sum(range(1, 101))
print(f'  for 版本: {total_for}')             # 5050

# while 版本
n = 1
total_while = 0
while n <= 100:
    total_while += n
    n += 1
print(f'  while 版本: {total_while}')         # 5050

# 示例2：猜数字游戏
print('\n【示例2】猜数字游戏（适合用 while）')
import random
secret = random.randint(1, 10)
attempts = 0

while True:                                   # 不确定几次能猜对 → 用 while
    guess = int(input('猜一个1-10的数字: '))
    attempts += 1
    
    if guess == secret:
        print(f'🎉 猜对了! 用了{attempts}次')
        break
    elif guess > secret:
        print('太大了，再试一次')
    else:
        print('太小了，再试一次')

print('\n✅ 练习完成!')