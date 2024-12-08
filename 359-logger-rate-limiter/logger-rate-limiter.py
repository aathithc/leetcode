class Logger:

    def __init__(self):
        self.messagemap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messagemap:
            self.messagemap[message] = timestamp
            return True
        if timestamp - self.messagemap[message] >= 10:
            self.messagemap[message] = timestamp
            return True
        else:
            return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)