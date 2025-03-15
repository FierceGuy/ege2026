# (№ 6626) (Е. Джобс) Катя составляет 5-буквенные слова из букв слова АПРЕЛЬ и упорядочивает
# их в обратном алфавитном порядке. Начало списка выглядит так:

# 1. ЬЬЬЬЬ
# 2. ЬЬЬЬР
# 3. ЬЬЬЬП
# 4. ЬЬЬЬЛ
# 5. ЬЬЬЬЕ
# 6. ЬЬЬЬА
# 7. ЬЬЬРЬ
# ...

# Сколько слов, оканчивающихся на Ь, запишет Катя, если заполнит список до 387 позиции (включительно)? 

number = 1
alphabet = "ЬРПЛЕА"
counter = 0

for char1 in alphabet:
    for char2 in alphabet:
        for char3 in alphabet:
            for char4 in alphabet:
                for char5 in alphabet:
                    word = char1 + char2 + char3 + char4 + char5

                    if char5 == "Ь" and number <= 387:
                        counter += 1

                    number +=1

print (counter)

