# 第4章 操作列表
# 4.1遍历列表
# for循环 单复数有助于搞清楚是整个列表还是单个元素临时变量，for … in …:
magiccians = ['alice', 'david', 'carolina']
for magiccian in magiccians:
    print(magiccian)

# 4.1.2 未缩进的部分退出循环节
for magiccian in magiccians:
    print(f'{magiccian.title()}, that is a great trick!!!')
    print(f"I cant't wait to see your trick, {magiccian.title()}!\n")
print("Thank you, everyone. That was a great magic show!")

# range函数，可以生成一组连续的数，从第一个值开始到第二个值结束但不包括第二个值，这是Python的差一行为的结果；它还能指定步长，在后面再加一个参数
for value in range(1, 5):
    print(value)

# list函数将range（）的结果转换为列表
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for midnum in range(1, 11):
    square = midnum ** 2
    print(square)
    squares.append(square)
print(squares)

# 列表中的最大值最小值和求和函数：min、max、sum
nummin = min(squares)
nummax = max(squares)
numsum = sum(squares)
print(nummin)
print(nummax)
print(numsum)

# 列表推导式简化循环结构，格式：变量名 = [表达式 for语句]
squares_list = [value_list**2 for value_list in range(1, 11)]
print(squares_list)

# 4.4列表的部分
# 切片，引用部分列表，这个也遵循差一行为
print(squares[0:5])
print(squares[:5])# 可省略开头或结尾
print(squares[-2:])
# for循环也可切片遍历，在in后面用索引位置切就行

# 复制列表，格式：列表2 = 列表1[:]
abc = [1, 2, 3]
fgh = abc[:]
abc.append(4)
fgh.append(5)
print(abc)
print(fgh)

# 元组，不可修改，除非重新定义元组
list_o = [1, 3, 2]
print(list_o)
list_o = [1, 3, 5]
print(list_o)
yuan = (1, 2, 3)
print(yuan)
yuan = (1, 3, 2)
print(yuan)
print(yuan[-1])
