import os

class FileIO:
    def __init__(self, filename, accessMode):
        if accessMode in ['r', 'rb', 'r+', 'rb+', 'w', 'w+', 'wb', 'wb+', 'a', 'a+', 'ab', 'ab+']:
            if ((accessMode in ['r', 'rb', 'r+', 'rb+']) and not (os.path.exists(filename))):
                print ("The given path is not a file, directory or a valid symlink.")
            else:
                self.file = open(filename, accessMode)
        else:
            print ("Invalid access mode.")

    def changeAccessMode(self, accessMode):
        if (self.isCreated()):
            self.file.close()
            self.file = open(self.file.name, accessMode)
        else:
            print ("The object is not initialized. Check the file path or the accessMode.")
        
    def read(self):
        if (self.isCreated()):
            if not (self.file.readable()):
                self.changeAccessMode("r")
            return self.file.read()
        else:
            print ("The object is not initialized. Check the file path or the accessMode.")
            return "Nothing to read"

    def readLine(self):
        if (self.isCreated()):
            if not (self.file.readable()):
                self.changeAccessMode("r")
            data = self.file.readline()
            return data
        else:
            print ("The object is not initialized. Check the file path or the accessMode.")
            return "Nothing to read"

    def write(self, data, end='\n'):
        if (self.isCreated()):
            if not (self.file.writable()):
                self.changeAccessMode("a")
            data = data + end
            self.file.write(data)
        else:
            print ("The object is not initialized. Check the file path or the accessMode.")

    def name(self):
        return self.file.name

    def mode(self):
        return self.file.mode

    def isCreated(self):
        return hasattr(self, 'file')

    def __del__(self):
        if (self.isCreated()):
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
