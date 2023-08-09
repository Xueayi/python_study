# 定义函数，username是形参，'jesse' 是实参
def greet_user(username):
    """显示简单的问候语"""  # 文档字符串注释，能包含多行
    print(f"Hello!, {username.title()}")


greet_user('jesse')


# 位置实参，以顺序关联
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print(f"\nI hava a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet("cat", "neko")


# 关键字实参，以   关键字=‘字符串’   对应
describe_pet(pet_name='harry', animal_type='hamster')


# 默认值，在定义函数时给形参赋值
def describe_animal(animal_name, animal_type='dog'):    # 有默认值的参数放后面
    """显示宠物信息"""
    print(f"\nI hava a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name.title()}")


describe_animal('umi')


# return语句，返回值
def get_formatted_name(first_name, last_name):
    """返回标准格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 让实参变成可选的——给实参设定一个空字符的默认值
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
        return full_name.title()
    else:
        full_name = f"{first_name} {last_name}"
        return full_name.title()


musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 返回字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first_name': first_name, 'last_name': last_name}
    return person


musician = build_person('timi', 'lee')
print(musician)


# 传递列表
def greet_users(users):
    """向列表中的每个用户发出简单的问候"""
    for user in users:
        print(f"Hello! deer {user.title()}")


username_all = ['john', 'mary', 'jack']
greet_users(username_all)


# function_name(list_name[:])这个式子表示创建列表的副本，并交给函数
# *形参名，一个星号创建元组，这样的表示方式能允许传递任意数量的实参，收到的信息自动放进元组
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


make_pizza('cat', 'dog', 'salt', 'spoon')


# **形参名，两个星号创建字典，使用任意数量的关键字实参，收到的关键字实参自动放进字典的键值对
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
# 再给形参指定默认值时，等号两边不要有空格


# 将函数存储在模块中，见同文件夹文件pizza和making_pizza
"""
导入格式：
import [module_name] # 导入全部函数，这种方法需要使用module_name.function_name()的格式来使用
或 from [module_name] import [function_name, function_1, ...] # 不需要使用点号
或 from [module_name] import * #导入全部函数，不需要使用点号
"""


# 使用as给函数指定别名（alias）
from pizza import make_pizza as mp
mp(16, 'ice-cream')
