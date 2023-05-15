# def ping(i):
#     if i > 0:
#         return pong(i - 1)
#     return "0"
# def pong(i):
#     if i > 0:
#         return ping(i - 1)
#     return "1"

# print(ping(3))


# def ask(prompt, retries=4, output=  'Error '):
#     for _ in range(retries):
#         response = input(prompt).lower()
#         if response in [ 'y' , 'yes' ]:
#             return True
#         if response in [ 'n', 'no' ]:
#             return False
#     print(output)
# print(ask( "Want to know the answer?" , 5))

# letters = [ 'a','b','c','d' ]
# print(letters[1:-1])

# x, y, z = 1, 2, 3 


a = 3000
b = 222
c = 22

def eng_kattasi(a, b, c):
    katta = 0
    if a > b and a > c:
        katta = a
    elif b > a and b > c:
        katta = b
    else:
        katta = c
    return katta
        

x = eng_kattasi(a, b, c)
# print(x)



unlilar = ['a', 'e', 'i', 'o', 'u']

word = "pythonlobby"

def hisoblovchi(word):
    unli = 0
    undosh = 0
    for harf in word:
        if harf in unlilar:
            unli +=1
        else:
            undosh+=1
    print(f"unlilar: {unli} undoshlar: {undosh}")

# hisoblovchi(word)


def factorial(n):
    facto = 1
    while n>0:
        facto = facto * n
        n = n - 1
        # print("doimiy while")
    return facto
# print(factorial(6))


def kattalashtirgich(soz):
    return soz.upper()
soz = "blllleeeeeeeee"
# print(soz.upper())
print(kattalashtirgich(soz))