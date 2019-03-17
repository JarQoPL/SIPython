text = str(input("Podaj imię i nazwisko bez spacji "))
imie = text[0:6]
nazwisko = text[6:]
print ("Twoje imię : ",imie)
print ("Twoje nazwisko : ", nazwisko)
print("Długość nazwiska: ",len(nazwisko))
print("Nazwisko z małych liter: ",nazwisko.lower())
