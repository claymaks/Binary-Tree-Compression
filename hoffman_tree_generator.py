from tree import huffman
from txtIO import fg, encode

reader = fg()
reader.read("sample_text.txt")
reader.gen_freq()
sorted_chars = sorted(reader.characters, key=lambda x: x[1], reverse=False)

print(sorted_chars)
h = huffman()
h.insert(sorted_chars)
print(h.find_char('j'), h.find_char('d'), h.find_char(' '))

e = encode()
e.open_file("sample_text.txt")
e.encode(h.find_char)


