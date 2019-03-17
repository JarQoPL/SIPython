import random
import statistics
import numpy
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

srednia = numpy.average(newNumbers)
print ("Średnia: ",srednia)

odchylenieStandardowe = statistics.stdev(numbers)
print("Odchylenie standardowe: ",odchylenieStandardowe)

#wektorZnormalizowany
wektorZnormalizowany = []
for x in range(0, 30):
    wZ = (newNumbers[x]-minimum)/(maximum-minimum)
    wektorZnormalizowany.append(wZ)
#Wektor standaryzowany
wektorStanryzowany =[]
for x in range(0, 30):
    wS = (newNumbers[x]-srednia)/odchylenieStandardowe
    wektorStanryzowany.append(wS)

print("Wektor znormalizowany: ", wektorZnormalizowany)

print("Wektor standaryzowany: ", wektorStanryzowany)
