# 字典用放在花括号{}中的键值对表示
# 不同颜色的外星人分数不同
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])

# 格式：字典名 = {键:值 ,键:值 ,...}，创建空字典的方式和创建空列表的方式相似
# 访问字典中的值格式：字典名[键]
new_points = alien_0['points']
print(f'You just earned {new_points} points!')

# 添加键值对，字典是动态结构，添加的格式：字典名[键] = 值
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 修改字典中的值，类似于新增键值对的赋值格式，可以理解为覆盖键值对
alien_0['color'] = 'yellow'
print(alien_0)

alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

print(f"Original position:{alien_0['x_position']}")
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position:{alien_0['x_position']}")

alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
print(f"Original position:{alien_0['x_position']}")
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position:{alien_0['x_position']}")

# del，删除键值对，del是语句不是方法，它放在开头
del alien_0['points']
print(alien_0)

# 由类似的对象创建多行字典
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
print(favorite_language)

# get()方法，访问值。get(指定键(,指定键不存在时的返回值))。
# 如果键有可能不存在，应该用get（）方法而不是方括号
point_value = alien_0.get('point', 'No point value assigned.')
print(point_value)

# 遍历所有的键值对
# items()方法，返回一个键值对列表
user_0 = {
    'usersname': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for k, v in user_0.items():
    print(f'\nKey:{k.title()}')
    print(f'Value:{v.title()}')

# 遍历所有键
# keys()方法，返回字典中的键
for name in favorite_language.keys():
    print(name.title())

# sorted()函数排序
for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# 遍历所有值
# values()方法，返回字典的值列表
for language in favorite_language.values():
    print(language)

# set()函数，剔除集合中重复的元素。集合中不允许出现重复的元素，可用花括号创建集合，不同于字典，没有键值对时则可能是集合
print('\n')
for language in set(favorite_language.values()):
    print(language.title())

# 嵌套，创建多个字典，把字典名放进列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print('\n')

# 更多的外星人及其修改
aliens = []
for alien_number in range(30):  # 执行循环的次数
    new_alien = {'color': 'blue', 'points': 20, 'speed': 'fast'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    print(alien)
print('...')
print(f'Total number of alien: {len(aliens)}')
print('\n\n')
for alien in aliens[:3]:
    if alien['color'] == 'blue':
        alien['color'] = 'black'
        alien['speed'] = 'very fast'
        alien['points'] = '25'
for alien in aliens[0:5]:
    print(alien)
print('...')

# 在字典中存储列表，值可由列表组成
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
for topping in pizza['toppings']:   #直接在字典的值里遍历，如果再遍历字典时如使用tiems时遇到列表再字典中，需要再写个for循环
    print(topping)

print('\n')
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phip': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    for language in languages:
        print(f"{language.title()} is {name.title()}'s favorite languages")

# 在字典里嵌套字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, userinfo in users.items():
    print('\n')
    print(f"Username: {username}")
    print(f"\tFull name: {userinfo['first'].title()} {userinfo['last'].title()}")
    print(f"\tLocation: {userinfo['location'].title()}")

