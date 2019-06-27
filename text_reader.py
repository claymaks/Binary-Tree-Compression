class fg(object):
    def __init__(self):
        self.characters = []

    def read(self, textfile):
        f = open(textfile, "r")
        self.reader = f

    def gen_freq(self):
        for word in self.reader:
            for c in word:
                if not any(c in sublist for sublist in self.characters):
                    self.characters.append([c, 1])
                else:
                    for n, sublist in enumerate(self.characters):
                        if c in sublist:
                            self.characters[n][1] += 1
        

class encode(object):
    def open_file(self, textfile):
        self.reader = open(textfile, "r")
        n,e = textfile.split(".")
        self.textfile = n + ".huffman." + e
        self.f = open(self.textfile, "w")
        self.f.close()
        
    def write(self, string):
        self.f = open(self.textfile, 'a')
        self.f.write(string)
        self.f.close()

    def encode(self, func):
        for word in self.reader:
            for c in word:
                self.write(func(c))
                

if __name__ == "__main__":
    reader = fg()
    reader.read("sample_text.txt")
    reader.gen_freq()
    print(reader.characters)
    reader.reader = "hello world"
    reader.characters = []
    reader.gen_freq()
    print(reader.characters)


    e = encode()
    e.open_file("sample_text.txt")
    e.write("hi")
    e.write("hello")
