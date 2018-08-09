def func():
    list = range(5)
    for i in list:
        yield i

result = func()

print(result)

for i in result:
    print(i)