my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["d"]
except KeyError:
    print("Kalit so'z yo'q!")
else:
    print("Bexato!")
finally:
    print("The finally statement ran!")


# for num in range(2, 8):
#     if not num % 2:
#         continue
#     print(num)

# print(range(5, 10)[-1])
# print(range(0, 10, 3)[2])
# print(range(-10, -100, -30)[1])


# def matrix_find(matrix, value):
#     if not matrix or not matrix[0]:
#         return False
#     j = len(matrix) - 1
#     for row in matrix:
#         while row[j] > value:
#             j = j - 1
#         if j == -1:
#             return False
#         if row[j] == value:
#             return True
#     return False
# matrix = [[3, 4, 4, 6],
# [6, 8, 11, 12],
# [6, 8, 11, 15],
# [9, 11, 12, 17]]
# print(matrix_find(matrix=matrix, value=11))


def qoshish(*args, ajratuvchi="/"):
    return ajratuvchi.join(args)
# print(qoshish("A", "B", "C", ajratuvchi=","))


# x = 'ali'
# y = 'vali'
# z = ''
# z = ' | '.join([x, y])
# print(z)


# words = [ 'cat' , 'mouse' , 'dog' ]
# for word in words[:]:
#     if len(word) > 3:
#         words.remove(word)
#         words.insert(0, word)
# print(words[0])
# print(words)

# print("""
# A
# B
# C
# """ == "\nA\nB\nC\n")


# print(' P"yt\'h"on ')


# def func(val1=3, val2=4, val3=6):
#     return val1 + val2 + val3
# values = {"val1":9, "val3":-1}
# print(func(**values))


# print("Answer")
# while True:
#     pass
# print("42")

royxat = [1,2,3,4,4,5,6,6,7,8,9,9,10]

# ENDI RO'YXATDAN FAQAT BIR DONASINI QOLDIRING 
    # if royxat


# print(royxat)