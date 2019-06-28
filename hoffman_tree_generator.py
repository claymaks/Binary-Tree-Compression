from tree import huffman
from txtIO import fg, encode
from listIO import 

#Read in sample text, output a frequency as sorted_chars
reader = fg()
reader.read("sample_text.txt")
reader.gen_freq()
sorted_chars = sorted(reader.characters, key=lambda x: x[1], reverse=False)

#Create Huffman tree, initialize with sorted_chars
e = huffman()
e.insert(sorted_chars)

#encode sample text as Huffman encoded binary
e = encode()
e.open_file("sample_text.txt")
e.encode(h.find_char)

#exports sorted_chars as list to text document
'"sample_text.tree.txt"'



#import sample_text.tree.txt as list



#load list into tree
d = huffman()
d.insert(sorted_chars)

#load sample_text.huffman.txt
reader = fg()
reader.read("sample_text.huffman.txt")

#decodes sample_text.huffman.txt
string = ""
for word in reader.reader:
    string += word
new_string = ""
wile string:
    char, string = d.translate(string)
    new_string += char

#exports as sample_text.export.txt
file = open("sample_text.export.txt", "w")
file.write(new_string)
