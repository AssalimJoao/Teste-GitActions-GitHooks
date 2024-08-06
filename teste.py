def foo(x, y):
    if x > 0:
        return x + y
    elif x == 0:
        return y
    else:
        return x - y


def bar():
    print("Hello, world!")


print(foo(3, 4))
bar()
