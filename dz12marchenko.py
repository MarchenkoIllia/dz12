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

