
from collections import Counter
c = Counter('abcdeabcdabcaba')
d = Counter('simsalabim')
print(d)

print(c)
c.update(d)     # make another counter
print(sorted(d))                   # add in the second counter

print(c)

print(c['a'])
print(''.join(sorted(c.elements())))

print(c.most_common(3) )