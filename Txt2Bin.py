#Text to binary class

import math

class Text2Binary(object):

    def getBin(self, char):
        
        self.fullBin = ''
    
        binList = ['0','0','0','0','0','0','0','0']

        while char != 0:

            base = int(math.log(char, 2))

            char = char - (2 ** base)

            binList[base] = '1'
            (binList).reverse()
            
        binString = ''.join(binList)

        self.fullBin = self.fullBin + binString

        return self.fullBin

    def writeText(self, binNum):

        newName = 'Bin_' + self.fileName
        newFile = open(newName, 'a+')

        newFile.write(binNum)

        newFile.close()
    
    def __init__(self, fileName):

        self.fileName = fileName
        self.txtFile = open(fileName, 'r')

        for x in self.txtFile:

            for i in x:

                fullString = self.getBin(ord(i))


        self.writeText(self.fullBin)

        (self.txtFile).close()
        
        return

        
