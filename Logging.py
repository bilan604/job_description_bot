class Logger(object):

    def __init__(self):
        self.contents = []

    def log(self, s):
        self.contents += s

    def display(self, sep=False):
        if sep:
            separator = "--------------------"
            for i in range(len(self.contents)):
                print(f"{i}: {self.contents}\n")
                print(separator)
        else:
            for i in range(len(self.contents)):
                print(f"{i}: {self.contents}\n")
