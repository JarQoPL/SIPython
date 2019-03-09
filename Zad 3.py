import random
import np
import statistics

numbers = []
for x in range(0, 30):
    randomNumber = random.randrange(100)
    numbers.append(randomNumber)

print ("Wektor: ",numbers)

minimum = min(numbers)
maximum = max(numbers)
print ("Min: ", minimum)
print ("Max: ", maximum)

newNumbers = sorted(numbers)

print ("Posortowany wektor: ",newNumbers)

srednia = np.average(newNumbers)
print ("Średnia: ",srednia)

odchylenieStandardowe = statistics.stdev(numbers)
print("Odchylenie standardowe: ",odchylenieStandardowe)

#wektorZnormalizowany
wektorZnormalizowany = []
for x in range(0, 29):
    wZ = (newNumbers[x]-minimum)/(minimum-maximum)
    wektorZnormalizowany.append(wZ)
#Wektor standaryzowany
for x in range(0, 29):
    wS = (newNumbers[x]-srednia)/odchylenieStandardowe
    wektorZnormalizowany.append(wS)

print("Wektor znormalizowany: ", wZ)

print("Wektor standaryzowany: ", wS)