import os

os.chdir('/Users/abby/Embroidery Fonts/test font/')

sizes=[1,2,3]
for x in sizes:
    if not "{} Inch".format(x) in os.listdir():
        os.mkdir("{} Inch".format(x))

for f in os.listdir():
    print(f)