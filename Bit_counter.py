#Bit counter

class bitCounter(object):

    def bitCounter(fileName):

        file = open(fileName, "r")

        bitcntr = 0

        for x in file:

            for i in x:

                if isinstance(i, int):
                    
                    bitcntr += 1

                else:

                    bitcntr += 8
        file.close()

        return bitcntr



        
