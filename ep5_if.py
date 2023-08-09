# 一个简单的示例，if语句的特点是根据if后的表达式返回的true或者false来判断该进行什么操作的
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# ==判断，用方法对变量进行处理不会改变存储在变量中的值，不等运算符是!=
car = 'Audi'
if car == 'audi':
    print('true')
else:
    print('false')
if car.lower() == 'audi':
    print('true')
else:
    print('false')

# and和or判断
age_0 = 22
age_1 = 24
if age_0 >= 21 and age_1 >= 25:
    print('ture')
else:
    print('false')
if age_0 >= 21 or age_1 >= 25:
    print('ture')
else:
    print('false')

# in（相反是not in），是否在列表中的判断
requested_topping = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_topping:
    print('true'.title())
else:
    print('false'.title())

# if语句（可不含else）
if age_0 >= 18:
    print('可以上网')

# if-else语句（略）

# if-elif-else语句，检查两个以上的条件，遇到满足条件的就跳过，格式：if-(elif)-...-(elif)-(else)
if age_0 < 4:
    print('门票25元')
elif age_0 < 18:
    print('门票50元')
else:
    print('门票100元')

# 用if-if-if的形式则不会跳过每个条件
# 对于数值0、空值、空列表等Python都会返回false
