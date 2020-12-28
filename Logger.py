import FileIO
import os
import datetime as dt

class Logger:
    def __init__(self, msg):
        if (os.path.isfile("Debug/log.txt")):
            os.remove("Debug/log.txt")
        self.file = FileIO.FileIO("Debug/log.txt", "a")
        self.file.write(msg + "\n" + self.datetime() + "\n")

    def datetime(self):
        return str(dt.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p"))

    def info(self, msg, arg0=None, arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None,
             arg7=None, arg8=None, arg9=None, arg10=None, arg11=None, arg12=None, arg13=None, arg14=None, arg15=None):
        args = [arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15]
        
        for arg in args:
            if (arg != None):
                msg = msg + " " + str(arg)
        self.file.writeLine(self.datetime() + " Info: " + msg)

    def warning(self, msg, arg0=None, arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None,
             arg7=None, arg8=None, arg9=None, arg10=None, arg11=None, arg12=None, arg13=None, arg14=None, arg15=None):
        args = [arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15]
        
        for arg in args:
            if (arg != None):
                msg = msg + " " + str(arg)
        self.file.writeLine(self.datetime() + " Warning: " + msg)

    def error(self, msg, arg0=None, arg1=None, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None,
             arg7=None, arg8=None, arg9=None, arg10=None, arg11=None, arg12=None, arg13=None, arg14=None, arg15=None):
        args = [arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15]
        
        for arg in args:
            if (arg != None):
                msg = msg + " " + str(arg)
        self.file.writeLine(self.datetime() + " Error: " + msg)

    def __del__(self):
        del self.file

def test():
    log = Logger("Numerical Analysis Research Thesis Log")

    log.info("Numerical Analysis Logs")
    log.info("Logger Check", 123, "and", 456)

    log.warning("Test Warning")
    log.warning("Test Warning", 123, "and", 456)

    log.warning("Test Error")
    log.warning("Test Error", 123, "and", 456)
    del log
