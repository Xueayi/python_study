message = 'hello world! '
print(message)

#f字符串   f、双引号、花括号括变量、逗号
print(f"Hello,{message}")

#标题型方法
print(message.title())


print(message.lower())
#全部小写

print(message.upper())
#全部大写


print("\thello\nworld")
#反斜杠添加空白

print(message)

print(message.rstrip())
#delete right block同样的还有lstrip and strip

print(message.removeprefix('hello '))
print('Albert Einstein once said,"A person who never made a mistake never tried anything new."')
filename='python_notes.py'
print(filename.removesuffix('.py'))
