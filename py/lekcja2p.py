import random
znaki = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
x = int(input("Podaj długość hasła"))
haslo = ""
for i in range (x):
    haslo+=random.choice(znaki)

print("twoje wygenerowane hasło", haslo)
