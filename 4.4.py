class Time:
    def __init__(self, h, m, s):
        self.__h, self.__m, self.__s = h, m, s

    def display(self):
        print(f"{self.__h:02d}:{self.__m:02d}:{self.__s:02d}")

    def __add__(self, other):
        s = (self.__s + other.__s) % 60
        m = (self.__m + other.__m + (self.__s + other.__s)//60) % 60
        h = self.__h + other.__h + (self.__m + other.__m + (self.__s + other.__s)//60)//60
        return Time(h, m, s)


h1 = int(input("Enter hours for Time 1: "))
m1 = int(input("Enter minutes for Time 1: "))
s1 = int(input("Enter seconds for Time 1: "))
t1 = Time(h1, m1, s1)

h2 = int(input("Enter hours for Time 2: "))
m2 = int(input("Enter minutes for Time 2: "))
s2 = int(input("Enter seconds for Time 2: "))
t2 = Time(h2, m2, s2)

t3 = t1 + t2
print("Sum of times:", end=" ")
t3.display()
