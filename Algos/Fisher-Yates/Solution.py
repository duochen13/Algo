
import random

class UniqueRandomNumberGenerator:

    def __init__(self, lowerbound, upperbound):
        assert lowerbound <= upperbound
        self.data = [_ for _ in range(lowerbound, upperbound + 1)]
        random.shuffle(self.data)

    def get(self):
        if not self.data:
            # or reset
            raise Exception('ERROR: Not enough data.')
        return self.data.pop()


class FisherRandomNumberGenerator:

    def __init__(self, lowerbound, upperbound):
        self.data = [ _ for _ in range(lowerbound, upperbound + 1)]
        for i in range(upperbound - lowerbound):
            j = random.randint(0, i)
            self.data[i], self.data[j] = self.data[j], self.data[i]


    def get(self):
        if not self.data:
            # or reset
            raise Exception('ERROR: Not enough data.')
        return self.data.pop()



if __name__ == '__main__':
    rng = FisherRandomNumberGenerator(3,10)
    try:
        for i in range(7):
            res = rng.get()
            print(res)
    except Exception:
        print("Oops, sth went wrong")