# Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды, 
# в обеих командах v и w обозначают цепочки символов.
# 1. заменить (v, w) 
# 2. нашлось (v)
# Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в строке нет, 
# эта команда не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор.
# Дана программа для исполнителя Редактор:
# ПОКА нашлось (111) ИЛИ нашлось (88888)
#   ЕСЛИ нашлось (111)
#     ТО заменить (111, 88)
#     ИНАЧЕ заменить (88888, 8)
#   КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 83 идущих
#  подряд цифр 8?

def editor(s):
    while "111" in s or "88888" in s:
        if "111" in s:
            s = s.replace("111", "88", 1)  # Заменяем первое вхождение "111" на "99"
        else:
            s = s.replace("88888", "8", 1)  # Заменяем первое вхождение "" на "3"
    return s

# Исходная строка из 83 цифры 8
start_line = "8" * 83
result = editor(start_line)
print(result)

