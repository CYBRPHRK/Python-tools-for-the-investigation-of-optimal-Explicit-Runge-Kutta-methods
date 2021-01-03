class FileIO:
    def __init__(self, filename, accessMode):
        self.file = open(filename, accessMode)

    def changeAccessMode(self, accessMode):
        self.file.close()
        self.file = open(self.file.name, accessMode)
        
    def read(self):
        if not (self.file.readable()):
            self.changeAccessMode("r")
        return self.file.read()

    def readLine(self):
        if not (self.file.readable()):
            self.changeAccessMode("r")
        data = self.file.readline()
        return data

    def write(self, data, end='\n'):
        if not (self.file.writable()):
            self.changeAccessMode("a")
        data = data + end
        self.file.write(data)

    def __del__(self):
        self.file.close()

def test():
    data = "Opens a file for appending.\nThe file pointer is at the end of the file if the file exists." + "\nThat is, the file is in the append mode. If the file does not exist, it creates a new file for writing."

    f = FileIO("test1.txt", "w")
    f.write(data)
    f.write("\nMore text added", end='')

    f.write("\nMore text added to it")
    print (f.readLine(), end='')
    print (f.readLine(), end='')
    print (f.read(), end='')
    del f
