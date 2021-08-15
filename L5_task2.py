# 2.	Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в
# каждой строке.

try:
    with open('task2_file.txt', 'r', encoding='utf-8') as file_reader:
        data = [data_string.split() for data_string in file_reader]
        print(data)
        print(f'Strings: {len(data)}')
        for i in range(0, len(data)):
            print(f'In string {i + 1}, words: {len(data[i])}')
except IOError:
    print(f'IOError.')


# str a
