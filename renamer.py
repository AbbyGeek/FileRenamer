import os

# Change comp var to what computer I'm working on, or to appropriate folder
PC = "C:\\Users\Abby\Desktop\Patches\Stock\Fonts\PES\PES\\test font"
MAC = "/Users/abby/Embroidery Fonts/test font"
comp = PC
os.chdir(PC)

# Check if font folder has additional PES folder and move into it
if os.path.isdir('PES'):
    os.chdir(comp+"/pes")

# Splits and extrapolates variables for sorting
for f in os.listdir():
    fList = f.split()
    if(fList[-1]) == "Inch.pes":
        size = fList[-2]
        char = fList[-3].lower()
        charType = fList[-4].lower()
        # Creates folder for specific size if not created
        if not os.path.isdir("{} Inch".format(size)):
            os.mkdir("{} Inch".format(size))
        #Upper
        if charType == "upper":
            destination = '{}/{} Inch/{}.pes'.format(comp, size, char.upper())
        #Lower
        elif charType == "lower":
            destination = '{}/{} Inch/{}.pes'.format(comp, size, char.lower())
        #Number
        elif charType == "number":
            destination = '{}/{} Inch/{}.pes'.format(comp, size, char)
        #Bonus
        elif charType == "bonus":
            if char == "exclamation": char = "!"
            elif char == "dash": char = "-"
            elif char == "at": char = "@"
            elif char == "ampersand": char = "&"
            elif char == "period" or char == "dot": char = "."
            elif char == "dollar": char = "$"
            elif char == "number": char = "#"
            elif char == "question": char = "question" #Unable to name a file "?"
            else: 
                print("{} is not defined".format(f))
                break
            destination = '{}/{} Inch/{}.pes'.format(comp, size, char)
        else: print("Error w/ file {}".format(f))
        oldFile = '{}/{}'.format(comp, f)
        # Move and rename file
        os.rename(oldFile, destination)