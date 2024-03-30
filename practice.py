class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        if self.capacity < 0:
            raise ValueError


    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError
        return self.size

    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError
        return self.size

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self,size=0):
        self.size = size

def main():
    cookies = Jar()
    print(cookies)



if __name__ == "__main__":
    main()
