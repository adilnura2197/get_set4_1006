royxat1 = [1, 2, 3, 4, 5]
royxat2 = [4, 5, 6, 7, 8]

set1 = set(royxat1)
set2 = set(royxat2)

print("Birlashma:", set1 | set2)
print("Kesishma:", set1 & set2)
print("Ayirma:", set1 - set2)


matn = input("Matn kiriting: ")

unikal = set(matn)

print("Unikal belgilar soni:", len(unikal))


uchga = set()
beshga = set()

for i in range(1, 101):
    if i % 3 == 0:
        uchga.add(i)

    if i % 5 == 0:
        beshga.add(i)

print("3 ga bo'linadiganlar:", uchga)
print("5 ga bo'linadiganlar:", beshga)

print("Ikkalasiga ham bo'linadiganlar:", uchga & beshga)
