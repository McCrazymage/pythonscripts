import re
f = open(r'd:/test/a.txt')
o = open(r'd:/test/b.txt', 'w')

lines = f.readlines()
for line in lines:
    k=re.search(r'[a-zA-Z]([1-9]*)[a-zA-Z]([1-9]*)[a-zA-Z]([1-9]*)[a-zA-Z]([1-9]*)', line)
    o.write('%d %d %d %d\n' % (int(k.group(1)), int(k.group(2)), int(k.group(3)), int(k.group(4))))
o.close()