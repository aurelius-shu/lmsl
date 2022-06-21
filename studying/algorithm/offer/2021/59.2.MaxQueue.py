class MaxQueue:

    def __init__(self):
        self.q = []
        self.m = []

    def max_value(self):
        return self.m[0] if self.m else -1

    def push_back(self, value):
        while self.m and self.m[-1] < value:
            self.m.pop()
        self.m.append(value)
        self.q.append(value)

    def pop_front(self):
        if not self.m:
            return -1
        ans = self.q[0]
        self.q = self.q[1:]
        if self.m[0] == ans:
            self.m = self.m[1:]
        return ans


# Your MaxQueue object will be instantiated and called as such:
obj = MaxQueue()
obj.push_back(1)
obj.push_back(2)
param_1 = obj.max_value()
print(param_1)
param_2 = obj.pop_front()
print(param_2)
param_3 = obj.max_value()
print(param_3)
