#4
# Определить позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
A = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
result = -1
if len(A):
    pos = A[0]
    for i in range(len(A)):
        if i > 0:
            if A[i] == pos:
                result = i
                break
            else:
                result = -1
print(result)