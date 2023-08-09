# input()函数
# message = input('Tell me something, and I will repeat it back to you: ')
# print(message)

# +=运算符在赋给变量的字符串末尾追加一个字符串
# prompt = "我们想知道你的信息"
# prompt += "\n请先告诉我们你的姓氏："
# name = input(prompt)    # 不要忘记把用户输入的值赋值给一个变量
# print(f"好的，你的姓氏是{name}")

# int()来把字符串转换成数值
# age = input("How old are you?")
# age = int(age)
# if age >= 18:
#     print('True')
# else:
#     print('False')

# %取余数运算符
# print(8 % 3)
#
# # while循环
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# 设定退出值，如“quit”
prompt = "\n我们想知道你的信息，请告诉我们一些什么"
prompt += "\n输入quit以退出程序"
#
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# 使用变量标志（flag）来控制整个程序的活动状态
# flag = True
# while flag:
#     message = input(prompt)
#     if message == 'quit':
#         flag = False
#     else:
#         print(message)

# 使用break退出循环
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\nEnter 'quit' when you are finshed."
#
# while 1:
#     message = input(prompt)
#     if message == 'quit':
#         break
#     else:
#         print(message)

# 使用continue返回循环开头
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# 避免无限循环
# x = 1
# while x < 5:
#     print(x)

# 使用while循环处理列表和字典，在遍历时进行修改等处理
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 删除为特定值的列表中所有元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:    # 是否可以把in理解为将后方的列表值依次递送给in前面的内容，如果前面是变量则存入，如果前面是字符串则进行比较返回t或f
    pets.remove('cat')

print(pets)

# 验证猜想
if 'dog' in pets:
    print('True')
else:
    print("False")

# 使用用户输入填充字典
responses = {}
flag = True

while flag:
    name = input("What's your name?\n")
    response = input("Which mountain would you like to climb someday?\n")
    responses[name] = response

    repeat = input("Would you like to let another person respond?(yse/no)\n")
    if repeat == 'no':
        flag = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")