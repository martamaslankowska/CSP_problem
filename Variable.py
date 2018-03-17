class Variable:
    count = 0

    def __init__(self, i, j, domain, val=-1):
        Variable.count += 1
        self.nr = Variable.count
        self.value = val
        self.color = "#FFFFBB"
        self.domain = domain
        self.i = i
        self.j = j

    def get_value(self):
        print("Value of this variable is:", self.value)
        return self.value

    def get_domain(self):
        print("Domain of variable ({0},{1}) is:".format(self.i, self.j), self.domain)



