f= open(r'c:/a.txt','r')
o= open(r'c:/test/b.txt','w')
lines = f.readlines()
for line in lines:
    items = line.split()
    a = 12.0000*float(items[0])+1.0078*float(items[1])+18.9984*float(items[2])+15.9949*float(items[3])
    o.write('%f\n' % a)
    
f.close()
o.close()