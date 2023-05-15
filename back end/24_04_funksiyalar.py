# from funksiyalar19_04 import raqamlar

# raqamlar(100)
import math

x=400
print(math.sqrt(x))

# def daraja_chiqar(x, y = 2):
#     return f"Daraja: | {x} ^ {y} = {x**y}"

# x = daraja_chiqar(3)
# print(x)


# def bolish(raqam):
#     for i in range(2, 11):
#         if raqam % i == 0:
#             print(f"{raqam} {i} ga qoldiqsiz bo'linadi")

# son = input("Raqam kiriting: ")
# son = int(son)
# bolish(son)






def oraliq(min,max):
    sonlar = [] # bo'sh ro'yxat
    while min<max:
        sonlar.append(min)
        min += 2
    return sonlar

# print(oraliq(0,10))
# print(oraliq(10,21))


# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     qiymatlar = [kompaniya, model, rangi, korobka, yili, narhi]
#     # for i in range(6):
#     avtolar.append(qiymatlar)
#     # avtolar.append(kompaniya, model, rangi, korobka, yili, narhi)
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
# print(avtolar)



