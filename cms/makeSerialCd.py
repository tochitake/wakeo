import random
import string


class MakeRndCode:
    def __init__(self, rndlist=[]):
        self._rndlist = list(set(rndlist))

    def mkrnd(self, strlen=40):
        src_str = string.ascii_letters + string.digits
        rnd_str = "".join([random.choice(src_str) for x in range(strlen)])
        # unique?
        if rnd_str in self._rndlist:
            rnd_str = self.mkrnd(strlen)
        self._rndlist.append(rnd_str)
        return rnd_str

    def addlist(self, rndlist):
        rndlist = list(set(rndlist))
        self._rndlist += rndlist

    def tolist(self):
        print(self._rndlist)

if __name__ == '__main__':
    mkrndcd = MakeRndCode()
    rnd = mkrndcd.mkrnd(10)
    print(rnd)

    rndl = [mkrndcd.mkrnd(10) for x in range(5)]
    print(rndl)