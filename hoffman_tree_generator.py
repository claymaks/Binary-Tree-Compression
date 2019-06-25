from tree import tree
from frequency_generator import fg

reader = fg()
reader.read("sample_text.txt")
reader.gen_freq()
sorted_chars = sorted(reader.characters, key=lambda x: x[1], reverse=False)

print(sorted_chars)
