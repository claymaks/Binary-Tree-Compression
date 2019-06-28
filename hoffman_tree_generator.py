from tree import huffman
from txtIO import fg, encode
from listIO import listIO

#Read in sample text, output a frequency as sorted_chars
reader = fg()
reader.read("sample_text.txt")
reader.gen_freq()
sorted_chars = sorted(reader.characters, key=lambda x: x[1], reverse=False)

#Create Huffman tree, initialize with sorted_chars
he = huffman()
he.insert(sorted_chars)
#encode sample text as Huffman encoded binary
e = encode()
e.open_file("sample_text.txt")
e.encode(he.find_char)

#exports sorted_chars as list to text document
'"sample_text.tree.txt"'


#import sample_text.tree.txt as list



#load list into tree
hd = huffman()
hd.insert(sorted_chars)

#load sample_text.huffman.txt
reader = fg()
reader.read("sample_text.huffman.txt")

#decodes sample_text.huffman.txt
string = ""
for word in reader.reader:
    string += word
new_string = ""
while string:
    char, string = hd.translate(string)
    new_string += char

#exports as sample_text.export.txt
file = open("sample_text.export.txt", "w+")
file.write(new_string)
file.close()
s = input("Files complete. Press \"s\" for stats >>> ")

if s == "s":
    #ANALYZE FILES


    print("Initial bits in file:", )

    print("Final bits in file:", )

    #uncompressed / compressed
    print("Compression ratio:", )

    print("Huffman tree size:", )

    #final bits + huffman tree bits
    print("Total size:", )
    
    #100 * (compressed + huffman tree) / uncompressed
    print("Space saved:", )





    
