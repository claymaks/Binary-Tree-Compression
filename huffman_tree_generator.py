from tree import huffman
from txtIO import fg, encode
from listIO import listIO
from Bit_counter import bitCounter_v2
from sys import platform
import time
import os


FILE = input("File: ")

start = time.time()
if ".txt" in FILE:
    pass
else:
    print("Not a txt")
    quit()

if platform == "linux" or platform == "linux2":
    fn = FILE.split("/")[-1].split(".")[0]
elif platform == "darwin":
    fn = FILE.split("/")[-1].split(".")[0]
elif platform == "win32":
    fn = FILE.split("\\")[-1].split(".")[0]
PATH = FILE[:-(len(fn)+4)]
LOG_F = PATH + "log.txt"
LOG = open(LOG_F, "w")
LOG.write(fn)
LOG.close()

LOG = open(LOG_F, "a")

print("File size:", os.path.getsize(FILE), file=LOG)
ENCODE_TIME_CONST = 9738.61561
t = ((1.15**(1.25*(os.path.getsize(FILE)/ENCODE_TIME_CONST))) - 1) + os.path.getsize(FILE)/ENCODE_TIME_CONST
print("Estimated time greater than:", t, "seconds.")
print("Simulated on 2.3 GHz Intel Core i5")

print("Estimated time greater than:", t, "seconds.", file=LOG)
print("Simulated on 2.3 GHz Intel Core i5", file=LOG)


#print("Read in sample text, output a frequency as sorted_chars")
reader = fg()
reader.read(FILE)
reader.gen_freq()
sorted_chars = sorted(reader.characters, key=lambda x: x[1], reverse=False)
#print(time.time()-start)

#print("Create Huffman tree, initialize with sorted_chars")
he = huffman()
he.insert(sorted_chars)
#print(time.time()-start)

#print("encode sample text as Huffman encoded binary")
e = encode()
e.open_file(FILE)
e.encode(he.find_char)
#print(time.time()-start)

#print("strip sorted_chars of 3rd item (binary path)")
stripped_chars = []
for i in sorted_chars:
    stripped_chars.append([i[0],i[1]])
#print(time.time()-start)

#print("exports sorted_chars as list to text document")
theFile = PATH + fn +'.tree.txt'


listIO.exportList(theFile,stripped_chars)
#print(time.time()-start)

#print("import sample_text.tree.txt as list")
impList = listIO.importList(theFile)
#print(time.time()-start)

#print("load list into tree")
hd = huffman()
hd.insert(impList)
#print(time.time()-start)

#print("load sample_text.huffman.txt")
reader = fg()
readFile = PATH + fn + ".huffman.txt"
reader.read(readFile)
#print(time.time()-start)

#print("decodes sample_text.huffman.txt")
string = ""
for word in reader.reader:
    string += word
new_string = ""
bit_size = len(string)
#print("Reading", bit_size, "bits")
lock = False
while string:
    char, string = hd.translate(string)
    new_string += char
    
#print(time.time()-start)

#print("exports as sample_text.export.txt")
fileEx = PATH + fn + ".export.txt"
file = open(fileEx, "w+")
file.write(new_string)
file.close()
end = time.time()
s = input("Files complete. Press \"s\" for stats >>> ")

if s == "s":
    #ANALYZE FILES
    print("Time to run:", end-start, file=LOG)
    uncomp = bitCounter_v2(FILE, "s")
    print("Initial bits in file:", uncomp, file=LOG)
    comp = bitCounter_v2(readFile, "b")
    print("Final bits in file:", comp, file=LOG)

    #uncompressed / compressed
    print("Compression ratio:", uncomp/comp, file=LOG)

    hts = bitCounter_v2(theFile, "s")
    print("Huffman tree size:", hts, "bits", file=LOG)

    #final bits + huffman tree bits
    print("Total size:", comp + hts, file=LOG)
    
    #100 * (compressed + huffman tree) / uncompressed
    print("Transfer cutdown to:", int(100 * (comp + hts) / uncomp)+1, "%", file=LOG)
    LOG.close()
else:
    LOG.close()
    quit()





    
