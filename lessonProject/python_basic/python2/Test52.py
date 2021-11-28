test = {"a":1, "b":2}
test_inv = {}

for j,k in test.items():
    #将k作为键，j作为值重新构建一个新字典
    test_inv[k] = j
print(test_inv)
