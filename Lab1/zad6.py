import random
import matplotlib.pyplot as plt
import numpy as np
numbers = []
numMany = []
id = 1
for x in range(100) :
    numbers.append(random.randint(1, 20))
    print(numbers[x])

for num in range(1,21) :
    numMany.append(numbers.count(num))
for x in range(0,20) :
    print(f"in list is {numMany[x]} for number == {x+1}")

freq = np.array(numMany)
ran = np.array(range(1,21))

ypos=np.arange(len(ran)) + 1

plt.bar(ypos-0.2, freq, width=0.4, label='frequncy', color='red')


plt.title('jak czesto losowa liczba powiela sie na range 1-20')
plt.xticks(ypos,ran)
plt.xlabel('liczby')
plt.ylabel('czestotliwosc')
plt.legend()
plt.show()
