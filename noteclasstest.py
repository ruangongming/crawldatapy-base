def chan():
    return 2
class dichuyen:
    def __init__(self, chan):
        self.chan = chan
    def dctrai(self):
        print("{} sang trai" .format(self.chan))
    def dcphai(self):
        print("{}sang phải".format(self.chan))

chan = chan()

dc = dichuyen(chan)

print(dc.dcphai())