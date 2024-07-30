class Sample:
    def __init__(self):
        self.a = 1
        self._b = 1
        self.__c = 1
        self.__d_ = 1
        self.__e__ = 1

    def show_attribute(self):
        a = self.a
        b = self._b
        c = self.__c
        d = self.__d_
        e = self.__e__
        print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")

s = Sample()
s.show_attribute()

print(s.a)
print(s._b)
