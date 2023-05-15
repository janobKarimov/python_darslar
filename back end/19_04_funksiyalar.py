# def my_function():
#   print("Hello from a function")


# my_function()


# def my_function(ism):
#   print(ism + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil")


# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, 
#         unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.upper()}!")

# salom_ber("bomms")
n ** 2
n ** 3
def salom_ber2():
    """Fodyalanuvchi ismini qabul qilib, 
        unga salom beruvchi funksiya"""
    ism = str(input("Ism kiriting: ")) 

    if ism == 'mirzo' or ism == "MIRZO" or ism == 'Mirzo':
        print(f"Assalomu alaykum, hurmatli 👑 Qirol {ism.upper()}!")

    else:
        print(f"Assalomu alaykum, hurmatli {ism.upper()}!")


# for i in range(4):
#     salom_ber2()

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")

# toliq_ism('olim','hakimov')

# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2023-tugilgan_yil} yoshda")

# # yosh_hisobla('olim', 2008)
# yosh_hisobla(tugilgan_yil=1997, ism='olim')

# import random

# def raqamlar(n = 10):
#     for i in range(10):
#         print(random.randint(1, n))

# raqamlar(100)


# def yosh_hisobla(tugilgan_yil, joriy_yil=2023):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# tyil = input("Tug'ilgan yilingizni kiriting: ")
# tyil = int(tyil)
# yosh_hisobla(tyil)

# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# yosh_hisobla(1993)

# def salom_ber(s):
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
#     print(s)

# salom_ber('hasan')

def yosh_hisobla(tugilgan_yil, joriy_yil=2023):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Hurmatli {ism} Siz {joriy_yil-tugilgan_yil} yoshdasiz")
ism = input("Ism kiritng:")   
tyil = input("Tug'ilgan yilingizni kiriting: ")
tyil = int(tyil)
yosh_hisobla(tyil)
