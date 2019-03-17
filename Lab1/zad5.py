import random
import math

def randomizeVec1():
    vector1 = []
    for x in range(0, 9):
        randomNumber = random.randrange(20)
        vector1.append(randomNumber)
    return vector1

def randomizeVec2():
    vector2 = []
    for x in range(0, 9):
        randomNumber = random.randrange(20)
        vector2.append(randomNumber)
    return vector2

def iloSkalarny(vect1,vect2):
    iloczynSkalarny=0
    for x in range(0, 9):
        iloczynSkalarny = iloczynSkalarny + (vector1[x]*vector2[x])
    return iloczynSkalarny

#
def dlugosci_wektorow(vec1,vec2):
    dlugoscWektora1 = 0
    dlugoscWektora2 = 0
    for x in range(0, 9):
        dlugoscWektora1 = dlugoscWektora1 + (vector1[x]*vector1[x])
        dlugoscWektora2 = dlugoscWektora2 + (vector2[x] * vector2[x])
    print("dlugosc wektora pierwszego: ", math.sqrt(dlugoscWektora1))
    print("długość wektora drugiego: ", math.sqrt(dlugoscWektora2))
    return [dlugoscWektora1,dlugoscWektora2]

def cos(iloczynSkalarny,dlug) :
#cos
    cosinus = iloczynSkalarny/(math.sqrt(dlug[0])*math.sqrt(dlug[1]))
    print("cosinus: ",cosinus)

    stopnie = cosinus * 180 / math.pi
    print("Stopnie: ",stopnie)
    radiany = stopnie * math.pi / 180
    print("Radiany: ",radiany)

vector1 = randomizeVec1()
vector2 = randomizeVec2()
ilo = iloSkalarny(vector1,vector2)
dlug=dlugosci_wektorow(vector1,vector2)
cos(ilo,dlug)
