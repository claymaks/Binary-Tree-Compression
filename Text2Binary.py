#Text to Binary

import math

def getBin(num):

    binlist = ['0','0','0','0','0','0','0','0']
    
    while num != 0:

        base = int(math.log(num, 2))

        num = num - (2 ** base)

        binlist[base] = '1'
        binlist.reverse()

    return binlist

    
def getText():

    txtFile = open('Sample.txt', 'r')

    for x in txtFile:

        for i in x:

            binlist = getBin(ord(i))
            binstr = ''.join(binlist)
            
            print(binstr)

    txtFile.close()
    
    return

getText()
