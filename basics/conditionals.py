# -*- coding: utf-8 -*-
\"\"\"条件语句练习\"\"\"

# ========== 简单条件 ==========
age = 18

if age >= 18:
    print('已成年，可以考驾照')
else:
    print('未成年，需要等待')

# ========== 多条件 ==========
score = 85

if score >= 90:
    grade = 'A'
    print('优秀')
elif score >= 80:
    grade = 'B'
    print('良好')
elif score >= 60:
    grade = 'C'
    print('及格')
else:
    grade = 'D'
    print('不及格')

print(f'成绩: {score}, 等级: {grade}')

# ========== 嵌套条件 ==========
is_student = True
has_ticket = True

if is_student:
    if has_ticket:
        print('学生票入场')
    else:
        print('需要购票')
else:
    if has_ticket:
        print('普通票入场')
    else:
        print('需要购票')

# ========== 多条件组合 ==========
age = 25
has_job = True

if age >= 18 and has_job:
    print('符合申请条件')

if age < 18 or not has_job:
    print('不符合条件')

# ========== 三目运算符 ==========
age = 20
status = '成年人' if age >= 18 else '未成年人'
print(f'状态: {status}')