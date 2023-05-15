# def kattasi(x,y,z):

#     max = x
#     if y > max:
#         max = y
#     if z >= max:
#         max = z
#     return max

# def aylana_info(radius, pi=3.14159):
#     aylana = {
#         "radius": radius,
#         "diametr": 2* radius,
#         "perimetr": 2 * radius * pi,
#         "yuza": pi * radius ** 2,
#     }
#     return aylana

# def fibonacci(n):

#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)        
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#             sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#     return sonlar


# print(fibonacci(10))


# def area(radius):
#     area = 3.14*radius*radius
#     return area

# radius = int(input("Radius kiriting: "))
# print(area(radius))

# import math

# print(math.sqrt(13689))

# def computepay(hours, rate):
#     if hours > 40:
#         overtime = hours - 40
#         overtime_pay = overtime * rate * 1.5
#         pay = 40 * rate + overtime_pay
#     else:
#         pay = hours * rate
#     return pay

# hours = float(input("Enter Hours: "))
# rate = float(input("Enter Rate: "))
# pay = computepay(hours, rate)
# print("Pay:", pay)


# def user_info(ism, yosh):
#     tugilgan_yil = 2023 - yosh
#     print(f"{ism} foydalanuvchisi {tugilgan_yil}-yilda tug'ilgan")

# def kvadrat_va_kub(num):
#     print(f"{num} ning kvadrati {num**2}, kubi {num**3}")

# def juft_yoki_toq(num):
#     if num % 2 == 0:
#         print(f"{num} juft son")
#     else:
#         print(f"{num} toq son")

# def katta_son(son1, son2):
#     if son1 == son2:
#         print("Sonlar teng")
#     elif son1 > son2:
#         print(f"{son1} katta son")
#     else:
#         print(f"{son2} katta son")

# def katta_kichik(x, y):
#     if x > y:
#         print(f"Katta son: {x}")
#         print(f"Kichik son: {y}")
#     elif x < y:
#         print(f"Katta son: {y}")
#         print(f"Kichik son: {x}")
#     else:
#         print("Sonlar teng")


# def min_max(x=2, y=2):
#     if x > y:
#         print(f"Katta son: {x}")
#         print(f"Kichik son: {y}")
#     elif x < y:
#         print(f"Katta son: {y}")
#         print(f"Kichik son: {x}")
#     else:
#         print("Sonlar teng")


# def qoldiqsiz_bolinish(num):
#     for i in range(2, 11):
#         if num % i == 0:
#             print(f"{num} soni {i} ga qoldiqsiz bo'linadi")
#         else:
#             print(f"{num} soni {i} ga qoldiqsiz bo'linmaydi")


# def user_info(Ism, Familiya, Tugilgan_yil, Yashash_joyi, Email="", Telfon_nomeri="", Yoshi=""):
#     user = {"Ism": Ism,
#             "Familiya": Familiya,
#             "Tug'ilgan yili": Tugilgan_yil,
#             "Tug'ilgan joyi": Yashash_joyi,
#             "Email manzil": Email,
#             "Telefon raqami": Telfon_nomeri,
#             "Yoshi": Yoshi}
#     return user


# mijozlar = []
# while True:
#     mijoz = input("Mijoz ismi: ")
#     if mijoz == "":
#         break
#     mijozlar.append(mijoz)

# for mijoz in mijozlar:
#     print(mijoz)

# def max_of_three(a, b, c):
#     return max(a, b, c)

# def circle_info(radius):
#     pi = 3.14
#     diameter = 2 * radius
#     perimeter = 2 * pi * radius
#     area = pi * radius ** 2
#     return {"radius": radius, "diameter": diameter, "perimeter": perimeter, "area": area}

# def prime_numbers(n):
#     primes = []
#     for num in range(2, n+1):
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             primes.append(num)
#     return primes

# def fibonacci(n):
#     fib = [1, 1]
#     for i in range(2, n):
#         fib.append(fib[i-1] + fib[i-2])
#     return fib[:n]

# def multiply_numbers(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result

# def student_info(first_name, last_name, **kwargs):
#     student = {"first_name": first_name, "last_name": last_name}
#     for key, value in kwargs.items():
#         student[key] = value
#     return student