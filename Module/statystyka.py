import statistics



numbers =[5.56, 8.8, 7, 6, 4, 7, 56, 98, 1020, 1.1]


print(round(statistics.mean(numbers), 2))

print(round(statistics.median(numbers), 2))


from statistics import NormalDist

IQ = NormalDist(mu=100, sigma = 5)
prob = round(IQ.cdf(104) - IQ.cdf(100), 4)
print(prob)
print(f'Probability: {round(100 * prob)}%')

# prawdopodobienstwo znalezienia osob IQ pomiedzy 100 i 104