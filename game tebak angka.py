import random

angka_rahasia = random.randint(1, 100)
kesempatan = 5

while kesempatan > 0:
 tebak = int(input("Tebak angka (1-100): "))
 if tebak == angka_rahasia:
 print("Selamat! Anda menang!")
 break
 elif tebak < angka_rahasia:
 print("Terlalu rendah!")
 else:
 print("Terlalu tinggi!")
 kesempatan -= 1
else:
 print("Anda kalah! Angka rahasia:", angka_rahasia)
