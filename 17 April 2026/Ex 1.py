class Statistics:
    def __init__(self, data:list=None):
        if len(data) == 0:
            self.data = None
        else:
            self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def range(self):
        return max(self.data) - min(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        return sorted(self.data)[len(self.data) // 2]

    def mode(self):
        max_counted = self.data[0]
        for value in self.data:
            if self.data.count(value) > self.data.count(max_counted):
                max_counted = value
        return max_counted

    def std(self):
        return round(self.var() ** 0.5, 1)

    def var(self):
        return round(sum((x - self.mean()) ** 2 for x in self.data) / self.count(), 1)

    def freq_dist(self):
        frequency = {}

        for item in self.data:
            frequency[item] = frequency.get(item, 0) + 1

        total = self.count()
        result = []
        for value, count in frequency.items():
            percentage = (count / total) * 100
            result.append((percentage, value))

        result.sort(reverse=True)
        return result

    def describe(self):
        return (
            f"Count: {self.count()}\n"
            f"Sum:  {self.sum()}\n"
            f"Min:  {self.min()}\n"
            f"Max:  {self.max()}\n"
            f"Range:  {self.range()}\n"
            f"Mean:  {self.mean()}\n"
            f"Median:  {self.median()}\n"
            f"Mode:  {self.mode()}\n"
            f"Variance:  {self.var()}\n"
            f"Standard Deviation:  {self.std()}\n"
            f"Frequency Distribution: {self.freq_dist()}"
        )