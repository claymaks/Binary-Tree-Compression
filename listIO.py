#Import/export list file

class listIO(object):

    def importList(fileName):

        readFile = open(fileName,'r')

        fileString = ''

        fullList = []

        for i in readFile:

            fileString = ''
            
            for x in i:

                if x != '\n' or not fileString:
                    if x == "\n":
                        fileString = fileString + "\\n"
                    else:
                        fileString = fileString + x
            if fileString[0] == "\\":
                fullList.append([fileString[0:2], int(fileString[2:])])
            else:
                fullList.append([fileString[0], int(fileString[1:])])

        readFile.close()

        return fullList

    def exportList(fileName, theList):

        theString = ''

        for i in theList:

            for k in i:
                if k == "\n":
                    theString = theString + "\\n"
                else:
                    theString = theString + str(k)
        
            theString = theString + '\n'

        newFile = open(fileName,'w+')

        for i in theString:

            newFile.write(i)

        newFile.close()
    
        return

        
