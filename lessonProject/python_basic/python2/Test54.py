import random
s = set([])

for i in range(int(input('N:'))):
    s.add(random.randint(1,20))

print(s)
print(sorted(s))
