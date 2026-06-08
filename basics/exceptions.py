# -*- coding: utf-8 -*-
\"\"\"异常处理练习\"\"\"

# ========== 基本异常捕获 ==========
def safe_divide(a, b):
    try:
        result = a / b
        print(f'{a} / {b} = {result}')
    except ZeroDivisionError:
        print('错误: 除数不能为零!')
    except TypeError:
        print('错误: 类型错误!')
    except Exception as e:
        print(f'未知错误: {e}')

safe_divide(10, 2)
safe_divide(10, 0)
safe_divide('10', 2)

# ========== 带 else 和 finally ==========
def get_element(lst, index):
    try:
        element = lst[index]
    except IndexError:
        print(f'错误: 索引 {index} 超出范围 (列表长度: {len(lst)})')
    else:
        print(f'成功获取元素: {element}')
    finally:
        print('--- 本次操作完成 ---\n')

get_element([1, 2, 3], 1)
get_element([1, 2, 3], 10)

# ========== 主动抛出异常 ==========
def validate_age(age):
    if age < 0:
        raise ValueError('年龄不能为负数!')
    if age > 150:
        raise ValueError('年龄不合理!')
    return age

try:
    print(f'年龄验证: {validate_age(25)}')
    print(f'年龄验证: {validate_age(-5)}')
except ValueError as e:
    print(f'验证失败: {e}')