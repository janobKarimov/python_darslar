# def daraja(n):
#     return lambda x : x**n

# kvadrat = daraja(2)
# kub = daraja(3)
# # print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")


# import math
# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))


# with open('pi.txt') as fayl:
#     pi = fayl.read()
#     pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
#     pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
#     pi = float(pi) # matnni float (o'nlik) songa o'tkazamiz
#     print(pi)
# try:
#     fayl = open('bot/bot/2.0/px.txt')
#     pi = fayl.read()
#     print(pi)
#     fayl.close()
# except FileNotFoundError:
#     print("xato")

# faylnomi = "c:/Users/Mirzo/Desktop/Wester/Foundation/bot/bot/2.0/pi.txt"
# faylnomi = 'bot/bot/2/pi.txt'
# with open(faylnomi) as fayl:
#     pi = fayl.read()
#     print(pi)

filename = 'talabalar.txt'
with open(filename) as file:
    talabalar = file.readlines()

# print(talabalar)


# faylnomi = 'ustozlar.txt'# ochilayotgan (yaratilayotgan) fayl nomi
# with open(faylnomi,'w') as fayl:
#     fayl.write('anvar narzullaev')
#     fayl.write('\nTuxumbek') # faylga yozilayotgan ma'lumot

# with open(faylnomi,'a') as fayl:
#     fayl.write('Alijon Valiyev\n')
#     fayl.write('2000')


# faylnomi = 'dars.txt'# ochilayotgan (yaratilayotgan) fayl nomi
# with open(faylnomi,'w') as fayl:
#     fayl.write('''Ushbu bo'limda katta hajmdagi ma'lumotlarni fayldan yuklab olish va dastur yakunida kerakli ma'lumotlarni va dastur natijasini faylga saqlashni o'rganamiz. Fayllar bilan ishlash dastur foydalanuvchilariga ham dasturga o'zlari istagan ma'lumotlarni yuklash imkoniyatini beradi.''')
#     # fayl.write('\nTuxumbek') # faylga yozilayotgan ma'lumot

# faylnomi = 'dars.txt'
# with open(faylnomi) as fayl:
#     print(fayl.read())

with open("pi_million_digits.txt") as file:
    pi = file.read()
pi = pi.rstrip()  # qator ohiridagi bo'shliqlarni olib tashlaymiz
pi = pi.replace("\n", "")  # qator tashlash belgisini almashtiramiz
pi = pi.replace(" ", "")

# Tug'ilgan kunim pi da bormi?
bdate = "010320"
print(bdate in pi)
