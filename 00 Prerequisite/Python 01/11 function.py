def say_hello(first_name, last_name):
    print('hello', first_name)
    print('goodbye', last_name)


i = 10
j = 20
say_hello('Jack', 'Reacher')

print('last line')


def get_age(name, family='Reacher'):
    if name == 'Jack':
        return 31
    elif name == 'Alton':
        return 28
    else:
        return -1


age = get_age('Jack')
print(age)