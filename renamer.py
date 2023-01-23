import os

os.chdir('/Users/abby/Embroidery Fonts/test font/')

sizes=[1,2,3]
for x in sizes:
    if not "{} Inch".format(x) in os.listdir():
        os.mkdir("{} Inch".format(x))

for f in os.listdir():
    if f[-8:] == "Inch.pes":
        size = f[-10]
        oldFile = '/Users/abby/Embroidery Fonts/test font/{}'.format(f)
        destination = '/Users/abby/Embroidery Fonts/test font/{} Inch/{}'.format(size, f)
        os.rename(oldFile, destination)
