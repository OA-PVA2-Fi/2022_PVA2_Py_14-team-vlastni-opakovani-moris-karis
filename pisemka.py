#1
for i in range(1, 11):
    print(i * 3)

#2
A = 69
B = 29

if A > B:
    print("A je větší než B.")
elif A < B:
    print("A je menší než B.")
elif A == B:
    print("A i B si jsou rovné.")

#3
cislo = int(input("Zadejte číslo: "))
for i in range(0, 21):
    print(i * cislo)

#4
cisla = [8, 176, 29, 43, 848, 64, 152, 17, 205, 56]

for num in cisla:
    if num % 8 == 0 and num > 42 and num < 208:
        print(num)
