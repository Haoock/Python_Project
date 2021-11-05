def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
    """修改列表中的元素"""
    names[0] = "Will"

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
print(usernames)
