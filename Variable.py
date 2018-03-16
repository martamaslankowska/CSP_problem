class Variable:
    # count = 0

    def __init__(self, i, j, domain, val=0):
        # Variable.count += 1
        # self.value = Variable.count
        self.value = val
        self.color = "#FFFFF0"
        self.domain = domain
        self.i = i
        self.j = j

    def get_value(self):
        print("Value of this variable is:", self.value)
        return self.value



