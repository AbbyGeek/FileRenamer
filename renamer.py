import os
'''
TODO: 
 YoungForeverPES font does not have "bonus" label on all files.
 Wavie 3 inch number need space between Number and Char
 Errors: 1295
 Undefined Chars: 28
'''


# Change comp var to what computer I'm working on, or to appropriate folder
PC = "C:\\Users\Abby\Desktop\Patches\Stock\Fonts\PES\PES"
MAC = "/Users/abby/Embroidery Fonts/PES/PES"
comp = MAC
os.chdir(comp)

errorCount = 0
undefinedCount = 0
# For each folder in directory:
for fontName in next(os.walk('.'))[1]:
    #fontName=next(os.walk('.'))[1]
    os.chdir("{}/{}".format(comp, fontName))
    # Check if font folder has additional PES folder and move into it
    if os.path.isdir('PES'):
        os.chdir(comp+"/"+fontName+"/pes/")
        extraPES = True
    else:
        extraPES = False
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
                if extraPES:
                    destination = '{}/{}/PES/{} Inch/{}.pes'.format(comp, fontName, size, char.upper())

                else:
                    destination = '{}/{}/{} Inch/{}.pes'.format(comp, fontName, size, char.upper())
            #Lower
            elif charType == "lower":
                if extraPES:
                    destination = '{}/{}/PES/{} Inch/{}.pes'.format(comp,fontName, size, char.lower())
                else:
                    destination = '{}/{}/{} Inch/{}.pes'.format(comp,fontName, size, char.lower())
            #Number
            elif charType == "number":
                if extraPES:
                    destination = '{}/{}/PES/{} Inch/{}.pes'.format(comp, fontName, size, char)
                else:
                    destination = '{}/{}/{} Inch/{}.pes'.format(comp, fontName, size, char)
            #Bonus (refactor this mess)
            elif charType == "bonus":
                if char == "exclamation": char = "!"
                elif char == "dash": char = "-"
                elif char == "at": char = "@"
                elif char == "ampersand" or char == "and": char = "&"
                elif char == "period" or char == "dot": char = "."
                elif char == "dollar" or char == "money": char = "$"
                elif char == "number": char = "#"
                elif char == "percent": char = "%"
                elif char == "question" or char == "questions": char = "question" #Unable to name a file "?"
                else: 
                    print("{} is not defined for {}".format(f, fontName))
                    undefinedCount+=1
                if extraPES:
                    destination = '{}/{}/PES/{} Inch/{}.pes'.format(comp, fontName, size, char)
                else:
                    destination = '{}/{}/{} Inch/{}.pes'.format(comp, fontName, size, char)
            else: 
                print("Error w/ file {} in {}".format(f, fontName))
                errorCount+=1
            if extraPES:
                oldFile = '{}/{}/PES/{}'.format(comp, fontName, f)
            else:
                oldFile = '{}/{}/{}'.format(comp, fontName, f)
            os.rename(oldFile, destination)
    print(fontName + " finished")
print("Errors: {}".format(errorCount))
print("Undefined Chars: {}".format(undefinedCount))