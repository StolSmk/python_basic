# 4.	Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
# нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

input_words = input('Input some words: ').split(' ')

my_dict = {}
i = 1

for word in input_words:
    my_dict.update({i:word[:10]})
    i = i + 1

for number, word in my_dict.items():
    print(f'{number}. {word}')
