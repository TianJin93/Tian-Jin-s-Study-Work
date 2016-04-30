class Hashtable:
    def __init__(self, dict):
        input_len = len(dict)
        self.m = (input_len) * 2 if input_len > 0 else 11
        self.n = input_len
        self.data = [None for _ in range(0, self.m)]
        for k, v in dict.items():
            h_k = self.hash(k)
            if self.data[h_k] is None:
                self.data[h_k] = []
            self.data[h_k].append((k, v))

    def __getitem__(self, key):
        h_k = self.hash(key)
        if self.data[h_k] is None:
            KeyError("{} is not valid.".format(key))
        else:
            for k, v in self.data[h_k]:
                if key == k:
                    return v

    def __setitem__(self, key, value):
        alpha = float(self.n) / self.m
        if alpha > 0.5:
            self.double()
        h_k = self.hash(key)
        if self.data[h_k] is None:
            self.data[h_k] = list()
        self.data[h_k].append((key, value))

    def __delitem__(self, key):
        alpha = float(self.n) / self.m
        if alpha < 0.25:
            self.quarter()
        h_k = self.hash(key)
        for k, v in self.data[h_k]:
            if k == key:
                self.data[h_k].remove((k, v))
                return
            if v is None:
                break
        KeyError("{} is not valid.".format(key))

    def keys(self):
        res = []
        for chain in self.data:
            if not chain is None:
                for k, v in chain:
                    res.append(k)
        return res

    def hash(self, k):
        return hash(k) % self.m

    def double(self):
        m = self.m
        self.m *= 2
        new = [None for _ in range(0, self.m)]
        for i in range(0, m):
            for (k, v) in self.data[i]:
                h_k = self.hash(k)
                new[h_k] = v
        self.data = new

    def quarter(self):
        m = self.m
        self.m /= 4
        new = [None for _ in range(0, self.m)]
        for i in range(0, m):
            for (k, v) in self.data[i]:
                h_k = self.hash(k)
                new[h_k] = v
        self.data = new

if __name__ == '__main__':
    import tests
    tests.do_tests()