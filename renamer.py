import os

os.chdir('/Users/abby/Embroidery Fonts/test font/')

for f in os.listdir():
    fList = f.split()
    if(fList[-1]) == "Inch.pes":
        size = fList[-2]
        char = fList[-3].lower()
        charType = fList[-4].lower()
        if not os.path.isdir("{} Inch".format(size)):
            os.mkdir("{} Inch".format(size))
        #Upper
        if charType == "upper":
            destination = '/Users/abby/Embroidery Fonts/test font/{} Inch/{}.pes'.format(size, char.upper())
        #Lower
        elif charType == "lower":
            destination = '/Users/abby/Embroidery Fonts/test font/{} Inch/{}.pes'.format(size, char.lower())
        #Number
        elif charType == "number":
            destination = '/Users/abby/Embroidery Fonts/test font/{} Inch/{}.pes'.format(size, char())
        #Bonus
        elif charType == "bonus":
            if char == "exclamation": char = "!"
            if char == "dash": char = "-"
            if char == "at": char = "@"
            if char == "ampersand": char = "&"
            if char == "period" or char == "dot": char = "."
            if char == "dollar": char = "$"
            if char == "question": char = "?"
            # print(char)
            destination = '/Users/abby/Embroidery Fonts/test font/{} Inch/{}.pes'.format(size, char)
        else: print(f)
        oldFile = '/Users/abby/Embroidery Fonts/test font/{}'.format(f)
        os.rename(oldFile, destination)

        ##Something isn't working. Only a few files are being sorted. The majority get lost somewhere