# 列表，方括号
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])  # 索引从0开始
print(bicycles[0].title())  # 方法再变量后

# 访问最后一个元素可以用-1，以此类推
print(bicycles[-1])

# f字符串，在引号前加上f，在引号内使用花括号引用变量
messaage = f'My first bicycles was a {bicycles[0].title()}.'
print(messaage)

# 修改元素和添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 重新赋值
motorcycles[0] = 'ducati'
print(motorcycles)

# append追加
motorcycles.append(bicycles)
print(motorcycles)

list_append = []
list_append.append('1')
list_append.append('3')
list_append.append('2')
print(list_append)
print(list_append[2])

# insert在某处插入，需要递送两个值，输入的位置数值是索引位置，或者理解为在原来的列表该索引位置左侧插入
motorcycles.insert(0, 'obs')
print(motorcycles)

# del删除，只需输入索引位置，del是语句而不是方法，它在变量名的前面
del motorcycles[-1]
print(motorcycles)

# pop方法删除最后一个元素，并使用它的值
motor = motorcycles.pop()
print(motorcycles)
print(motor)

# pop递送一个值时可以删除任意位置的列表元素
motor_2 = motorcycles.pop(1)
print(motorcycles)
print(motor_2)

# remove方法根据值删除元素，只删除第一个出现的该值
motorcycles.remove('obs')
print(motorcycles)

# sort列表排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# cars.sort()
# print(cars)

# sort按相反的顺序排序，传递参数reverse=True
# cars.sort(reverse=True)
# print(cars)

# sorted函数临时排序，给它递送一个列表，它的返回值就是临时排序
print(sorted(cars))
print(sorted(cars, reverse=True))

# reverse反转列表/反向打印列表
cars.reverse()
print(cars)

# len函数确定列表的长度
print(len(cars))