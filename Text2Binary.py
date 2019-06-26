#Text to Binary

import math

def write_txt(name, string):

    name = 'Bin_' + name
    new_file = open(name, 'w+')

    for char in string:

        new_file.write(char)

    new_file.close()

    return

def getBin(num):

    binlist = ['0','0','0','0','0','0','0','0']
    
    while num != 0:

        base = int(math.log(num, 2))

        num = num - (2 ** base)

        binlist[base] = '1'
        binlist.reverse()

    return binlist

    
def getText():

    file_name = input('Enter the name(with extension) of the file you want to convert: ')
    txtFile = open(file_name, 'r')

    full_bin = ''
    
    for x in txtFile:

        for i in x:

            binlist = getBin(ord(i))
            binstr = ''.join(binlist)

            full_bin = full_bin + binstr
            
    write_txt(file_name, full_bin)

    txtFile.close()
    
    return

getText()
