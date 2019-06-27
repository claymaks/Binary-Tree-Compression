#Import/export list file

class listIO(object):

    def importList(fileName):

        readFile = open(fileName,'r')

        fileString = ''

        fullList = []

        for i in readFile:

            fileString = ''
            
            for x in i:

                if x != '\n':
                    
                    fileString = fileString + x

            fullList.append(list(fileString))

        readFile.close()

        return fullList

    def exportList(fileName, theList):

        theString = ''

        for i in theList:

            for k in i:

                theString = theString + str(k)

            theString = theString + '\n'

        newFile = open(fileName,'w+')

        for i in theString:

            newFile.write(i)

        newFile.close()
    
        return

        
