# Поиск и замена слов в содержимом текстового файла

# You are an inspiration for lots of people.
def FindNChange(file, word_in_file, new_word):
    with open(file, mode='r') as f:
        str1 = f.readline()

    with open(file, mode='w') as f:
        str1 = str1.split(' ')
        for i in range(len(str1)):
            if str1[i] == word_in_file:
                str1[i] = new_word
        str1 = ' '.join(str1)
        f.writelines(str1)

# FindNChange("text.txt", "as", "new")


# Подсчет количества слов в содержимом текстового файла, которые не являются числами
def CountWords(file):
    with open(file, mode='r') as f:
        str1 = f.readline()
        str1 = str1.split(' ')
        print(str1)
        n = 0
        for i in str1:
            if i == int:
                n+=0
            elif i == bool:
                n+=0
            n+=1
    print(f'Кол-во слов, которые не являются числами в файле: {n}')

CountWords("text.txt")