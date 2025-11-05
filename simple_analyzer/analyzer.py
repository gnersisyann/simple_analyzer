class Analyzer:
    def __init__(self):
        self.numbers = []

    def add_number(self, x):
        self.numbers.append(int(x))

    def even_count(self):
        count = 0
        for number in self.numbers:
            if number % 2 == 0:
                count = count + 1
        return count

    def odd_count(self):
        count = 0
        for number in self.numbers:
            if number % 2 != 0:
                count = count + 1
        return count

    def highest_number(self):
        if len(self.numbers) == 0:
            return None
        
        highest = self.numbers[0]
        for number in self.numbers:
            if number > highest:
                highest = number
        return highest

    def increasing_pairs(self):
        if len(self.numbers) < 2:
            return 0
        
        count = 0
        for i in range(1, len(self.numbers)):
            if self.numbers[i] > self.numbers[i-1]:
                count = count + 1
        return count