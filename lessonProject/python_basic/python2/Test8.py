n = 123456
# %09d 表示最小宽度为9，左边补0
print("n(09):%09d" % n)





# %+9d 表示最小宽度为9，带上符号
print("n(+9):%+9d" %n)

f = 140.5
# %-+010f 表示最小宽度为10，左对齐，带上符号
print("f(-+0):%-+10f" % f)
# +140.500000


s = "Hello"
# %-10s 表示最小宽度为10，左对齐
print("s(-10):%-10s." % s)

