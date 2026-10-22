# 1-m
x = 13
print(type(x))
print(x.bit_length())


# 2-m
s = "hello"
print(type(s))
print(s.upper())
print(s.replace("e", "3"))


# 3-m
def add(a, b):
    return a + b

print(type(add))
add.label = "sum"
print(add.label)


# 4-m
class User:
    pass

u = User()
print(u)
print(type(u))


# 5-m
class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age

u = User("alim", 25)
print(u.username, u.age)

