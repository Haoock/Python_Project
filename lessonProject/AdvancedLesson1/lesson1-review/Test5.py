import random
s = set([])

for i in range(int(input('N:'))):
    s.add(random.randint(1,5))

print(s)
print(sorted(s))
