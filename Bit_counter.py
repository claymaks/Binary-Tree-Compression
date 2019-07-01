#Bit counter

#bug where a number inside a string text document is counted as one bit instead of 8
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

def bitCounter_v2(fileName, t):
    
        file = open(fileName, "r")
        if t == "s":
            val = 8
        elif t == "b":
            val = 1

        bitcntr = 0

        for x in file:

            for i in x:

                bitcntr += val
                
        file.close()

        return bitcntr



        
