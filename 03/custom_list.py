
class CustomList(list):

    def __init__(self, *args):
        super().__init__(*args)

    def __add__(self, other):
        if isinstance(other, CustomList):
            result = self
            while len(self) != len(other):
                if len(self) < len(other):
                    self.append(0)
                else:
                    other.append(0)
            for i in range(len(self)):
                result[i] += other[i]
            return result
        raise TypeError("Not CustomList")

    def __sub__(self, other):
        if isinstance(other, CustomList):
            result = self
            while len(self) != len(other):
                if len(self) < len(other):
                    self.append(0)
                else:
                    other.append(0)
            for i in range(len(self)):
                result[i] -= other[i]
            return result
        raise TypeError("Not CustomList")

    def __str__(self):
        return super().__str__() + f" summa = {sum(self)}"

    def __lt__(self, other):
        if isinstance(other, CustomList):
            return sum(self) < sum(other)
        raise TypeError("Not CustomList")

    def __eq__(self, other):
        if isinstance(other, CustomList):
            return sum(self) == sum(other)
        raise TypeError("Not CustomList")

    def __le__(self, other):
        if isinstance(other, CustomList):
            return sum(self) <= sum(other)
        raise TypeError("Not CustomList")

    def __ne__(self, other):
        if isinstance(other, CustomList):
            return sum(self) != sum(other)
        raise TypeError("Not CustomList")

    def __gt__(self, other):
        if isinstance(other, CustomList):
            return sum(self) > sum(other)
        raise TypeError("Not CustomList")

    def __ge__(self, other):
        if isinstance(other, CustomList):
            return sum(self) >= sum(other)
        raise TypeError("Not CustomList")
